

let transactions = JSON.parse(
    localStorage.getItem("transactions") || "[]"
);
let monthlyBudget = Number(localStorage.getItem("monthlyBudget")) || 0;

let totalIncome = Number(
    localStorage.getItem("totalIncome") ?? 8000
);

let totalExpenses = Number(
    localStorage.getItem("totalExpenses") ?? 2500
);

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

const transactionList = document.querySelector(".transactions");
const budgetInput = document.getElementById("budget-limit");
const setBudgetButton = document.getElementById("set-budget");
const monthlyLimitElement = document.getElementById("monthly-limit");
const monthlySpentElement = document.getElementById("monthly-spent");
const remainingBudgetElement = document.getElementById("remaining-budget");
const budgetMessage = document.getElementById("budget-message");

//                 Saves income, expenses, and transactions in local storage.

function saveData() {
    localStorage.setItem("totalIncome", totalIncome);
    localStorage.setItem("totalExpenses", totalExpenses);
    localStorage.setItem("transactions", JSON.stringify(transactions));
}

//                 Updates the dashboard income, expenses, and available balance.

function updateDashboard() {
    incomeElement.textContent = `₹${totalIncome.toFixed(2)}`;
    expensesElement.textContent = `₹${totalExpenses.toFixed(2)}`;

    const balance = totalIncome - totalExpenses;
    balanceElement.textContent = `₹${balance.toFixed(2)}`;
}

//                Handles adding new expenses and deleting existing expenses.

expenseForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const amount = Number(amountInput.value);
    const category = categoryInput.value;
    const date = new Date().toLocaleDateString("en-IN");

    // Validates the expense amount.

    if (!Number.isFinite(amount) || amount <= 0) {
        alert("Please enter a valid amount.");
        return;
    }

    // Calculates the total expenses for the current month.

    const monthlyExpenses = getMonthlyExpenses();

    // Prevents adding an expense that exceeds the monthly budget.

    if (monthlyBudget > 0 && monthlyExpenses + amount > monthlyBudget) {
        alert("Monthly budget limit exceeded! Increase your budget to add this expense.");
        return;
    }

    totalExpenses += amount;

    const newTransaction = {
        amount: amount,
        category: category,
        type: "expense",
        date: date
    };

    transactions.push(newTransaction);

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
        totalExpenses -= amount;

        const index = transactions.indexOf(newTransaction);

        if (index !== -1) {
            transactions.splice(index, 1);
        }

        transaction.remove();

        updateDashboard();
        saveData();
        updateChart();
        updateIncomeChart();
        updateBudget();
    });

    transaction.appendChild(details);
    transaction.appendChild(deleteButton);
    transactionList.appendChild(transaction);

    updateDashboard();
    saveData();
    updateChart();
    updateIncomeChart();
    updateBudget();

    expenseForm.reset();
});


//                          Displays saved transactions and allows users to delete them.

transactions.forEach(function (item) {
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
        const index = transactions.indexOf(item);

        if (index !== -1) {
            transactions.splice(index, 1);

            if (item.type === "income") {
                totalIncome -= item.amount;
            } else {
                totalExpenses -= item.amount;
            }

            transaction.remove();

            updateDashboard();
            saveData();
            updateChart();
            updateIncomeChart();
            updateBudget();
        }
    });

    transaction.appendChild(details);
    transaction.appendChild(deleteButton);
    transactionList.appendChild(transaction);
});

//                    Handles adding new income and deleting existing income.

incomeForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const amount = Number(incomeAmountInput.value);
    const category = incomeCategoryInput.value;
    const date = new Date().toLocaleDateString("en-IN");

    // Validates the income amount.

    if (!Number.isFinite(amount) || amount <= 0) {
        alert("Please enter a valid income amount.");
        return;
    }

    totalIncome += amount;

    const newTransaction = {
        amount: amount,
        category: category,
        type: "income",
        date: date
    };

    transactions.push(newTransaction);

    const transaction = document.createElement("div");
    transaction.className = "transaction-item";

    const details = document.createElement("span");
    details.textContent =
        `${category}: ₹${amount.toFixed(2)} (Income) | ${date}`;

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.className = "delete-button";

    // Deletes this specific income and updates the dashboard.

    deleteButton.addEventListener("click", function () {
        totalIncome -= amount;

        const index = transactions.indexOf(newTransaction);

        if (index !== -1) {
            transactions.splice(index, 1);
        }

        transaction.remove();

        updateDashboard();
        saveData();
        updateChart();
        updateIncomeChart();
    });

    transaction.appendChild(details);
    transaction.appendChild(deleteButton);
    transactionList.appendChild(transaction);

    updateDashboard();
    saveData();
    updateChart();
    updateIncomeChart();

    incomeForm.reset();
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
        alert("Please enter a valid budget amount.");
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
            if (!item.date) {
                return false;
            }

            const parts = item.date.split("/");
            const transactionDate = new Date(
                parts[2],
                parts[1] - 1,
                parts[0]
            );

            return item.type === "expense" &&
                transactionDate.getMonth() === currentMonth &&
                transactionDate.getFullYear() === currentYear;
        })
        .reduce(function (total, item) {
            return total + item.amount;
        }, 0);
}

// Initializes the dashboard, charts, and monthly budget when the page loads.
updateDashboard();
updateChart();
updateIncomeChart();
updateBudget();