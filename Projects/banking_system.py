# ****** Project Banking System Easy to Advance *****

balance = 0
is_running = True
MPIN = '9861'


def show_balance():
    print(f"Your Current Balance Is Rs {balance:.2f}")


def deposit():
    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Invalid amount!")
        return 0
    else:
        return amount


def withdraw():
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient balance!")
        return 0
    elif amount <= 0:
        print("Invalid amount!")
        return 0
    else:
        transaction_pin = input("Enter Your Transaction PIN for processing: ")
        
        if transaction_pin == MPIN:            
            return amount
        else:
            print("Something Went Wrong!!")
            return 0


def sign_up():
    global balance, is_running

    # user = input("Enter Your Username: ")
    # passwrd = input("Enter Password: ")

    while True:
        print("\n--- Banking Menu ---")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            show_balance()
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw()
        elif choice == '4':
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice!")


def register_account():
    user_name = input("Enter Your Username: ")
    password = input("Enter Strong password for your Account: ")

    with open("Projects/credentials.txt", "w") as f:
        f.write(f"Username = {user_name}\n")
        f.write(f"Password = {password}\n")

    print("Account registered successfully!")
    print("You can now Sign Up.")

def main():
    global is_running

    while is_running:
        print("\n*** Welcome to Banking System ***")
        print("1. Sign Up")
        print("2. Register")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            sign_up()
        elif choice == '2':
            register_account()
        elif choice == '3':
            print("Thank you for using Banking System!")
            is_running = False
        else:
            print("Invalid input!")


if __name__ == '__main__':
    main()


    




    

