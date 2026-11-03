const API_URL = "http://127.0.0.1:5000";

function showNotification(status, message) {
    window.location.href =
        `notification.html?type=result&status=${encodeURIComponent(status)}&message=${encodeURIComponent(message)}`;
}

let transactions = [];

let monthlyBudget = Number(localStorage.getItem("monthlyBudget")) || 0;

let totalIncome = 0;

let totalExpenses = 0

const balanceElement = document.getElementById("balance");
const incomeElement = document.getElementById("income");
const expensesElement = document.getElementById("expenses");
const filterCategory = document.getElementById("filter-category");
const searchInput = document.getElementById("search-transaction");

const expenseForm = document.getElementById("expense-form");
const incomeForm = document.getElementById("income-form");
const incomeAmountInput = document.getElementById("income-amount");
const incomeCategoryInput = document.getElementById("income-category");
const amountInput = document.getElementById("amount");
const categoryInput = document.getElementById("category");

const transactionList = document.getElementById("transaction-list");
const budgetInput = document.getElementById("budget-limit");
const setBudgetButton = document.getElementById("set-budget");
const loadingMessage = document.getElementById("loadingMessage");
const monthlyLimitElement = document.getElementById("monthly-limit");
const monthlySpentElement = document.getElementById("monthly-spent");
const remainingBudgetElement = document.getElementById("remaining-budget");
const budgetMessage = document.getElementById("budget-message");


async function fetchTransactions() {
    try {
        const response = await fetch(`${API_URL}/transactions`);

        if (!response.ok) {
            throw new Error("Failed to fetch transactions");
        }

        const transactions = await response.json();

        console.log("Transactions:", transactions);

        return transactions;

    } catch (error) {
        console.error("Error fetching transactions:", error);
        throw error;
    }
}


async function loadTransactions() {
    loadingMessage.textContent = "Loading transactions...";

    try {
        const databaseTransactions = await fetchTransactions();

        transactions = databaseTransactions;

        totalIncome = transactions
            .filter(item => item.type === "income")
            .reduce((total, item) => total + Number(item.amount), 0);

        totalExpenses = transactions
            .filter(item => item.type === "expense")
            .reduce((total, item) => total + Number(item.amount), 0);

        renderTransactions();

        updateDashboard();
        updateChart();
        updateIncomeChart();
        updateBudget();

        loadingMessage.textContent = "";

    } catch (error) {
        console.error("Error loading transactions:", error);

        loadingMessage.textContent =
            "Unable to load transactions. Please check your backend connection and refresh.";
    }
}

//                 Updates the dashboard income, expenses, and available balance.

function updateDashboard() {
    incomeElement.textContent = `₹${totalIncome.toFixed(2)}`;
    expensesElement.textContent = `₹${totalExpenses.toFixed(2)}`;

    const balance = totalIncome - totalExpenses;
    balanceElement.textContent = `₹${balance.toFixed(2)}`;
}

//                Handles adding new expenses and deleting existing expenses.

expenseForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const amount = Number(amountInput.value);
    const category = categoryInput.value;
    const date = new Date().toLocaleDateString("en-IN");

    // Validates the expense amount.

    if (!Number.isFinite(amount) || amount <= 0) {
        showNotification("error", "Please enter a valid amount.");
        return;
    }

    // Calculates the total expenses for the current month.

    const monthlyExpenses = getMonthlyExpenses();

    // Prevents adding an expense that exceeds the monthly budget.

    if (monthlyBudget > 0 && monthlyExpenses + amount > monthlyBudget) {
        showNotification("warning", "Monthly budget limit exceeded! Increase your budget to add this expense.");
        return;
    }

    totalExpenses += amount;

    const newTransaction = {
        amount: amount,
        category: category,
        type: "expense",
        date: date
    };

    try {
        const response = await fetch(`${API_URL}/transactions`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                amount: amount,
                category: category,
                type: "expense"
            })
        });

        if (!response.ok) {
            throw new Error("Failed to save expense");
        }

        const result = await response.json();
        newTransaction.id = result.id;

    } catch (error) {
        console.error("Error saving expense:", error);
        showNotification("error", "Expense could not be saved to database.");
        return;
    }

    transactions.push(newTransaction);

    const editButton = document.createElement("button");
    editButton.textContent = "update";
    editButton.className = "edit-button";

    editButton.addEventListener("click", function () {
        window.location.href =
            `edit-transactions.html?id=${newTransaction.id}`;
    });

    const transaction = document.createElement("div");
    transaction.className = "transaction-item";

    const details = document.createElement("span");
    details.textContent =
        `${category}: ₹${amount.toFixed(2)} (Expense) | ${date}`;

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.className = "delete-button";

    // Deletes this specific expense and updates the dashboard.


    deleteButton.addEventListener("click", function () {
        window.location.href =
            `notification.html?type=confirm&action=delete&id=${newTransaction.id}`;
    });



    transaction.appendChild(details);
    transaction.appendChild(editButton);
    transaction.appendChild(deleteButton);
    transactionList.appendChild(transaction);

    updateDashboard();
    updateChart();
    updateIncomeChart();
    updateBudget();

    expenseForm.reset();
});


//                          Displays saved transactions and allows users to delete them.

function renderTransactions() {
    transactionList.innerHTML = "";

    transactions.forEach(function (item) {
        const editButton = document.createElement("button");
        editButton.textContent = "Update ";
        editButton.className = "edit-button";

        editButton.addEventListener("click", function () {
            window.location.href =
                `edit-transactions.html?id=${item.id}`;
        });

        const transaction = document.createElement("div");
        transaction.className = "transaction-item";

        const details = document.createElement("span");
        details.textContent =
            `${item.category}: ₹${item.amount.toFixed(2)} (${item.type === "income" ? "Income" : "Expense"}) | ${item.date || "Old transaction"}`;

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.className = "delete-button";

        // Deletes a saved transaction and refreshes all related data.

        deleteButton.addEventListener("click", function () {
            window.location.href =
                `notification.html?type=confirm&action=delete&id=${item.id}`;
        });

        transaction.appendChild(details);
        transaction.appendChild(editButton);
        transaction.appendChild(deleteButton);
        transactionList.appendChild(transaction);
    });
}

//                    Handles adding new income and deleting existing income.
incomeForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const amount = Number(incomeAmountInput.value);
    const category = incomeCategoryInput.value.trim();

    if (!Number.isFinite(amount) || amount <= 0) {
        showNotification("error", "Please enter a valid income amount.");
        return;
    }

    if (category === "") {
        showNotification("error", "Please enter a valid category.");
        return;
    }

    try {
        const response = await fetch(`${API_URL}/transactions`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                amount: amount,
                category: category,
                type: "income"
            })
        });

        if (!response.ok) {
            throw new Error("Failed to save income");
        }

        await loadTransactions();

        incomeForm.reset();

        showNotification("success", "Income added successfully!");

    } catch (error) {
        console.error("Income save error:", error);
        showNotification("error", "Income could not be saved to database.");
    }
});

//                      Filters transactions by search text and selected category.

function filterTransactions() {
    const searchText = searchInput.value.toLowerCase().trim();
    const selectedCategory = filterCategory.value;
    const allTransactions = document.querySelectorAll(".transaction-item");

    allTransactions.forEach(function (transaction) {
        const details = transaction.querySelector("span").textContent.toLowerCase();

        const matchesSearch = details.includes(searchText);
        const matchesCategory =
            selectedCategory === "All" ||
            details.startsWith(selectedCategory.toLowerCase() + ":");

        transaction.style.display =
            matchesSearch && matchesCategory ? "flex" : "none";
    });
}

//                       Runs the filter whenever the user searches or changes category.

searchInput.addEventListener("input", filterTransactions);
filterCategory.addEventListener("change", filterTransactions);

//  Stores the expense chart instance.
let expenseChart;

//                      Creates or updates the expense chart by category.

function updateChart() {
    const chartCanvas = document.getElementById("expense-chart");

    if (!chartCanvas || typeof Chart === "undefined") {
        return;
    }

    const categories = ["Food", "Travel", "Shopping", "Bills", "Other"];

    const categoryTotals = categories.map(function (category) {
        return transactions
            .filter(function (item) {
                return item.type === "expense" &&
                    item.category === category;
            })
            .reduce(function (total, item) {
                return total + Number(item.amount);
            }, 0);
    });

    if (expenseChart) {
        expenseChart.data.datasets[0].data = categoryTotals;
        expenseChart.update();
        return;
    }

    expenseChart = new Chart(chartCanvas, {
        type: "bar",
        data: {
            labels: categories,
            datasets: [{
                label: "Expenses by Category (₹)",
                data: categoryTotals,
                backgroundColor: [
                    "#fb923c",
                    "#f97316",
                    "#fdba74",
                    "#ea580c",
                    "#fb923c"
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Stores the income chart instance.
let incomeChart;

//                    Creates or updates the income chart by category.

function updateIncomeChart() {
    const chartCanvas = document.getElementById("income-chart");

    if (!chartCanvas || typeof Chart === "undefined") {
        return;
    }

    const categories = [
        "Salary",
        "Pocket Money",
        "Gift",
        "Other Income"
    ];

    const categoryTotals = categories.map(function (category) {
        return transactions
            .filter(function (item) {
                return item.type === "income" &&
                    item.category === category;
            })
            .reduce(function (total, item) {
                return total + Number(item.amount);
            }, 0);
    });

    if (incomeChart) {
        incomeChart.data.datasets[0].data = categoryTotals;
        incomeChart.update();
        return;
    }

    incomeChart = new Chart(chartCanvas, {
        type: "bar",
        data: {
            labels: categories,
            datasets: [{
                label: "Income by Category (₹)",
                data: categoryTotals,
                backgroundColor: [
                    "#60a5fa",
                    "#3b82f6",
                    "#93c5fd",
                    "#2563eb"
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

//                 Saves the monthly budget entered by the user.

setBudgetButton.addEventListener("click", function () {
    const budget = Number(budgetInput.value);

    if (!Number.isFinite(budget) || budget <= 0) {
        showNotification("error", "Please enter a valid budget amount.");
        return;
    }

    monthlyBudget = budget;

    localStorage.setItem("monthlyBudget", monthlyBudget);

    updateBudget();
    budgetInput.value = "";
});

// Calculates monthly expenses and updates the budget details.
function updateBudget() {
    const monthlyExpenses = getMonthlyExpenses();

    const remaining = monthlyBudget - monthlyExpenses;

    monthlyLimitElement.textContent = `₹${monthlyBudget.toFixed(2)}`;
    monthlySpentElement.textContent = `₹${monthlyExpenses.toFixed(2)}`;
    remainingBudgetElement.textContent = `₹${remaining.toFixed(2)}`;

    // Displays a message based on the remaining budget.
    if (remaining < 0) {
        budgetMessage.textContent = "⚠️ Monthly budget exceeded!";
        budgetMessage.style.color = "red";
    } else {
        budgetMessage.textContent = "Budget is within limit.";
        budgetMessage.style.color = "green";
    }
}

//         Calculates the total expenses for the current month.

function getMonthlyExpenses() {
    const currentMonth = new Date().getMonth();
    const currentYear = new Date().getFullYear();

    return transactions
        .filter(function (item) {
            if (!item.date || item.type !== "expense") {
                return false;
            }

            const transactionDate = new Date(item.date);

            return !isNaN(transactionDate.getTime()) &&
                transactionDate.getMonth() === currentMonth &&
                transactionDate.getFullYear() === currentYear;
        })
        .reduce(function (total, item) {
            return total + Number(item.amount);
        }, 0);
}

loadTransactions();