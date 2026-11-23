# Bank Balance Checking Program

correct_pin = "1234"
balance = 25000.00

print("===== WELCOME TO SHERRU BANK =====")
print("Branch:mumbai")
print("Enter your accountholder name:")
pin = input("Enter your ATM PIN: ")


if pin == correct_pin:
    print("\nLogin Successful!")
    print("--------------------------")
    print("1. Check Balance")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nYour Current Bank Balance is: ₹", balance)
    elif choice == "2":
        print("Thank you for using ABC Bank!")
    else:
        print("Invalid choice!")

else:
    print("Incorrect PIN! Access Denied.") 
