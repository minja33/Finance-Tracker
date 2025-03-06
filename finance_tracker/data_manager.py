# finance_tracker/data_manager.py
import json
import os

class DataManager:
    def __init__(self, data_file="finance_data.json"):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """Load data from JSON file or initialize new structure."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {
            "transactions": [],
            "categories": ["income", "food", "rent", "entertainment", "other"]
        }

    def save_data(self):
        """Save data to JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def get_data(self):
        """Return current data."""
        return self.data

    def update_data(self, new_data):
        """Update data and save."""
        self.data = new_data
        self.save_data()