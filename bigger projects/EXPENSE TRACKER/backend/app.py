import os
from flask import Flask, jsonify, request
from config import Config
from sqlalchemy import text
from extensions import db
import models
import math
from flask_cors import CORS  # type: ignore[reportMissingModuleSource]

app = Flask(__name__)
CORS(
    app,
    resources={
        r"/transactions*": {
            "origins": os.getenv(
                "FRONTEND_ORIGIN",
                "http://127.0.0.1:5500"
            )
        }
    }
)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


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
            "error": "Invalid category for this transaction type"
        }), 400

    description = data.get("description", "")

    if not isinstance(description, str):
        return jsonify({"error": "Description must be text"}), 400

    if len(description) > 255:
        return jsonify({
            "error": "Description cannot exceed 255 characters"
        }), 400

    if transaction_type == "expense":
        total_income = db.session.query(
            db.func.coalesce(db.func.sum(models.Transaction.amount), 0)
        ).filter_by(type="income").scalar()

        total_expenses = db.session.query(
            db.func.coalesce(db.func.sum(models.Transaction.amount), 0)
        ).filter_by(type="expense").scalar()

        available_balance = float(total_income) - float(total_expenses)

        if amount > available_balance:
            return jsonify({
                "error": "Insufficient balance. Add income before recording this expense."
            }), 400

    try:
        new_transaction = models.Transaction(
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
        return jsonify({"error": "Could not save transaction"}), 500

@app.route("/transactions", methods=["GET"])
def get_transactions():
    transactions = models.Transaction.query.order_by(
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
def update_transaction(transaction_id):
    transaction = models.Transaction.query.get_or_404(transaction_id)

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

    if new_amount != transaction.amount or new_type != transaction.type:
        total_income = db.session.query(
            db.func.coalesce(db.func.sum(models.Transaction.amount), 0)
        ).filter(
            models.Transaction.type == "income",
            models.Transaction.id != transaction.id
        ).scalar()

        total_expenses = db.session.query(
            db.func.coalesce(db.func.sum(models.Transaction.amount), 0)
        ).filter(
            models.Transaction.type == "expense",
            models.Transaction.id != transaction.id
        ).scalar()

        base_balance = float(total_income) - float(total_expenses)

        current_balance = base_balance
        if transaction.type == "income":
            current_balance += transaction.amount
        else:
            current_balance -= transaction.amount

        new_balance = base_balance
        if new_type == "income":
            new_balance += new_amount
        else:
            new_balance -= new_amount

        # Allow corrections that improve an existing negative balance,
        # but reject changes that make the balance more negative.
        if new_balance < 0 and new_balance < current_balance:
            return jsonify({
                "error": "Insufficient balance. This change would make your balance more negative."
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



@app.route("/transactions/<int:transaction_id>", methods=["DELETE"])
def delete_transaction(transaction_id):
    transaction = models.Transaction.query.get_or_404(transaction_id)

    if transaction.type == "income":
        total_income = db.session.query(
            db.func.coalesce(db.func.sum(models.Transaction.amount), 0)
        ).filter(
            models.Transaction.type == "income",
            models.Transaction.id != transaction.id
        ).scalar()

        total_expenses = db.session.query(
            db.func.coalesce(db.func.sum(models.Transaction.amount), 0)
        ).filter_by(type="expense").scalar()

        new_balance = float(total_income) - float(total_expenses)

        if new_balance < 0:
            return jsonify({
                "error": "Cannot delete this income because it would make your balance negative."
            }), 400

    db.session.delete(transaction)
    db.session.commit()

    return jsonify({
        "message": "Transaction deleted successfully!"
    })


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1")
