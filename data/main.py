from utils.loader import load_transactions
from services.analytics import recalculate
from services.goals import goal_progress
from services.alerts import balance_alerts


# Load data
df = load_transactions()
print("🔹 Original Transactions:")
print(df)

# Remove a transaction (simulate user action)
df = df.drop(index=1).reset_index(drop=True)
print("\n❌ Transaction at index 1 removed")

# Recalculate analytics
daily_spending, monthly_avg = recalculate(df)

print("\n📅 Daily Spending:")
print(daily_spending)

print("\n📊 Monthly Average Spending:")
print(monthly_avg)

# Current balance
current_balance = df.iloc[-1]["balance"]
print(f"\n💰 Current Balance: ₹{current_balance}")

# Alerts
thresholds = [10000, 5000, 2000]
alerts = balance_alerts(current_balance, thresholds)

print("\n🔔 Alerts:")
if alerts:
    for a in alerts:
        print(a)
else:
    print("✅ Balance is healthy")

# Savings goal
goal = goal_progress(current_balance, 80000)

print("\n🎯 Savings Goal:")
print(f"Progress : {goal['progress_percent']}%")
print(f"Remaining: ₹{goal['remaining']}")
