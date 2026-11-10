import os
import math

from flask import Flask, jsonify, request, session
from flask_cors import CORS #pyright: ignore[reportMissingModuleSource]
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

from config import Config
from extensions import db
import models


app = Flask(__name__)

frontend_origin = os.getenv(
    "FRONTEND_ORIGIN",
    "http://127.0.0.1:5500"
)

CORS(
    app,
    resources={
        r"/transactions.*": {
            "origins": frontend_origin
        },
        r"/auth/.*": {
            "origins": frontend_origin
        }
    },
    supports_credentials=True
)

app.config.from_object(Config)

is_production = frontend_origin.startswith("https://")

app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="None" if is_production else "Lax",
    SESSION_COOKIE_SECURE=is_production,
    PERMANENT_SESSION_LIFETIME=3600
)

db.init_app(app)

with app.app_context():
    db.create_all()

with app.app_context():
    db.session.execute(text("""
        ALTER TABLE transactions
        ADD COLUMN IF NOT EXISTS user_id INTEGER
        REFERENCES users(id)
    """))
    db.session.commit()

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"error": "Please login first"}), 401

        return func(*args, **kwargs)

    return wrapper

@app.route("/auth/signup", methods=["POST"])
def signup():
    data = request.get_json()

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

    name = data.get("name", "").strip()
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not name or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    if len(name) > 100 or len(email) > 120:
        return jsonify({"error": "Name or email is too long"}), 400

    if "@" not in email or "." not in email:
        return jsonify({"error": "Enter a valid email"}), 400

    if len(password) < 8:
        return jsonify({
            "error": "Password must be at least 8 characters"
        }), 400

    if models.User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 409

    new_user = models.User(
        name=name,
        email=email,
        password_hash=generate_password_hash(password)
    )

    try:
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "message": "Account created successfully!"
        }), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already registered"}), 409

    except Exception:
        db.session.rollback()
        app.logger.exception("Signup failed")
        return jsonify({"error": "Could not create account"}), 500
    

@app.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = models.User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid email or password"}), 401

    session.clear()
    session["user_id"] = user.id
    session.permanent = True

    return jsonify({
        "message": "Login successful!",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }), 200


@app.route("/")
def home():
    return jsonify({
        "message": "Expense Tracker API is running!",
        "database": "Configuration loaded"
    })


@app.route("/db-test")
def db_test():
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({"status": "Database connected"})

    except Exception:
        app.logger.exception("Database connection test failed")
        return jsonify({"error": "Database connection failed"}), 500


@app.route("/transactions", methods=["POST"])
@login_required
def add_transaction():
    data = request.get_json()

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

    required_fields = ["amount", "category", "type"]

    if not all(key in data for key in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        amount = float(data["amount"])
    except (ValueError, TypeError):
        return jsonify({"error": "Amount must be a valid number"}), 400

    if not math.isfinite(amount) or amount <= 0:
        return jsonify({"error": "Amount must be greater than zero"}), 400

    category = data["category"]
    transaction_type = data["type"]

    if transaction_type not in ["income", "expense"]:
        return jsonify({"error": "Invalid transaction type"}), 400

    if not isinstance(category, str) or not category.strip():
        return jsonify({"error": "Category cannot be empty"}), 400

    if transaction_type == "expense":
        allowed_categories = [
            "Food", "Travel", "Shopping", "Bills", "Other"
        ]
    else:
        allowed_categories = [
            "Salary", "Pocket Money", "Gift", "Other Income"
        ]

    if category.strip() not in allowed_categories:
        return jsonify({
            "error": "Invalid category for this transaction type"
        }), 400

    description = data.get("description", "")

    if not isinstance(description, str):
        return jsonify({"error": "Description must be text"}), 400

    if len(description) > 255:
        return jsonify({
            "error": "Description cannot exceed 255 characters"
        }), 400

    try:
        new_transaction = models.Transaction(
            user_id=session["user_id"],
            amount=amount,
            category=category.strip(),
            description=description.strip(),
            type=transaction_type
        )

        db.session.add(new_transaction)
        db.session.commit()

        return jsonify({
            "message": "Transaction added successfully!",
            "id": new_transaction.id
        }), 201

    except Exception:
        db.session.rollback()
        app.logger.exception("Transaction save failed")
        return jsonify({"error": "Could not save transaction"}), 500


@app.route("/auth/logout", methods=["POST"])
@login_required
def logout():
    session.clear()

    return jsonify({
        "message": "Logged out successfully!"
    }), 200


@app.route("/auth/me", methods=["GET"])
def current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Not logged in"}), 401

    user = db.session.get(models.User, user_id)

    if not user:
        session.clear()
        return jsonify({"error": "User not found"}), 401

    return jsonify({
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }), 200

@app.route("/transactions", methods=["GET"])
@login_required
def get_transactions():
    user_id = session["user_id"]

    transactions = models.Transaction.query.filter_by(
        user_id=user_id
    ).order_by(
        models.Transaction.id.desc()
    ).all()

    return jsonify([
        {
            "id": t.id,
            "amount": t.amount,
            "category": t.category,
            "description": t.description,
            "type": t.type,
            "date": t.date.isoformat() if t.date else None
        }
        for t in transactions
    ])


@app.route("/transactions/<int:transaction_id>", methods=["PUT"])
@login_required
def update_transaction(transaction_id):
    transaction = models.Transaction.query.filter_by(
        id=transaction_id,
        user_id=session["user_id"]
    ).first_or_404()

    data = request.get_json()

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

    new_amount = transaction.amount
    new_type = transaction.type

    if "amount" in data:
        if isinstance(data["amount"], bool):
            return jsonify({"error": "Invalid amount"}), 400

        try:
            new_amount = float(data["amount"])
        except (ValueError, TypeError):
            return jsonify({"error": "Amount must be a valid number"}), 400

        if not math.isfinite(new_amount) or new_amount <= 0:
            return jsonify({"error": "Amount must be greater than zero"}), 400

    if "type" in data:
        new_type = data["type"]

        if new_type not in ["income", "expense"]:
            return jsonify({"error": "Invalid transaction type"}), 400

    if "category" in data:
        category = data["category"]

        if not isinstance(category, str) or not category.strip():
            return jsonify({"error": "Category cannot be empty"}), 400

        if new_type == "expense":
            allowed_categories = [
                "Food",
                "Travel",
                "Shopping",
                "Bills",
                "Other"
            ]
        else:
            allowed_categories = [
                "Salary",
                "Pocket Money",
                "Gift",
                "Other Income"
            ]

        if category.strip() not in allowed_categories:
            return jsonify({
                "error": "This category is not allowed for this transaction type."
            }), 400

    if "description" in data:
        description = data["description"]

        if not isinstance(description, str):
            return jsonify({"error": "Description must be text"}), 400

        if len(description) > 255:
            return jsonify({
                "error": "Description cannot exceed 255 characters"
            }), 400
    
    try:
        transaction.amount = new_amount
        transaction.type = new_type

        if "category" in data:
            transaction.category = category.strip()

        if "description" in data:
            transaction.description = description.strip()

        db.session.commit()

        return jsonify({
            "message": "Transaction updated successfully!"
        })

    except Exception:
        db.session.rollback()
        return jsonify({"error": "Could not update transaction"}), 500


@login_required
def delete_transaction(transaction_id):
    user_id = session["user_id"]

    transaction = models.Transaction.query.filter_by(
        id=transaction_id,
        user_id=user_id
    ).first_or_404()

    db.session.delete(transaction)
    db.session.commit()

    return jsonify({
        "message": "Transaction deleted successfully!"
    })


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1")
