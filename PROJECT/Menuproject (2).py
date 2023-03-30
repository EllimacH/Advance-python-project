import os
import time
import hashlib
import datetime
from datetime import datetime

date = datetime.now()

users = {}
balance = 0

products = {
    1: {'name': 'Diamond', 'price': 200000, 'GB': 20, 'months': 1},
    2: {'name': 'Gold   ', 'price': 150000, 'GB': 15, 'months': 1},
    3: {'name': 'Silver ', 'price': 100000, 'GB': 10, 'months': 1},
    4: {'name': 'Bronze ', 'price': 50000, 'GB': 5, 'months': 1}
}

# creates a new user account and stores the username and hashed password in the users dictionary. If users type wrong password, it will ask them to retype again.


def create_account():
    global users
    username = input("Enter your username: ")
    # check if users.txt exists, create it if it doesn't
    if not os.path.isfile("users.txt"):
        with open("users.txt", "w") as f:
            f.write("username,password,balance,product_ID\n")
    with open("users.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n").split(",")
            if username == line[0]:
                print("Username already exists! Please try again.\n")
                return False
    while True:
        password = input("Enter your password: ")
        if len(password) < 8:
            print("Password must be 8 or more characters! Please try again.")
        else:
            break
    password2 = input("Reconfirm your password: ")
    if password == password2:
        try:
            hashed_password = hashlib.pbkdf2_hmac(
                'sha256', password.encode('utf-8'), b'salt', 100000)
            users[username] = hashed_password
            balance = 0
            print("Account created successfully!\n")
            with open("users.txt", "a") as f:
                f.write(f"{username},{password},{balance}\n")
        except Exception as e:
            print(f"An error occurred while creating your account: {e}")
    else:
        print("Invalid information! Please try again.\n")


def sign_in():
    global users
    attempts = 0
    while attempts < 3:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        found = False
        with open("users.txt", "r") as f:
            for line in f:
                line = line.rstrip("\n").split(",")
                if username == line[0] and password == line[1]:
                    found = True

        if found:
            print("Login successful!")
            print("[+] Date:", datetime.now().strftime("%d-%m-%Y %I:%M"))
            return username
        else:
            print("Invalid username or password!")
            attempts += 1
    print("Too many login attempts!")
    return None


def deposit(username):
    try:
        amount = int(input("Enter the amount to deposit: "))
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        return

    with open("users.txt", "r") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].rstrip("\n").split(",")
        if username == line[0]:
            balance = int(line[2])
            break

    balance += amount

    with open("users.txt", "w") as f:
        for i in range(len(lines)):
            line = lines[i].rstrip("\n").split(",")
            if username == line[0]:
                lines[i] = f"{line[0]},{line[1]},{balance}\n"
        f.writelines(lines)

    print("Deposit successful! Current balance is:", balance)
    print("[+] Date:", datetime.now().strftime("%d-%m-%Y %I:%M"))


def check_balance(username):
    with open("users.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n").split(",")
            if username == line[0]:
                balance = int(line[2])
                print(f"Your current balance is: {balance}")
                print("[+] Date:", date.strftime("%d-%m-%Y %I:%M"))
                return
        print("Username not found!")


def check_product():
    print("Available products: Product information will be displayed by the order: Name - Price - GB - Months")
    for key, value in products.items():
        print(
            f"{key}. {value['name']} -  {value['price']} - {value['GB']} - {value['months']}")
    print("[+] Date:", date.strftime("%d-%m-%Y %I:%M"))

    choice = int(
        input("Enter the product number to get more information about this product: "))
    if choice == 1:
        print("Diamond package: 200k VND for 1 month, suitable for small and medium companies. When you buy 6 months or more, you will get 1 month promotion at the same price. When you buy 1 year or more, you will get 2 months promotion at the same price.")
    elif choice == 2:
        print("Gold package: 150k VND for 1 month, suitable for people who go to work need to use the internet. When you buy 6 months or more, you will get 1 month promotion at the same price. When you buy 1 year or more, you will get 2 months promotion at the same price.")
    elif choice == 3:
        print("Silver package: 100k VND for 1 month, suitable people who go to work need to use the internet. When you buy 6 months or more, you will get 1 month promotion at the same price. When you buy 1 year or more, you will get 2 months promotion at the same price.")
    elif choice == 4:
        print("Bronze package: 50k VND for 1 month, suitable for students or pupils. When you buy 6 months or more, you will get 1 month promotion at the same price. When you buy 1 year or more, you will get 2 months promotion at the same price.")
    else:
        print("Invalid input")

# Buys a product from the list of available products. If the user has enough balance, the product will be purchased and the user's balance will be updated. Otherwise, the user will be notified that they have insufficient funds. If the user enters an invalid input, program will answer "Invalid input. Please enter a number."


def check_buy_product():
    # Displays the list of available products.
    print("Available products: Product information will be displayed by the order: Name - Price - GB - Months")
    for key, value in products.items():
        print(
            f"{key}. {value['name']} -  {value['price']} - {value['GB']} - {value['months']}")
    print("[+] Date:", date.strftime("%d-%m-%Y %I:%M"))


def buy_product(username):
    global balance
    global plan
    check_buy_product()
    try:
        with open("users.txt", "r") as f:
            lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i].rstrip("\n").split(",")
            if line[0] == username:
                balance = int(line[2])
                if len(line) >= 4 and line[3] != '0':
                    print("You have already bought a product!")
                    return
                product_id = int(input("Enter the product ID: "))
                if product_id in products:
                    if balance >= products[product_id]['price']:
                        balance -= products[product_id]['price']
                        plan = products[product_id]['name']
                        print(
                            f"Product {products[product_id]['name']} purchased successfully!")
                        print("Your current balance is:", balance)
                        print("[+] Date:", date.strftime("%d-%m-%Y %I:%M"))
                        lines[i] = f"{line[0]},{line[1]},{balance},{product_id}\n"
                        with open("users.txt", "w") as f:
                            f.writelines(lines)
                    else:
                        print("Insufficient funds!")
                    return
        print("User not found in file!")
    except ValueError:
        print("Invalid input. Please enter a number.\n")


def current_plan(username):
    with open("users.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        fields = line.strip().split(',')
        if fields[0] == username:
            if len(fields) < 4 or not fields[3]:
                print("You have no plan at the moment.")
            else:
                product_id = int(fields[3])
                name = products[product_id]['name']
                data = products[product_id]['GB']
                price = products[product_id]['price']
                time = products[product_id]['months']
                if product_id in products:
                    print(
                        f"Your current plan is:, {name} - {price}VND - {data}GB - {time}month")
                else:
                    print("Unknown plan.")
            print("[+] Date:", date.now().strftime("%d-%m-%Y %I:%M"))
            return
    print("User not found in file!")

# Clears the screen.


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# The main function. There are 3 options: create account, sign in, and exit.
# If the user chooses to create an account, the program will ask for the user's username and password.
# If the user chooses to sign in, the program will ask for the user's username and password.
# If the user enters the correct username and password, the program will display the user's balance and the list of available products. The user can then choose to deposit, check balance, check product, buy product, check current plan, or sign out.
# If the user chooses to deposit, the program will ask for the amount of money to deposit.
# If the user chooses to check balance, the program will display the user's balance.
# If the user chooses to check product, the program will display the list of available products.
# If the user chooses to buy product, the program will ask for the product ID.
# If the user chooses to check current plan, the program will display the user's current plan.
# If the user chooses to sign out, the program will return to the main menu.
# If the user enters an invalid input, the program will notify the user that the input is invalid.


def main():
    """
    The main function.
    """
    global balance
    balance = 0
    print("Welcome to Internet Service Provider")
    while True:
        print("1. Create account")
        print("2. Sign in")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice: "))
            clear_screen()
            if choice == 1:
                create_account()
            elif choice == 2:
                username = sign_in()
                if username:
                    while True:
                        print("1. Deposit")
                        print("2. Check balance")
                        print("3. Check product")
                        print("4. Buy product")
                        print("5. Check current plan")
                        print("6. Sign out")
                        try:
                            choice = int(input("Enter your choice: "))
                            if choice == 1:
                                deposit(username)
                                input('Press enter to continue.')
                            elif choice == 2:
                                check_balance(username)
                                input('Press enter to continue.')
                            elif choice == 3:
                                check_product()
                                input('Press enter to continue.')
                            elif choice == 4:
                                buy_product(username)
                                input('Press enter to continue.')
                            elif choice == 5:
                                current_plan(username)
                                input('Press enter to continue.')
                            elif choice == 6:
                                print("Signed out successfully!")
                                break
                            else:
                                print("Invalid choice!")
                            clear_screen()
                        except ValueError:
                            print("Invalid input. Please enter a number.\n")
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input. Please enter a number.\n")


main()
