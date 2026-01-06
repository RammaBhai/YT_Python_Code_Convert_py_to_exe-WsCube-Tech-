# main.py
from models import Tracker, Expense, Income
from storage import save_data, load_data
from reports import plot_expense_pie
from datetime import datetime


def get_float(prompt: str) -> float:
    """Safely get a float value from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")


def get_date(prompt: str) -> str:
    """Validate date input"""
    while True:
        date_str = input(prompt)
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("❌ Date must be in YYYY-MM-DD format.")


def show_menu():
    print(
        "\n📊 Expense Tracker Menu"
        "\n1️⃣  Add Expense"
        "\n2️⃣  Add Income"
        "\n3️⃣  Show Balance"
        "\n4️⃣  Show Expense Chart"
        "\n5️⃣  Save & Exit"
    )


def main():
    tracker = Tracker()
    load_data(tracker)
    print("✅ Data loaded successfully!")

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            amt = get_float("Amount: ")
            cat = input("Category: ").strip()
            date = get_date("Date (YYYY-MM-DD): ")
            tracker.add_expense(Expense(amt, cat, date))
            print("✅ Expense added.")

        elif choice == "2":
            amt = get_float("Amount: ")
            cat = input("Source: ").strip()
            date = get_date("Date (YYYY-MM-DD): ")
            tracker.add_income(Income(amt, cat, date))
            print("✅ Income added.")

        elif choice == "3":
            balance = tracker.total_balance()
            print(f"💰 Current Balance: {balance:.2f}")

        elif choice == "4":
            if not tracker.expenses:
                print("⚠️ No expenses to plot.")
            else:
                plot_expense_pie(tracker)

        elif choice == "5":
            save_data(tracker)
            print("💾 Data saved. Goodbye!")
            break

        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    main()
