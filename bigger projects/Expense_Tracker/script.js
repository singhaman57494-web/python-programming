

function saveData() {
    localStorage.setItem("totalIncome", totalIncome);
    localStorage.setItem("totalExpenses", totalExpenses);
}

let totalIncome = Number(
    localStorage.getItem("totalIncome") ?? 8000
);

let totalExpenses = Number(
    localStorage.getItem("totalExpenses") ?? 2500
);


const balanceElement = document.getElementById("balance");
const incomeElement = document.getElementById("income");
const expensesElement = document.getElementById("expenses");

const expenseForm = document.getElementById("expense-form");
const amountInput = document.getElementById("amount");
const categoryInput = document.getElementById("category");

const transactionList = document.querySelector(".transactions");

function updateDashboard() {
    incomeElement.textContent = `₹${totalIncome.toFixed(2)}`;
    expensesElement.textContent = `₹${totalExpenses.toFixed(2)}`;

    const balance = totalIncome - totalExpenses;
    balanceElement.textContent = `₹${balance.toFixed(2)}`;
}

expenseForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const amount = Number(amountInput.value);
    const category = categoryInput.value;

    if (!Number.isFinite(amount) || amount <= 0) {
        alert("Please enter a valid amount.");
        return;
    }

    totalExpenses += amount;


    const transaction = document.createElement("div");
    transaction.className = "transaction-item";

    const details = document.createElement("span");
    details.textContent = `${category}: ₹${amount.toFixed(2)}`;

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.className = "delete-button";

    deleteButton.addEventListener("click", function () {
        totalExpenses -= amount;
        transaction.remove();
        updateDashboard();
        saveData();
    });

    transaction.appendChild(details);
    transaction.appendChild(deleteButton);
    transactionList.appendChild(transaction);


    updateDashboard();
    saveData();
    expenseForm.reset();
});

updateDashboard();
