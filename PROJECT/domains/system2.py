import re
import os
import json
import random
from domains.user import User

class System:
    def __init__(self):
        self.users: list[User] = []

        self.mobile_plans = {
            1: {"name": "Diamond", "price": 200000, "gb": 20},
            2: {"name": "Gold", "price": 150000, "gb": 15},
            3: {"name": "Silver", "price": 100000, "gb": 10},
            4: {"name": "Bronze", "price": 50000, "gb": 5},
        }

        if os.path.exists("users.json"):
            self.load_data_from_json("users.json")

        self.logged_in_user = User() # This is a blank user object, to be assigned to the logged in user object

    # ==============================
    # SAVE/LOAD PERSISTENT USER DATA
    # ==============================

    def load_data_from_json(self, file_name: str) -> None:
        with open(file_name, "r") as f:
            data = json.load(f)
            for user in data:
                # create a blank, temporary user object to assign the raw data
                user_obj = User()

                # assigns data to the temporary user
                try:
                    user_obj.username = user["username"]
                    user_obj.password = user["password"]
                    user_obj.balance = user["balance"]

                    user_obj.mobile_plan_id = user["mobile_plan_id"]

                    user_obj.domain_name = user["domain_name"]
                    user_obj.domain_ip = user["domain_ip"]
                    user_obj.current_vpn_plan_id = user["current_vpn_plan_id"]
                    user_obj.current_vps_plan_id = user["current_vps_plan_id"]
                except: # if the data is not complete, skip it
                    pass

                # append to the list in System
                self.users.append(user_obj)

    def flush_data_to_json(self) -> None:
        # Create a temporary list to store the serialized data
        data: list[dict[str, str | int]] = []

        # Loop through all users and append the serialized data to the temporary list
        for user in self.users:
            data.append(user.serialize())

        # Write the temporary list to the file
        with open("users.json", "w") as f:
            json.dump(data, f)

    # ======================
    # LOG-IN/LOG-OUT/SIGN-UP
    # ======================

    def create_account(self):
        # Handling username
        while True:
            username = input("Enter your username: ")
            for user in self.users:
                if username == user.username:
                    print("Username already exists! Please try again.\n")
                    continue        
            else:
                break

        # Handling password
        password = input("Enter your password: ")
        while True:
            if len(password) < 8:
                password = input("Password must be 8 or more characters! Please try again: ")
            else:
                password_confirm = input("Confirm your password: ")
                if password == password_confirm:
                    break
                else:
                    password = input("Password does not match! Please try again: ")

        # Save the new user to the list
        user = User()
        user.username = username
        user.password = user.encrypt_password(password)
        self.users.append(user)

    def sign_in(self) -> bool:
        attempts = 0
        while True:
            input()
            attempts += 1
            if attempts >= 3:
                print("You have exceeded the number of attempts. Please try again later.")
                return False
            username = input("Enter your username: ")
            # if user accidentally hit login, they can return to main menu by not entering username
            for user in self.users:
                if not user.username == username:
                    print("Invalid username, do you want to return to login menu? (Y/n)")
                    choice = input().lower()
                    if choice == "n":
                        continue
                    else:
                        return False

            password = input("Enter your password: ")
            for user in self.users:
                if user.username == username and user.password == self.logged_in_user.encrypt_password(password):
                    print("Login successful!")
                    self.logged_in_user = user
                    return True

            print("Invalid username or password!")

    def sign_out(self) -> bool:
        """Set the status is False to logout"""
        print("Logout successful!")
        return False

    # ==================
    # BALANCE MANAGEMENT
    # ==================

    def check_balance(self):
        print(f"Your balance: {self.logged_in_user.balance} VND")

    def top_up(self):
        print("Enter the amount you want to recharge: ")
        amount = int(input())
        self.logged_in_user.balance += amount  # add amount to balance
        print("Recharge successful!")
        print(f"Your balance: {self.logged_in_user.balance} VND")

    def check_plan(self):
        # check product_id in file to check plan that user is using. if product_id = 0, user is not using any plan
        if self.logged_in_user.product_id == 0:
            print("You have not subscribed to any plan yet!")
            return
    # ======================
    # MOBILE PLAN MANAGEMENT
    # ======================

        selected_plan = self.products[self.logged_in_user.product_id]
        print(f"Your current plan is: {selected_plan['name']}")

    def check_product(self):  # check product information
        print("Available products: Product information will be displayed by the order: Name - Price - GB - Months")
        for product in self.products:
            print(f"{product}. {self.products[product]['name']} - {self.products[product]['price']} VND - {self.products[product]['gb']} GB")
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

    def buy_product(self) -> None:
      
        # prints all products
        print("Available products: Product information will be displayed by the order: Name - Price - GB - Months")
        for product in self.products:
                print(f"- {product}. {self.products[product]['name']} - {self.products[product]['price']} VND - {self.products[product]['gb']} GB")

        # prompts user to choose a product
        while True:

            product_id = int(input("Enter product ID to purchase (0 to cancel): "))
            if product_id == 0:
                print("Purchase cancelled.")
                return
            #if user already has a plan, print current plan and ask if they want to change plan
            if self.logged_in_user.product_id != 0:
                print(f"Your current plan is: {self.products[self.logged_in_user.product_id]['name']}. Do you want to change plan? (Y/n)")
                choice = input().lower()
                if choice == "n":
                    print("Purchase cancelled.")
                    return
            # checks if product_id is valid
            if product_id not in self.products:
                print("Invalid product ID. Please try again.")
                continue

            # checks if user has sufficient balance
            if self.logged_in_user.balance < int(self.products[product_id]['price']):
                print("Insufficient balance.")
                return
            
            # updates user's product and balance
            self.logged_in_user.product_id = product_id
            self.logged_in_user.balance -= int(self.products[product_id]['price'])
            print("Purchase successful!")
            return

    # =================
    # DOMAIN MANAGEMENT
    # =================


    def get_user_object(self, username: str) -> User:
        for user in self.users:
            if user.username == username:
                return user
        return None

    def is_domain_name_available(self, domain_name: str) -> bool:
        for user in self.users:
            if user.domain_name == domain_name:
                return False
        return True

    def get_random_ip(self):
        while True:
            random_ip = ".".join([str(random.randint(0, 255)) for _ in range(4)])
            for user in self.users:
                if user.domain_ip == random_ip:
                    continue
            return random_ip

    # ========
    # COSMETIC
    # ========

    def clear_screen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
