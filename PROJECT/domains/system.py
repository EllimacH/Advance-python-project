import re
import os
import time
import hashlib
from datetime import datetime
from domains.product import Product
from domains.user import User

class System:
    def __init__(self):
        self.users = {}
        self.products = [
            Product(1, 'Diamond', 200000, 20, 1),
            Product(2, 'Gold', 150000, 15, 1),
            Product(3, 'Silver', 100000, 10, 1),
            Product(4, 'Bronze', 50000, 5, 1)
        ]

    def create_account(self, users: list):
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
            global password
            password = input("Enter your password: ")
            if len(password) < 8:
                print("Password must be 8 or more characters! Please try again.")
            else:
                break
        password2 = input("Reconfirm your password: ")
        if password == password2:
            try:
                user = User(username, password)
                # self.users[username] = user
                # adding user to users array
                users.append(user)
                print("Account created successfully!\n")
                with open("users.txt", "a") as f:
                    f.write(username+","+password+"\n")
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
            # with open("users.txt", "r") as f:
            #     for line in f:
            #         line = line.rstrip("\n").split(",")
            #         if username == line[0] and password == line[1]:
            #             found = True
            #             break
            # if found:
            #     print("Login successful!")
            #     return username


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

    def buy_product(self, user: User):
        # try:
        #     with open("users.txt", "r") as f:
        #         lines = f.readlines()
        #     for i in range(len(lines)):
        #         line = lines[i].rstrip("\n").split(",")
        #         if line[0] == username:
        #             balance = int(line[2])
        #             if len(line) >= 4 and line[3] != '0':
        #                 print("You have already bought a product!")
        #                 return
        try:
            with open("users.txt", "r") as f:
                lines = f.readlines()
            for line in lines:
                fields = line.strip().split(',')
                if fields[0] == user.username:
                    user.balance = int(fields[2])
                    if len(fields) >= 4 and fields[3] != '0':
                        print("You have already bought a product!")
                        return
        except:
            pass

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
        print(f"Your balance is {user.get_balance()} VND")

 

    def check_plan(self, user):
        if user.current_plan:
            print(f"Your current plan is {user.current_plan.name}")
        else:
            with open("users.txt", "r") as f:
                lines = f.readlines()
            for line in lines:
                fields = line.strip().split(',')
                if fields[0] == user.username:
                    if len(fields) < 4 or not fields[3]:
                        print("You have no plan at the moment.")

    # def top_up(self, user):
    #     while True:
    #         try:
    #             amount = int(input("Enter amount to top_up: "))
    #             break
    #         except:
    #             print("Invalid amount! Please try again.")
    #     with open("users.txt", "r") as f:
    #         lines = f.readlines()
    #     for i in range(len(lines)):
    #         line = lines[i].rstrip("\n").split(",")
    #         if line[0] == user.username:
    #             if len(line) >= 3: # check the length of the line list
    #                 user.balance = int(line[2])
    #             else:
    #                 user.balance = 0 # set balance to zero if there are not enough elements
    #             break
    #     user.balance += amount

    #     with open("users.txt", "r") as f:
    #         lines = f.readlines()
    #     with open("users.txt", "w") as f:
    #         for line in lines:
    #             if line.startswith(user.username):
    #                 f.write(f"{user.username},{user.password},{user.balance}\n")
    #             else:
    #                 f.write(line)

    def top_up(self, user):
        while True:
            try:
                amount = int(input("Enter amount to deposit: "))
                break
            except:
                print("Invalid amount! Please try again.")
        with open("users.txt", "r") as f:
            lines = f.readlines()
        with open("users.txt", "w") as f:
            for line in lines:
                if line.startswith(user.username):
                    f.write(f"{user.username},{password},{user.balance}\n")
                else:
                    f.write(line)

        user.balance += amount

        print("Top-up successfully!")
        print(f"Your new balance is {user.balance} VND")

    def clear_screen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
