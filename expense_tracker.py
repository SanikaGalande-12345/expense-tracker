import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

FILENAME = "expenses.csv"


# ------------------------------------------------
# 1. Create file if it does not exist
# ------------------------------------------------
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])


# ------------------------------------------------
# 2. Add Expense
# ------------------------------------------------
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food/Travel/Shopping/etc): ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount! Please enter numbers only.\n")
        return

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("✅ Expense added successfully!\n")


# ------------------------------------------------
# 3. View Expenses
# ------------------------------------------------
def view_expenses():
    print("\n----- All Expenses -----")
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()


# ------------------------------------------------
# 4. Show Total Expense
# ------------------------------------------------
def show_total():
    total = 0
    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])

    print(f"\n💰 Total Expense: ₹{total}\n")


# ------------------------------------------------
# 5. Show Category-wise Chart
# ------------------------------------------------
def show_chart():
    category_data = {}

    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in category_data:
                category_data[category] += amount
            else:
                category_data[category] = amount

    if not category_data:
        print("No data available!")
        return

    # Plot Bar Chart
    plt.figure()
    plt.bar(category_data.keys(), category_data.values())
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.title("Expense Distribution by Category")
    plt.xticks(rotation=45)
    plt.show()


# ------------------------------------------------
# 6. Main Menu
# ------------------------------------------------
def main():
    initialize_file()

    while True:
        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Show Chart")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            show_chart()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()
