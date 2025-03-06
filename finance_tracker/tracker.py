# finance_tracker/tracker.py
from datetime import datetime
from .data_manager import DataManager

class FinanceTracker:
    def __init__(self):
        self.data_manager = DataManager()

    def add_transaction(self, amount, category, description, is_income=False):
        """Add a new transaction."""
        data = self.data_manager.get_data()
        if category not in data["categories"]:
            data["categories"].append(category)
        
        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": float(amount),
            "category": category,
            "description": description,
            "type": "income" if is_income else "expense"
        }
        data["transactions"].append(transaction)
        self.data_manager.update_data(data)
        return f"Added {transaction['type']}: ${amount} - {description}"

    def get_balance(self):
        """Calculate current balance."""
        data = self.data_manager.get_data()
        income = sum(t["amount"] for t in data["transactions"] if t["type"] == "income")
        expenses = sum(t["amount"] for t in data["transactions"] if t["type"] == "expense")
        return income - expenses

    def get_summary(self):
        """Generate financial summary."""
        data = self.data_manager.get_data()
        balance = self.get_balance()
        summary = f"Current Balance: ${balance:.2f}\n\nCategory Breakdown:\n"
        
        categories = {}
        for t in data["transactions"]:
            cat = t["category"]
            categories[cat] = categories.get(cat, 0) + (t["amount"] if t["type"] == "income" else -t["amount"])
        
        for cat, amount in categories.items():
            summary += f"{cat}: ${amount:.2f}\n"
        return summary