# ATM Simulator

balance = 1000.00 # Starting balance
pin = "1234"

print("Welcome to Python Bank ATM")
user_pin = input("Enter your PIN: ")

if user_pin != pin:
    print("Invalid PIN. Access denied.")
else:
    print("PIN accepted. Access granted.")
    
    while True:
        print("\n" + "="*30)
        print("ATM MENU")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("="*30)
        
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            print(f"Your current balance is: ${balance:.2f}")
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: $"))
                if amount > 0:
                    balance += amount
                    print(f"${amount:.2f} deposited successfully!")
                    print(f"New balance: ${balance:.2f}")
                else:
                    print("Invalid amount. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: $"))
                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        print(f"${amount:.2f} withdrawn successfully!")
                        print(f"Remaining balance: ${balance:.2f}")
                    else:
                        print("Insufficient funds!")
                else:
                    print("Invalid amount. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == "4":
            print("Thank you for using Python Bank ATM!")
            print("Have a great day!")
            break
        else:
            print("Invalid option. Please select 1-4.")