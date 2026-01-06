# reports.py
import matplotlib.pyplot as plt


def expense_summary(tracker):
    summary = {}
    for e in tracker.expenses:
        summary[e.category] = summary.get(e.category, 0) + e.amount
    return summary


def plot_expense_pie(tracker):
    summary = expense_summary(tracker)
    plt.pie(summary.values(), labels=summary.keys(), autopct="%1.1f%%")
    plt.title("Expenses by Category")
    plt.show()
