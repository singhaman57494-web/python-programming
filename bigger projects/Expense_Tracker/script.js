

function saveData() {
    localStorage.setItem("totalIncome", totalIncome);
    localStorage.setItem("totalExpenses", totalExpenses);
    localStorage.setItem("transactions", JSON.stringify(transactions));
}

let transactions = JSON.parse(
    localStorage.getItem("transactions") || "[]"
);

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


function updateDashboard() {
    incomeElement.textContent = `₹${totalIncome.toFixed(2)}`;
    expensesElement.textContent = `₹${totalExpenses.toFixed(2)}`;

    const balance = totalIncome - totalExpenses;
    balanceElement.textContent = `₹${balance.toFixed(2)}`;

    // updateChart();
    // updateIncomeChart();
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

    transactions.push({
        amount: amount,
        category: category,
        type: "expense",
        date: new Date().toLocaleDateString("en-IN")
    });


    const transaction = document.createElement("div");
    transaction.className = "transaction-item";

    const details = document.createElement("span");
    details.textContent =
        `${category}: ₹${amount.toFixed(2)} (Expense) | ${new Date().toLocaleDateString("en-IN")}`;

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.className = "delete-button";

    deleteButton.addEventListener("click", function () {
        totalExpenses -= amount;
        transactions.splice(
            transactions.findIndex(
                item => item.amount === amount && item.category === category
            ),
            1
        );
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
    expenseForm.reset();
});

updateDashboard();

transactions.forEach(function (item) {
    const transaction = document.createElement("div");
    transaction.className = "transaction-item";

    const details = document.createElement("span");
    details.textContent =
        `${item.category}: ₹${item.amount.toFixed(2)} (${item.type === "income" ? "Income" : "Expense"}) | ${item.date || "Old transaction"}`;

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.className = "delete-button";

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
        }
    });

    transaction.appendChild(details);
    transaction.appendChild(deleteButton);
    transactionList.appendChild(transaction);
});

incomeForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const amount = Number(incomeAmountInput.value);
    const category = incomeCategoryInput.value;

    if (!Number.isFinite(amount) || amount <= 0) {
        alert("Please enter a valid income amount.");
        return;
    }

    totalIncome += amount;
    transactions.push({
        amount: amount,
        category: category,
        type: "income",
        date: new Date().toLocaleDateString("en-IN")
    });
    const transaction = document.createElement("div");
    transaction.className = "transaction-item";

    const details = document.createElement("span");
    details.textContent =
        `${category}: ₹${amount.toFixed(2)} (Income) | ${new Date().toLocaleDateString("en-IN")}`;

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.className = "delete-button";
    deleteButton.addEventListener("click", function () {
        totalIncome -= amount;

        transactions = transactions.filter(function (item) {
            return !(item.amount === amount &&
                item.category === category &&
                item.type === "income");
        });

        transaction.remove();
        updateDashboard();
        saveData();
    });

    transaction.appendChild(details);
    transaction.appendChild(deleteButton);
    transactionList.appendChild(transaction);

    updateDashboard();
    saveData();
    incomeForm.reset();
});


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

searchInput.addEventListener("input", filterTransactions);
filterCategory.addEventListener("change", filterTransactions);

let expenseChart;

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


let incomeChart;

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

updateChart();
updateIncomeChart();