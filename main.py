import time
import hashlib
from datetime import datetime

date = datetime.now()

users = {}

products = {
    1: {'name': 'Diamond', 'price': 200000, 'time': 20, 'months': 1},
    2: {'name': 'Gold', 'price': 150000, 'time': 15, 'months': 1},
    3: {'name': 'Silver', 'price': 100000, 'time': 10, 'months': 1},
    4: {'name': 'Bronze', 'price': 50000, 'time': 5, 'months': 1}
}


def create_account():
    """
    Creates a new user account and stores the username and hashed password in the users dictionary.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    password2 = input("Reconfirm your password: ")
    if password == password2:
        try:
            hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), b'salt', 100000)
            users[username] = hashed_password
            print("Account created successfully!\n")
        except Exception as e:
            print(f"An error occurred while creating your account: {e}")
    else:
        print("Invalid information! Please try again.\n")


def sign_in():
    """
    Authenticates a user by checking their username and password against the values in the users dictionary.
    """
    global users
    attempts = 0
    while attempts < 3:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in users and hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'),
                b'salt', 100000) == users[username]:
            print("Login successful!")
            print("[+] Date:", date.strftime("%d-%m-%Y %I:%M"))
            return True
        else:
            print("Invalid username or password!")
            attempts += 1
    print("Too many login attempts!")
    return False


def deposit():
    """
    Deposits a specified amount into the user's account balance.
    """
    global balance
    try:
        amount = int(input("Enter the amount to deposit: "))
        balance += amount
        print("Deposit successful! Current balance is:", balance)
        print("[+] Date:", date.strftime("%d-%m-%Y %I:%M"))
    except ValueError:
        print("Invalid input. Please enter a number.\n")


def check_balance():
    """
    Displays the user's current account balance.
    """
    print("Your current balance is:", balance)
    print("[+] Date:", date.strftime("%d-%m-%Y %I:%M"))

def check_product():
    """
    Displays the list of available products.
    """
    print("Available products: Product information will be displayed by the order: Name - Price - Time - Months")
    for key, value in products.items():
        print(f"{key}. {value['name']} - {value['price']} - {value['time']} - {value['months']}")
    print("[+] Date:", date.strftime("%d-%m-%Y %I:%M"))

def buy_product():
    """
    Buys a product from the list of available products.
    """
    global balance
    check_product()
    try:
        product_id = int(input("Enter the product ID: "))
        if product_id in products:
            if balance >= products[product_id]['price']:
                balance -= products[product_id]['price']
                print(f"Product {products[product_id]['name']} purchased successfully!")
                print("Your current balance is:", balance)
                print("[+] Date:", date.strftime("%d-%m-%Y %I:%M"))
            else:
                print("Insufficient funds!")
        else:
            print("Invalid product ID!")
    except ValueError:
        print("Invalid input. Please enter a number.\n")





def main():
    """
    The main function.
    """
    global balance
    balance = 0
    print("Welcome to B.A.T.E!")
    while True:
        print("1. Create account")
        print("2. Sign in")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                create_account()
            elif choice == 2:
                if sign_in():
                    while True:
                        print("1. Deposit")
                        print("2. Check balance")
                        print("3. Buy product")
                        print("4. Sign out")
                        try:
                            choice = int(input("Enter your choice: "))
                            if choice == 1:
                                deposit()
                            elif choice == 2:
                                check_balance()
                            elif choice == 3:
                                buy_product()
                            elif choice == 4:
                                print("Signed out successfully!")
                                break
                            else:
                                print("Invalid choice!")
                        except ValueError:
                            print("Invalid input. Please enter a number.1\n")
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input. Please enter a number.\n")


main()




#add def function about checkng the product info so that the user can check the product info before buying it