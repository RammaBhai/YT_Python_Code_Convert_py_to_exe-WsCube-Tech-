# models.py
from datetime import datetime


class Transaction:
    def __init__(self, amount: float, category: str, date: str):
        self.amount = amount
        self.category = category
        self.date = datetime.strptime(date, "%Y-%m-%d")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date.strftime("%Y-%m-%d"),
        }


class Expense(Transaction):
    pass


class Income(Transaction):
    pass


class Tracker:
    def __init__(self):
        self.expenses = []
        self.incomes = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def add_income(self, income: Income):
        self.incomes.append(income)

    def total_balance(self):
        total_income = sum(i.amount for i in self.incomes)
        total_expense = sum(e.amount for e in self.expenses)
        return total_income - total_expense
