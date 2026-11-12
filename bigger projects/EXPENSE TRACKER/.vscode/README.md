# Expense Tracker 💰

A full-stack Expense Tracker web application built using **Python, Flask, PostgreSQL, HTML, CSS, and JavaScript**.

## ✨ Features

- User Signup and Login
- Secure Password Hashing
- User-specific Transaction Management
- Add, Edit, and Delete Transactions
- Income and Expense Tracking
- Automatic Balance Calculation
- Negative Balance Support
- Monthly Budget Limit
- Monthly Transaction History
- CSV Export for Excel and Google Sheets
- Responsive Design for Mobile and Desktop
- PostgreSQL Database Integration

## 🛠️ Technologies Used

**Frontend:** HTML, CSS, JavaScript

**Backend:** Python, Flask

**Database:** PostgreSQL

**Deployment:** Render

## 📁 Project Structure

```text
EXPENSE TRACKER/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── extensions.py
│   ├── models.py
│   └── requirements.txt
│
├── frantend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   ├── login.html
│   ├── sign.html
│   └── monthly-history.html
│
└── README.md
```

## 🚀 Run Locally

1. Clone the repository.
2. Open the backend folder.
3. Create and activate a Python virtual environment.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Configure your `.env` file with:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
```

6. Start the Flask backend:

```bash
python app.py
```

7. Open `frantend/index.html` using VS Code Live Server.

## 🌐 Live Demo

Frontend: https://python-programming-2.onrender.com

Backend: https://python-programming-1-8ew8.onrender.com

## 🔐 Security

- Passwords are stored as secure hashes.
- Transactions are associated with individual user accounts.
- Login sessions protect transaction routes.
- Environment variables are used for sensitive configuration.

## 👨‍💻 Author

Created as a full-stack Python project.