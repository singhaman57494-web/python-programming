
from flask import Flask, jsonify, request
from config import Config
from sqlalchemy import text
from extensions import db
from flask_cors import CORS
import models

app = Flask(__name__)
CORS(app)

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
        result = db.session.execute(
            text("SELECT current_database()")
        ).scalar()

        return jsonify({"database": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/transactions", methods=["POST"])
def add_transaction():
    data = request.get_json()

    if not data or not all(
        key in data for key in ["amount", "category", "type"]
    ):
        return jsonify({"error": "Missing required fields"}), 400

    new_transaction = models.Transaction(
        amount=data["amount"],
        category=data["category"],
        description=data.get("description", ""),
        type=data["type"]
    )

    db.session.add(new_transaction)
    db.session.commit()

    return jsonify({
        "message": "Transaction added successfully!",
        "id": new_transaction.id
    }), 201


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
    data = request.get_json() or {}

    transaction.amount = data.get("amount", transaction.amount)
    transaction.category = data.get("category", transaction.category)
    transaction.description = data.get(
        "description", transaction.description
    )
    transaction.type = data.get("type", transaction.type)

    db.session.commit()

    return jsonify({
        "message": "Transaction updated successfully!"
    })


@app.route("/transactions/<int:transaction_id>", methods=["DELETE"])
def delete_transaction(transaction_id):
    transaction = models.Transaction.query.get_or_404(transaction_id)

    db.session.delete(transaction)
    db.session.commit()

    return jsonify({
        "message": "Transaction deleted successfully!"
    })


if __name__ == "__main__":
    app.run(debug=True)
