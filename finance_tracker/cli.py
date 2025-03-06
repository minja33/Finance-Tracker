# finance_tracker/cli.py
from .tracker import FinanceTracker

class FinanceCLI:
    def __init__(self):
        self.tracker = FinanceTracker()

    def run(self):
        """Run the CLI loop."""
        while True:
            print("\n1. Add Income\n2. Add Expense\n3. Show Summary\n4. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                self._add_transaction(True)
            elif choice == "2":
                self._add_transaction(False)
            elif choice == "3":
                print(self.tracker.get_summary())
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid option, try again.")

    def _add_transaction(self, is_income):
        """Helper method to add a transaction."""
        try:
            amount = float(input("Amount: "))
            category = input("Category: ")
            desc = input("Description: ")
            print(self.tracker.add_transaction(amount, category, desc, is_income))
        except ValueError:
            print("Invalid amount. Please enter a number.")