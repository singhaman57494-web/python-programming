
const API_URL =
    window.location.hostname === "localhost" ||
        window.location.hostname === "127.0.0.1"
        ? "http://127.0.0.1:5000"
        : "https://python-programming-1-8ew8.onrender.com";

const calendarGrid = document.getElementById("calendarGrid");
const currentMonthHeading = document.getElementById("currentMonth");

const monthlyIncomeElement = document.getElementById("monthlyIncome");
const monthlyExpensesElement = document.getElementById("monthlyExpenses");
const monthlyBalanceElement = document.getElementById("monthlyBalance");

const prevMonthButton = document.getElementById("prevMonth");
const nextMonthButton = document.getElementById("nextMonth");

let selectedDate = new Date();
let allTransactions = [];

const currency = new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "INR",
    maximumFractionDigits: 2
});

function formatMoney(amount) {
    return currency.format(Number(amount) || 0);
}

function showError(message) {
    calendarGrid.innerHTML = `
        <p class="history-error">${message}</p>
    `;
}

async function loadTransactions() {
    try {
        const response = await fetch(`${API_URL}/transactions`, {
            method: "GET",
            credentials: "include"
        });

        if (response.status === 401) {
            window.location.href = "login.html";
            return;
        }

        if (!response.ok) {
            throw new Error("Transactions load nahi ho paaye.");
        }

        const data = await response.json();

        if (!Array.isArray(data)) {
            throw new Error("Server se invalid transaction data mila.");
        }

        allTransactions = data;
        renderCalendar();

    } catch (error) {
        console.error(error);
        showError("Transactions load nahi ho paaye. Backend connection check karo.");
    }
}

function getMonthTransactions(year, month) {
    return allTransactions.filter(transaction => {
        if (!transaction.date) return false;

        const date = new Date(transaction.date);

        return (
            date.getFullYear() === year &&
            date.getMonth() === month
        );
    });
}

function renderCalendar() {
    const year = selectedDate.getFullYear();
    const month = selectedDate.getMonth();

    currentMonthHeading.textContent = selectedDate.toLocaleDateString(
        "en-IN",
        {
            month: "long",
            year: "numeric"
        }
    );

    const monthTransactions = getMonthTransactions(year, month);

    let totalIncome = 0;
    let totalExpenses = 0;

    monthTransactions.forEach(transaction => {
        const amount = Number(transaction.amount) || 0;

        if (transaction.type === "income") {
            totalIncome += amount;
        } else if (transaction.type === "expense") {
            totalExpenses += amount;
        }
    });

    monthlyIncomeElement.textContent = formatMoney(totalIncome);
    monthlyExpensesElement.textContent = formatMoney(totalExpenses);
    monthlyBalanceElement.textContent = formatMoney(totalIncome - totalExpenses);

    monthlyBalanceElement.style.color =
        totalIncome - totalExpenses < 0 ? "#dc2626" : "#16a34a";


    calendarGrid.innerHTML = "";

    const daysInMonth = new Date(year, month + 1, 0).getDate();

    const activeDays = new Set(
        monthTransactions.map(transaction =>
            new Date(transaction.date).getDate()
        )
    );

    // Sirf transaction wali dates show hongi
    for (let day = 1; day <= daysInMonth; day++) {

        if (!activeDays.has(day)) {
            continue;
        }

        const dayBox = document.createElement("div");
        dayBox.className = "calendar-day";

        const today = new Date();

        if (
            day === today.getDate() &&
            month === today.getMonth() &&
            year === today.getFullYear()
        ) {
            dayBox.classList.add("today");
        }

        const dayTransactions = monthTransactions.filter(transaction => {
            const transactionDate = new Date(transaction.date);
            return transactionDate.getDate() === day;
        });


        let dailyIncome = 0;
        let dailyExpenses = 0;

        const dayNumber = document.createElement("div");
        dayNumber.className = "day-number";
        dayNumber.textContent = day;

        dayBox.appendChild(dayNumber);

        dayTransactions.forEach(transaction => {
            const amount = Number(transaction.amount) || 0;
            const entry = document.createElement("div");

            entry.className = "day-entry";

            const isIncome = transaction.type === "income";

            if (isIncome) {
                dailyIncome += amount;
                entry.classList.add("day-income");
            } else if (transaction.type === "expense") {
                dailyExpenses += amount;
                entry.classList.add("day-expense");
            }

            const title =
                transaction.description ||
                transaction.category ||
                "Transaction";

            const category = transaction.category || "Other";
            const sign = isIncome ? "+" : "-";

            entry.textContent =
                `${sign}${formatMoney(amount)} · ${category} (${title})`;

            dayBox.appendChild(entry);
        });

        if (dayTransactions.length === 0) {
            const emptyText = document.createElement("div");
            emptyText.className = "day-entry";
            emptyText.textContent = "No transactions";
            emptyText.style.color = "#999";

            dayBox.appendChild(emptyText);
        }

        const dailyTotal = document.createElement("div");
        dailyTotal.className = "day-total";

        dailyTotal.innerHTML = `
            <div class="day-income">
                Income: ${formatMoney(dailyIncome)}
            </div>
            <div class="day-expense">
                Expenses: ${formatMoney(dailyExpenses)}
            </div>
            <div>
                Balance: ${formatMoney(dailyIncome - dailyExpenses)}
            </div>
        `;

        dayBox.appendChild(dailyTotal);
        calendarGrid.appendChild(dayBox);
    }
}

prevMonthButton.addEventListener("click", () => {
    selectedDate.setMonth(selectedDate.getMonth() - 1);
    renderCalendar();
});

nextMonthButton.addEventListener("click", () => {
    selectedDate.setMonth(selectedDate.getMonth() + 1);
    renderCalendar();
});

loadTransactions();
