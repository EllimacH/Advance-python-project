import os
import time
from datetime import datetime
import random

date = datetime.now()

users = {}

products = {
    1: {'name': 'Diamond', 'price': 200000, 'GB': 20, 'months': 1},
    2: {'name': 'Gold   ', 'price': 150000, 'GB': 15, 'months': 1},
    3: {'name': 'Silver ', 'price': 100000, 'GB': 10, 'months': 1},
    4: {'name': 'Bronze ', 'price': 50000, 'GB': 5, 'months': 1}
}


def create_account():
    """
    Creates a new user account and stores the username and password in the users dictionary.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    password2 = input("Reconfirm your password: ")
    if password == password2:
        try:
            users[username] = password
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
        if username in users and password == users[username]:
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


# def check_product():
#     """
#     Displays the list of available products.
#     """
#     print("Available products: Product information will be displayed by the order: Name - Price - GB - Months")
#     for key, value in products.items():
#         print(
#             f"{key}. {value['name']} -  {value['price']} - {value['GB']} - {value['months']}")
#     print("[+] Date:", date.strftime("%d-%m-%Y %I:%M"))


# def check_product_discription():
#     choice = int(input("Enter the product number: "))
#     if choice == 1:
#         print("Diamond package: 200k VND for 1 month, suitable for small and medium companies. When you buy 6 months or more, you will get 1 month promotion at the same price. When you buy 1 year or more, you will get 2 months promotion at the same price.")
#     elif choice == 2:
#         print("Gold package: 150k VND for 1 month, suitable for people who go to work need to use the internet. When you buy 6 months or more, you will get 1 month promotion at the same price. When you buy 1 year or more, you will get 2 months promotion at the same price.")
#     elif choice == 3:
#         print("Silver package: 100k VND for 1 month, suitable people who go to work need to use the internet. When you buy 6 months or more, you will get 1 month promotion at the same price. When you buy 1 year or more, you will get 2 months promotion at the same price.")
#     elif choice == 4:
#         print("Bronze package: 50k VND for 1 month, suitable for students or pupils. When you buy 6 months or more, you will get 1 month promotion at the same price. When you buy 1 year or more, you will get 2 months promotion at the same price.")
#     else:
#         print("Invalid input")

def check_product():
    """
    Displays the list of available products.
    """
    print("Available products: Product information will be displayed by the order: Name - Price - GB - Months")
    for key, value in products.items():
        print(
            f"{key}. {value['name']} -  {value['price']} - {value['GB']} - {value['months']}")
    print("[+] Date:", date.strftime("%d-%m-%Y %I:%M"))

    choice = int(input("Enter the product number to get more information about this product: "))
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


def buy_product():
    """
    Buys a product from the list of available products.
    """
    global balance
    global plan
    check_product()
    try:
        product_id = int(input("Enter the product ID: "))
        if product_id in products:
            if balance >= products[product_id]['price']:
                balance -= products[product_id]['price']
                plan = products[product_id]['name']
                print(
                    f"Product {products[product_id]['name']} purchased successfully!")
                print("Your current balance is:", balance)
                print("[+] Date:", date.strftime("%d-%m-%Y %I:%M"))
            else:
                print("Insufficient funds!")
        else:
            print("Invalid product ID!")
    except ValueError:
        print("Invalid input. Please enter a number.\n")


def current_plan(plan=None):
    """
    Displays the user's current plan.
    """
    if plan is None:
        print("You have no plan at the moment.")
    else:
        print("Your current plan is:", plan)
    print("[+] Date:", date.strftime("%d-%m-%Y %I:%M"))


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def sign_out():
    """
    Signs out the user.
    """
    print("Signing out...")
    print("[+] Date:", date.strftime("%d-%m-%Y %I:%M"))
    return False


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
                if sign_in():
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
                                deposit()
                                input('Press enter to continue.')
                            elif choice == 2:
                                check_balance()
                                input('Press enter to continue.')
                            elif choice == 3:
                                check_product()
                                input('Press enter to continue.')
                            elif choice == 4:
                                buy_product()
                                input('Press enter to continue.')
                            elif choice == 5:
                                current_plan()
                                input('Press enter to continue.')
                            elif choice == 6:
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


