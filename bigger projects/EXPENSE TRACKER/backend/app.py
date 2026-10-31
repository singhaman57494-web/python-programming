from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from sqlalchemy import text

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

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
        return jsonify({"database": "Connected successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)