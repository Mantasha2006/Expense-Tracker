import json
try:
    with open("expense.json", "r") as f:
        expense_data= json.load(f)

except FileNotFoundError:

    expense_data = {}

while True:
    print("-------Expense Tracker--------")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Calcuate Total Expense")
    print("6. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        expense_id = input("Enter expenseID:")

        if expense_id in expense_data:
            print("ExpenseID already exist..")

        else:
            Expense_name= input("Enter expense name:")
            Expense_amount=int( input("Enter expense amount:"))
            Category= input("Enter category:")
            Date= input("Enter date:")

            expense_data[expense_id]={
                "Expense_name": Expense_name,
                "Expense_amount": Expense_amount,
                "Category": Category,
                "Date": Date
            }

            with open("expense.json", "w") as f:
                json.dump(expense_data, f, indent=4)

            print("Expense added successfully!!")

    elif choice=="2":
        if not expense_data:
            print("No expenses found!")

        else:
            for expense_id , details in expense_data.items():
                print("ExpenseID:", expense_id)
                print("Expense Name:", details['Expense_name'])
                print("Amount:", details['Expense_amount'])
                print("Category:", details['Category'])
                print("Date:", details['Date'])

    elif choice=="3":
        expense_id= input("Enter expenseID to search:")

        if expense_id in expense_data:
            details= expense_data[expense_id]

            print("Expense Name:", details['Expense_name'])
            print("Amount:", details['Expense_amount'])
            print("Category:", details['Category'])
            print("Date:", details['Date'])
            

        else:
            print("Expense ID not found")

    elif choice=="4":
        expense_id=input("Enter expense id of the expense data you want to delete:")

        if expense_id in expense_data:
            del expense_data[expense_id]

            with open("expense.json", "w") as f:
                json.dump(expense_data, f, indent=4)
                
            print("Expense data deleted successfully!")

        else:
            print("ExpenseID not found..")

    elif choice=="5":
        Total = 0
        for details in expense_data.values():
            Total += details['Expense_amount']

        print("\nTotal Amount", Total)

    elif choice=="6":
        print("Thank you for using expense tracker......")

        break
    else:
        print("Invalid choice")
                
                
                
