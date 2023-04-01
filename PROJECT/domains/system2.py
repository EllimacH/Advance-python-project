import re
import os
import time
import hashlib
from datetime import datetime
from domains.product import Product
from domains.user import User


class System:
    def __init__(self):
        self.products = [
            {"id": 1, "name": "Diamond", "price": 200000, "gb": 20, "months": 1},
            {"id": 2, "name": "Gold", "price": 150000, "gb": 15, "months": 1},
            {"id": 3, "name": "Silver", "price": 100000, "gb": 10, "months": 1},
            {"id": 4, "name": "Bronze", "price": 50000, "gb": 5, "months": 1},
        ]

        self.users = []
        if os.path.isfile("users.txt"):
            with open("users.txt", "r") as f:
                for line in f:
                    line = line.rstrip("\n").split(",")
                    if len(line) < 4:
                        continue
                    if line[0] != "username":
                        user = User(line[0], line[1], int(line[2]), int(line[3]))
                        self.users.append(user)

    def create_account(self):
        while True:
            username = input("Enter your username: ")
            if not os.path.isfile("users.txt"):
                with open("users.txt", "w") as f:
                    f.write("username,password,balance,product_id \n")
            with open("users.txt", "r") as f:
                for line in f:
                    line = line.rstrip("\n").split(",")
                    if username == line[0]:
                        print("Username already exists! Please try again.\n")
                        return False
            password = input("Enter your password: ")
            if len(password) < 8:
                print("Password must be 8 or more characters! Please try again.")
            else:
                break
        password2 = input("Reconfirm your password: ")
        if password == password2:
            try:
                user = User(username, password, 0, None)
                self.users.append(user)
                print("Account created successfully!\n")
                with open("users.txt", "a") as f:
                    f.write(f"{username},{password},0,0\n")
            except Exception as e:
                print(f"An error occurred while creating your account: {e}")
        else:
            print("Invalid information! Please try again.\n")

    def sign_in(self):
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
                        break
            if found:
                print("Login successful!")
                return username
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

    def check_balance(self, username):
        for user in self.users:
            if user.username == username:
                print(f"Your balance: {user.balance} VND")
                return
        print("User not found")

    def top_up(self, username):
        print("Enter the amount you want to recharge: ")
        amount = int(input())
        for user in self.users:
            if user.username == username:
                user.balance += amount
                print("Recharge successful!")
                print(f"Your balance: {user.balance} VND")
                with open("users.txt", "r") as f:
                    lines = f.readlines()
                with open("users.txt", "w") as f:
                    for line in lines:
                        line = line.rstrip("\n").split(",")
                        if line[0] == username:
                            line[2] = str(user.balance)
                            line = ",".join(line)
                        f.write(line + "\n")
                return
        print("User not found")

    def check_plan(self, username):
        for user in self.users:
            if user.username == username:
                if user.product_id == None:
                    print("You have not subscribed to any plan yet!")
                    return
                for product in self.products:
                    if product["id"] == user.product_id:
                        print(f"Your current plan is: {product['name']}")
                        return
        print("User not found")


    def check_product(self):
        print("Available products: Product information will be displayed by the order: Name - Price - GB - Months")
        for product in self.products:
            print(
                f"{product['id']}. {product['name']} - {product['price']} VND - {product['gb']} GB - {product['months']} month")
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

    # def buy_product(self, username):
    #     print("Enter the product number you want to buy: ")
    #     for product in self.products:
    #         print(
    #             f"{product['id']}. {product['name']} - {product['price']} VND - {product['gb']} GB - {product['months']} month")
    #     choice = int(input())
    #     for user in self.users:
    #         if user.username == username:
    #             if user.balance < self.products[choice - 1]['price']:
    #                 print("Not enough balance!")
    #                 return
    #             user.balance -= self.products[choice - 1]['price']
    #             user.product_id = self.products[choice - 1]['id']
    #             print("Purchase successful!")
    #             print(f"Your balance: {user.balance} VND")
    #             with open("users.txt", "r") as f:
    #                 lines = f.readlines()
    #             with open("users.txt", "w") as f:
    #                 for line in lines:
    #                     line = line.rstrip("\n").split(",")
    #                     if line[0] == username:
    #                         line[2] = str(user.balance)
    #                         line[3] = str(user.product_id)
    #                         line = ",".join(line)
    #                     f.write(line + "\n")
    #             return
    #     print("User not found")
    #enhance the code above by adding check if the user has already bought a plan or not and if the user has bought a plan, ask if they want to change the plan or not
    def buy_product(self, username):
        print("Enter the product number you want to buy: ")
        for product in self.products:
            print(
                f"{product['id']}. {product['name']} - {product['price']} VND - {product['gb']} GB - {product['months']} month")
        choice = int(input())
        for user in self.users:
            if user.username == username:
                if user.balance < self.products[choice - 1]['price']:
                    print("Not enough balance!")
                    return
                if user.product_id == None:
                    user.balance -= self.products[choice - 1]['price']
                    user.product_id = self.products[choice - 1]['id']
                    print("Purchase successful!")
                    print(f"Your balance: {user.balance} VND")
                    with open("users.txt", "r") as f:
                        lines = f.readlines()
                    with open("users.txt", "w") as f:
                        for line in lines:
                            line = line.rstrip("\n").split(",")
                            if line[0] == username:
                                line[2] = str(user.balance)
                                line[3] = str(user.product_id)
                                line = ",".join(line)
                            f.write(line + "\n")
                    return
                else:
                    print("You have already bought a plan. Do you want to change your plan? (Y/N)")
                    choice = input()
                    if choice == "Y" or choice == "y":
                        user.balance -= self.products[choice - 1]['price']
                        user.product_id = self.products[choice - 1]['id']
                        print("Purchase successful!")
                        print(f"Your balance: {user.balance} VND")
                        with open("users.txt", "r") as f:
                            lines = f.readlines()
                        with open("users.txt", "w") as f:
                            for line in lines:
                                line = line.rstrip("\n").split(",")
                                if line[0] == username:
                                    line[2] = str(user.balance)
                                    line[3] = str(user.product_id)
                                    line = ",".join(line)
                                f.write(line + "\n")
                        return
                    if choice == "N" or choice == "n":
                        return
        print("User not found")
        




    def clear_screen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
