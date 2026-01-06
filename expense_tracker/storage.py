# storage.py
import json
from models import Expense, Income, Tracker


def save_data(tracker: Tracker, filename="data.json"):
    data = {
        "expenses": [e.to_dict() for e in tracker.expenses],
        "incomes": [i.to_dict() for i in tracker.incomes],
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def load_data(tracker: Tracker, filename="data.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            for e in data.get("expenses", []):
                tracker.add_expense(Expense(**e))
            for i in data.get("incomes", []):
                tracker.add_income(Income(**i))
    except FileNotFoundError:
        pass
