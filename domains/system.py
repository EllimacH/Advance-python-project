import re
import os
import json
import random
from domains.user import User
import customtkinter as ctk
from customtkinter import *
from tkinter import messagebox
from datetime import datetime

class System:
    def __init__(self):
        self.users: list[User] = []

        self.mobile_plans = {
            1: {"name": "Diamond", "price": 2500000, "gb": 500, "description": "Diamond package: 2500000 VND with 500GB for 1 month, suitable for small and medium companies. When you buy 6 months or more, you will get 1 month promotion at the same price. When you buy 1 year or more, you will get 2 months promotion at the same price."},
            2: {"name": "Gold", "price": 500000, "gb": 100, "description": "Gold package: 500000 VND with 100GB for 1 month, suitable for people who go to work need to use the internet. When you buy 6 months or more, you will get 1 month promotion at the same price. When you buy 1 year or more, you will get 2 months promotion at the same price."},
            3: {"name": "Silver", "price": 250000, "gb": 50, "description": "Silver package: 250000 VND with 50GB for 1 month, suitable people who go to work need to use the internet. When you buy 6 months or more, you will get 1 month promotion at the same price. When you buy 1 year or more, you will get 2 months promotion at the same price."},
            4: {"name": "Bronze", "price": 150000, "gb": 30, "description": "Bronze package: 150000 VND with 30GB for 1 month, suitable for students or pupils. When you buy 6 months or more, you will get 1 month promotion at the same price. When you buy 1 year or more, you will get 2 months promotion at the same price."},
        }

        if os.path.exists("users.json"):
            self.load_data_from_json("users.json")

        self.logged_in_user = User() # This is a blank user object, to be assigned to the logged in user object

    # ===================================================================
    #
    #      FOR PERSISTENCE DATA STORAGE, DO NOT MODIFY BELOW THIS LINE
    #
    # ===================================================================

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
                    user_obj.is_admin = user["is_admin"]

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
        data: list[dict[str, str | int | list[dict[str, str | int]]]] = []

        # Loop through all users and append the serialized data to the temporary list
        for user in self.users:
            data.append(user.serialize())

        # Write the temporary list to the file
        with open("users.json", "w") as f:
            json.dump(data, f)

    # ===================================================================
    #
    #      FOR PERSISTENCE DATA STORAGE, DO NOT MODIFY ABOVE THIS LINE
    #
    # ===================================================================

    # =================================================
    #
    #      METHODS FOR THIS CLASS [BELOW] THIS LINE
    #
    # =================================================

    def is_valid_domain(self, domain_name: str) -> bool:
        """Check if domain is vaid + loop through all users and check if domain_name is available"""

        # 2 conditions to check if domain_name is valid
        is_valid = re.match(r"^(?=.{1,255}$)[a-zA-Z0-9](?:(?:[a-zA-Z0-9\-]){0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z]{2,})+$", domain_name)
        is_taken = False

        # iterate users to check if domain_name is taken
        for user in self.users:
            if user.domain_name == domain_name:
                is_taken = True
                break

        # return True if both conditions are met
        if is_valid and not is_taken:
            return True
        else:
            return False

    def get_random_ip(self):
        while True:
            # check if the random_ip is a private IP address
            # - generate a list of 4 random numbers between 0 and 255
            random_ip_list = [str(random.randint(0, 255)) for _ in range(4)]
            # - merge elements in the list into a string separated by dots
            random_ip = ".".join(random_ip_list)
            # - a list of private IP ranges
            private_ip_ranges = ["10.", "172.16.", "192.168."]
            # - a list containing True or False depending on whether the random_ip starts with any of the private IP ranges
            private_range_match = [random_ip.startswith(private_ip_range) for private_ip_range in private_ip_ranges]
            if any(private_range_match): # if any of the private IP ranges match,
                continue # skip the rest of the loop and start again

            # check if the random_ip is already assigned to a user
            ip_taken = False
            for user in self.users: # loop through all users
                if user.domain_ip == random_ip: # if the random_ip is already assigned to a user,
                    ip_taken = True
                    break # break out of the for loop
            if ip_taken:
                continue

            # if the loop ends and no other user has the random_ip, return it
            return random_ip
        
    # =================================================
    #
    #      METHODS FOR THIS CLASS [ABOVE] THIS LINE
    #
    # =================================================

    # ============================================================
    #
    #      METHODS FOR CLI [BELOW] THIS LINE - DO NOT MODIFY
    #
    # ============================================================

    # LOG-IN/LOG-OUT/SIGN-UP

    def create_account(self):
        # Handling username
        while True:
            username = input("\nEnter your username (leave blank to cancel): ")
            for user in self.users:
                if username == "":
                    return
                if username == user.username:
                    print("Username already exists! Please try again.")
                    break
            else:
                break

        # Handling password
        password = input("Enter your password (leave blank to cancel): ")
        while True:
            if password == "":
                return
            if len(password) < 8:
                password = input("Password must be 8 or more characters! Please try again: ")
            else:
                password_confirm = input("Confirm your password: ")
                if password == password_confirm:
                    break
                else:
                    password = input("Password does not match! Please try again: ")

        # Check if this is the first user to be created
        is_admin = False
        if len(self.users) == 0:
            is_admin = True

        # Save the new user to the list
        user = User()
        user.username = username
        user.password = user.encrypt_password(password)
        user.is_admin = is_admin
        self.users.append(user)

    def log_in(self) -> bool:
        attempts = 0
        while True:
            # sign_in attempts handler
            if attempts >= 3:
                print("You have exceeded the number of attempts. Please try again later.")
                return False
            input_username = input("\nEnter your username (leave blank to return to main menu): ")

            # if user accidentally hit login, they can return to main menu by not entering username
            if input_username == "":
                return False

            # username handler
            username_exists = False
            for user in self.users:
                if user.username == input_username:
                    username_exists = True
                    break
            if not username_exists:
                print("Username does not exist! Please try again.")
                continue

            # password handler
            input_password = input("Enter your password (leave blank to return to main menu): ")
            if input_password == "":
                return False
            for user in self.users:
                valid_username = user.username == input_username
                valid_password = user.is_valid_password(input_password)
                if valid_username and valid_password:
                    print("Login successful!")
                    self.logged_in_user = user # so we don't have to loop through all users to find the logged in user every time we need to access their data
                    return True

            attempts += 1
            print("Invalid password!")

    def log_out(self) -> bool:
        """Set the status is False to logout"""
        print("Logout successful!")
        return False

    # BALANCE MANAGEMENT

    def check_balance(self):
        print(f"\nYour balance: {self.logged_in_user.balance} VND")

    def top_up(self) -> None:
        amount = input("\nEnter the amount you want to recharge: ")

        # amount handler
        if not amount.isdigit():
            print("Invalid amount!")
            return

        self.logged_in_user.balance += int(amount)  # add amount to balance
        print("Recharge successful!")
        print(f"Your balance: {self.logged_in_user.balance} VND")

    # MOBILE PLAN MANAGEMENT

    def check_current_plan(self):
        current_mobile_plan_id = self.logged_in_user.mobile_plan_id

        # empty plan handler
        if current_mobile_plan_id == 0:
            print("You have not subscribed to any plan yet!")
            return

        current_plan = self.mobile_plans[current_mobile_plan_id]
        plan_name = current_plan["name"]
        plan_price = current_plan["price"]
        plan_gb = current_plan["gb"]
        print(f"Your current plan is: {plan_name} - {plan_price} VND - {plan_gb} GB")

    def list_mobile_plans(self) -> None:  # check product information
        while True:
            print("\n== Mobile plans ==")
            for plan_id, plan in self.mobile_plans.items():
                print(f"[{plan_id}] {plan['name']} - {plan['price']} VND - {plan['gb']} GB")
            choice = input("Select the plan you want to check more information: ")
            if not choice.isdigit():
                print("Invalid input!")
                break

            choice = int(choice)
            if choice not in self.mobile_plans:
                print("Invalid input!")
                input("Press enter to continue...")
                continue
            print(f"Name: {self.mobile_plans[choice]['name']}")
            print(f"Price: {self.mobile_plans[choice]['price']} VND")
            print(f"Data: {self.mobile_plans[choice]['gb']} GB")
            print(f"Description: {self.mobile_plans[choice]['description']}")
            print()
            print("[1] Keep browsing")
            print("[else] Return to main menu")
            choice = input("Enter your choice: ")
            match choice:
                case "1": continue
                case _: break

    # DOMAIN MANAGEMENT

    def register_mobile_plan(self):
        # list all mobile plans
        print("\n== Mobile plans ==")
        for plan_id, plan in self.mobile_plans.items():
            print(f"[{plan_id}] {plan['name']} - {plan['price']} VND - {plan['gb']} GB")

        input_mobile_plan_id = input("Enter product ID to purchase (0 to cancel): ")
        while True:
            # get user input for mobile plan id

            # checks if input is a number, converts to int
            if not input_mobile_plan_id.isdigit(): # type: ignore (this comment is just for ignoring the error)
                print("Invalid input. Please try again.")
                continue
            input_mobile_plan_id = int(input_mobile_plan_id)

            # checks if user wants to cancel
            if input_mobile_plan_id == 0:
                print("Purchase cancelled.")
                return

            # check if entered mobile plan id is valid
            if input_mobile_plan_id not in self.mobile_plans:
                input_mobile_plan_id = input("Invalid product ID. Please try again: ")
                continue

            # checks if user has a current plan
            if self.logged_in_user.mobile_plan_id != 0:
                current_plan_name = self.mobile_plans[self.logged_in_user.mobile_plan_id]['name']
                choice = input(f"Your current plan is: {current_plan_name}. Do you want to change? (Y/n)")
                if choice == "n":
                    print("Purchase cancelled.")
                    return

            # checks if mobile_plan is valid
            if input_mobile_plan_id not in self.mobile_plans:
                print("Invalid product ID. Please try again.")
                continue

            # checks if user has sufficient balance
            if self.logged_in_user.balance < int(self.mobile_plans[input_mobile_plan_id]['price']):
                print("Insufficient balance.")
                return

            # updates user's product and balance
            self.logged_in_user.mobile_plan_id = input_mobile_plan_id
            self.logged_in_user.balance -= int(self.mobile_plans[input_mobile_plan_id]['price'])
            print("Purchase successful!")
            print(f"Your balance: {self.logged_in_user.balance} VND")
            # adds transaction to user's transaction history
            self.logged_in_user.transaction_history.append({
                "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "amount": int(self.mobile_plans[input_mobile_plan_id]['price']),
                "description": f"Purchase {self.mobile_plans[input_mobile_plan_id]['name']}"
            })
            return


    def transaction_history(self):
        print("\n== Transaction history ==")
        for transaction in self.logged_in_user.transaction_history:
            print(f"{transaction['date']} - {transaction['amount']} VND - {transaction['description']}")
    # COSMETIC

    def clear_screen(self):
        if os.name == "nt": # If the host OS is Windows
            os.system("cls")
        else:
            os.system("clear")

    # ============================================================
    #
    #      METHODS FOR CLI [ABOVE] THIS LINE - DO NOT MODIFY
    #
    # ============================================================

    # ==========================================
    #
    #      METHODS FOR GUI [BELOW] THIS LINE
    #
    # ==========================================

    def purchase_mobile_plan(self, mobile_plan_id):
        # checks if user has a current plan
        if self.logged_in_user.mobile_plan_id != 0:
            current_plan_name = self.mobile_plans[self.logged_in_user.mobile_plan_id]['name']
            choice = messagebox.askyesno("Bate", f"Your current plan is: {current_plan_name}. Do you want to change?")
            if not choice:
                messagebox.showinfo("Bate", "Purchase cancelled.")
                return

        # checks if user has sufficient balance
        if self.logged_in_user.balance < int(self.mobile_plans[mobile_plan_id]['price']):
            messagebox.showerror("Bate", f"Insufficient balance. Your balance: {self.logged_in_user.balance} VND")
            return

        # updates user's product and balance
        self.logged_in_user.mobile_plan_id = mobile_plan_id
        self.logged_in_user.balance -= int(self.mobile_plans[mobile_plan_id]['price'])
        messagebox.showinfo("Bate", "Purchase successful!")
        return

    def add_user(self, username, hashed_password):
        user = User()
        user.username = username
        user.password = hashed_password
        self.users.append(user)

    # ===========================================
    #
    #      METHODS FOR GUI [ABOVE] THIS LINE
    #
    # ===========================================