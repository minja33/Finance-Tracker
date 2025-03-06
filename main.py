# main.py
from finance_tracker.cli import FinanceCLI

def main():
    cli = FinanceCLI()
    cli.run()

if __name__ == "__main__":
    main()