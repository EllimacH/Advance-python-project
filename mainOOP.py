import os
import time
import hashlib
from datetime import datetime


class User:
    def __init__(self, username, password, balance=0, current_plan=None):
        self.username = username
        self.password = hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), b'salt', 100000)
        self.balance = balance
        self.current_plan = current_plan

    def check_password(self, password):
        return self.password == hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), b'salt', 100000)


class Product:
    def __init__(self, id, name, price, gb, months):
        self.id = id
        self.name = name
        self.price = price
        self.gb = gb
        self.months = months


class System:
    def __init__(self):
        self.users = {}
        self.products = [
            Product(1, 'Diamond', 200000, 20, 1),
            Product(2, 'Gold', 150000, 15, 1),
            Product(3, 'Silver', 100000, 10, 1),
            Product(4, 'Bronze', 50000, 5, 1)
        ]

    def create_account(self):
        while True:
            username = input("Enter your username: ")
            if username in self.users:
                print("Username already exists! Please try again.\n")
            else:
                break
        while True:
            password = input("Enter your password: ")
            if len(password) < 8:
                print("Password must be 8 or more characters! Please try again.")
            else:
                break
        password2 = input("Reconfirm your password: ")
        if password == password2:
            try:
                user = User(username, password)
                self.users[username] = user
                print("Account created successfully!\n")
                with open("users.txt", "a") as f:
                    f.write(username+","+password+"\n")
            except Exception as e:
                print(f"An error occurred while creating your account: {e}")
        else:
            print("Invalid information! Please try again.\n")

    # def load_users(self):
    #     with open("users.txt", "r") as f:
    #         for line in f:
    #             line = line.rstrip("\n").split(",")
    #             username = line[0]
    #             password = line[1]
    #             user = User(username, password)
    #             self.users[username] = user

    def sign_in(self):
        attempts = 0
        while attempts < 3:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username in self.users and self.users[username].check_password(password):
                print("Login successful!")
                print("[+] Date:", datetime.now().strftime("%d-%m-%Y %I:%M"))
                return self.users[username]
            else:
                print("Invalid username or password!")
                attempts += 1
                print("Do you want to return to login menu? (Y/N)")
                choice = input()
                if choice == "Y" or choice == "y":
                    return None
                if choice == "N" or choice == "n":
                    print("you have", 3-attempts, "attempts left")
                    continue
        print("You have exceeded the number of attempts. Please try again later.")

    def sign_out(self):
        print("Logout successful!")
        return None

    def check_product(self):
        print("Available products: Product information will be displayed by the order: Name - Price - GB - Months")
        for product in self.products:
            print(
                f"{product.id}. {product.name} - {product.price} VND - {product.gb} GB - {product.months} months")
        print("Enter the product number to get more information about this product: ")
        choice = int(input())
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

    def buy_product(self, user):
        print("Choose a product to buy:")
        for product in self.products:
            print(
                f"{product.id}. {product.name} - {product.price} VND - {product.gb} GB - {product.months} months")
        while True:
            try:
                product_id = int(input("Enter product ID: "))
                product = self.products[product_id - 1]
                break
            except:
                print("Invalid product ID! Please try again.")
        if user.balance >= product.price:
            user.balance -= product.price
            user.current_plan = product
            print("Purchase successful!")
            print(f"Your new balance is {user.balance} VND")
        else:
            print("Not enough balance!")

    def check_balance(self, user):
        print(f"Your balance is {user.balance} VND")

    def check_plan(self, user):
        if user.current_plan:
            print(f"Your current plan is {user.current_plan.name}")
        else:
            print("You don't have any plan yet!")

    def top_up(self, user):
        while True:
            try:
                amount = int(input("Enter amount to top_up: "))
                break
            except:
                print("Invalid amount! Please try again.")
        user.balance += amount
        print("Top-up successfully!")
        print(f"Your new balance is {user.balance} VND")

    def clear_screen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def main(self):
        # self.load_users()
        user = None
        print("Welcome to the Internet Service Provider (B.A.T.E) system!")
        while True:
            if user:
                print("1. Buy product")
                print("2. Check balance")
                print("3. Check current plan")
                print("4. Top-up")
                print("5. Sign out")
                print("6. Check product")
                choice = input("Enter your choice: ")
                if choice == "1":
                    self.clear_screen()
                    self.buy_product(user)
                    input("Press Enter to continue...")
                    self.clear_screen()
                elif choice == "2":
                    self.clear_screen()            
                    self.check_balance(user)
                    input("Press Enter to continue...")
                    self.clear_screen()
                elif choice == "3":
                    self.clear_screen()
                    self.check_plan(user)
                    input("Press Enter to continue...")
                    self.clear_screen()
                elif choice == "4":
                    self.clear_screen()
                    self.top_up(user)
                    input("Press Enter to continue...")
                    self.clear_screen()
                elif choice == "5":
                    user = self.sign_out()
                elif choice == "6":
                    self.clear_screen()
                    self.check_product()
                    input("Press Enter to continue...")
                    self.clear_screen()

                else:
                    print("Invalid choice! Please try again.")
                    self.clear_screen( )
            else:
                print("1. Create account")
                print("2. Sign in")
                print("3. Exit")
                choice = input("Enter your choice: ")
                self.clear_screen()
                if choice == "1":
                    self.create_account()
                elif choice == "2":
                    user = self.sign_in()
                elif choice == "3":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice! Please try again.")


if __name__ == "__main__":
    System().main()

