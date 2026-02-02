💰 Expense Management Application

A backend-focused expense management system built with Python, designed to analyze UPI transaction data, track spending patterns, generate real-time alerts, and help users plan savings goals.
This project is structured to be scalable, API-ready, and suitable for integration with a Flutter frontend.

🚀 Features

📄 UPI Transaction Parsing

Reads and processes transaction data from CSV files

Supports debit and credit transactions with balance tracking

📊 Expense Analytics

Daily spending calculation

Monthly average expense analysis

Automatic recalculation after transaction updates

❌ Transaction Exclusion

Allows removing specific transactions

All analytics update instantly after removal

🔔 Low Balance Alerts

Supports multiple user-defined balance thresholds

Generates warnings when balance falls below set limits

🎯 Savings Goal Tracking

Set a target amount for future purchases

Tracks progress percentage and remaining amount

Uses real transaction history and current balance

🧱 Clean Backend Architecture

Modular file structure

Separation of concerns (analytics, alerts, goals, utilities)

Easy to extend with database or API layer

🛠 Tech Stack

Language: Python

Libraries: pandas

Version Control: Git & GitHub

Editor: VS Code

📂 Project Structure
expense_app_backend/
│
├── data/
│   └── transactions.csv
│
├── services/
│   ├── analytics.py     # Expense calculations
│   ├── alerts.py       # Low balance alerts
│   └── goals.py        # Savings goal logic
│
├── utils/
│   └── loader.py       # Transaction loader
│
├── main.py             # Application entry point
└── README.md

▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/satyamsinghbt25mech-ship-it/expense-management-app.git
cd expense-management-app

2️⃣ Install dependencies
pip install pandas

3️⃣ Run the application
python main.py

📈 Sample Output

Daily spending summary

Monthly average expenses

Balance alerts (if triggered)

Savings goal progress (% and remaining amount)

🧠 Learning Outcomes

This project demonstrates:

Real-world data processing with Python

Financial analytics logic used in expense-tracking apps

Clean backend design principles

Practical use of Git and GitHub for project management

🔮 Future Enhancements

🔌 Convert backend to FastAPI for frontend integration

🗄 Replace CSV with SQLite / PostgreSQL

📱 Build a Flutter mobile UI

🔐 Add user authentication

☁️ Cloud deployment

👤 Author

Satyam Singh
GitHub: https://github.com/satyamsinghbt25mech-ship-it

⭐ If you find this project useful

Give it a ⭐ on GitHub — it really helps!