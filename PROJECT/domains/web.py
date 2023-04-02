import time
import re
# from os import system, name
import os
from domains.user import User
from domains.system2 import System


class Web:
    """Managing web, domain and VPN services"""

    def __init__(self):
        self.vps_packages = {
            1: {"name": "Basic", "price": 200000},
            2: {"name": "Advanced", "price": 350000},
            3: {"name": "High End", "price": 500000},
            4: {"name": "VIP", "price": 800000},
            5: {"name": "VIP+", "price": 1850000}
        }
        self.selected_vps_plan: int = 0

        self.vpn_packages = {
            1: {"name": "Basic", "price": 100000},
            2: {"name": "Advanced", "price": 150000},
            3: {"name": "High End", "price": 200000},
            4: {"name": "VIP", "price": 300000},
            5: {"name": "VIP+", "price": 500000}
        }
        self.selected_vpn_plan: int = 0

    def buy_domain(self, user: User, system: System) -> bool:
        """Register a new domain and IP address, return True if success, False otherwise"""
        if user.balance < 200000:
            print("You must have at least 200.000 VND to buy a domain")
            return False

        print("1. Register a new domain (200.000 VND)")
        print("2. Back to main menu")
        choose = input("Enter your choice: ")
        match choose:
            case "1":
                domain_input = input("Make a unique domain of your own: ( mydomain.com) ")
                while True:
                    domain_is_valid = re.match(r"^(?=.{1,255}$)[a-zA-Z0-9](?:(?:[a-zA-Z0-9\-]){0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z]{2,})+$", domain_input)
                    domain_is_available = system.is_domain_name_available(domain_input)

                    if domain_is_valid and domain_is_available:
                        break
                    domain_input = input("Domain is invalid or already taken. Please input a new one:")

                user.domain_name = domain_input
                user.domain_ip = system.get_random_ip()
                user.balance -= 200000
                print("Domain registered successfully!")
                return True
            case "2": return False
            case _: return False

    def buy_vps(self, user: User, system: System) -> bool:
        """Buy a service package, return True if success, False otherwise"""
        print("")
        print("1. Buy a service package")
        print("2. Back to main menu")
        choose = int(input("Enter your choice: "))
        if choose == 1:
            print(" == VPS tier list == ")
            for id, package in self.vps_packages.items():
                print(f"{id}. {package['name']} ({package['price']} VND)")
            print("else. Back to main menu")

            choice = input("Choose your package: ")
            match choice:
                case "1":
                    # NOTE: splitting this into multiple lines to make it more readable
                    if user.balance < int(self.vps_packages[int(choice)]['price']):
                        print(f"You must have at least {self.vps_packages[int(choice)]['price']} VND to buy the {self.vps_packages[int(choice)]['name']} package")
                        return False
                    user.balance -= int(self.vps_packages[int(choice)]['price'])
                    self.selected_vps_package = int(choice)
                    print(f"You have purchased {self.vps_packages[self.selected_vps_package]['name']} package")
                    return True
                case "2":
                    if user.balance < int(self.vps_packages[int(choice)]['price']):
                        print("You must have at least 350.000 VND to buy the advanced package")
                        return False
                    user.balance -= int(self.vps_packages[int(choice)]['price'])
                    self.selected_vps_package = int(choice)
                    print(f"You have purchased {self.vps_packages[self.selected_vps_package]['name']} package")
                    return True
                case "3":
                    if user.balance < int(self.vps_packages[int(choice)]['price']):
                        print("You must have at least 500.000 VND to buy the high end package")
                        return False
                    user.balance -= int(self.vps_packages[int(choice)]['price'])
                    self.selected_vps_package = int(choice)
                    print(f"You have purchased {self.vps_packages[self.selected_vps_package]['name']} package")
                case "4":
                    if user.balance < int(self.vps_packages[int(choice)]['price']):
                        print("You must have at least 800.000 VND to buy the VIP package")
                        return False
                    user.balance -= int(self.vps_packages[int(choice)]['price'])
                    self.selected_vps_package = int(choice)
                    print(f"You have purchased {self.vps_packages[self.selected_vps_package]['name']} package")
                    return True
                case "5":
                    if user.balance < int(self.vps_packages[int(choice)]['price']):
                        print("You must have at least 1.850.000 VND to buy the VIP+ package")
                        return False
                    user.balance -= int(self.vps_packages[int(choice)]['price'])
                    self.selected_vps_package = int(choice)
                    print(f"You have purchased {self.vps_packages[self.selected_vps_package]['name']} package")
                    return True
                case "6":
                    pass
                case _:
                    return False
            print("Payment is in progress, please wait...")
            time.sleep(1)
            print("")
            print("Payment Completed")
            print(f"You have purchased {self.vps_packages[self.selected_vps_package]['name']} package")
            return True
        else:
            return False

    # Check domain info

    def domain_info(self, system: System):
        domain_name = system.logged_in_user.domain_name
        domain_ip = system.logged_in_user.domain_ip
        print(f"Domain name: {domain_name}")
        print(f"Domain IP: {domain_ip}")

    # Buy VPN

    def buy_vpn(self, system: System) -> bool:

        balance = system.logged_in_user.balance
        system.logged_in_user.current_vpn_plan

        print("")
        print("1. Buy a VPN package")
        print("2. Back to main menu")
        choose = int(input("Enter your choice: "))
        if choose == 1:
            print(" == VPN tier list == ")
            for id, package in self.vpn_packages.items():
                print(f"{id}. {package['name']} ({package['price']} VND)")
            print("else. Back to main menu")

            choice = input("Choose your package: ")
            match choice:
                case "1":
                    # NOTE: splitting this into multiple lines to make it more readable
                    if balance < int(self.vpn_packages[int(choice)]['price']):
                        print(f"You must have at least {self.vpn_packages[int(choice)]['price']} VND to buy the {self.vpn_packages[int(choice)]['name']} package")
                        return False
                    balance -= int(self.vpn_packages[int(choice)]['price'])
                    system.logged_in_user.current_vpn_plan = int(choice)

                case "2":
                    if balance < int(self.vpn_packages[int(choice)]['price']):
                        print("You must have at least 350.000 VND to buy the advanced package")
                        return False
                    balance -= int(self.vpn_packages[int(choice)]['price'])
                    system.logged_in_user.current_vpn_plan = int(choice)

                case "3":
                    if balance < int(self.vpn_packages[int(choice)]['price']):
                        print("You must have at least 500.000 VND to buy the high end package")
                        return False
                    balance -= int(self.vpn_packages[int(choice)]['price'])
                    system.logged_in_user.current_vpn_plan = int(choice)

                case "4":
                    if balance < int(self.vpn_packages[int(choice)]['price']):
                        print("You must have at least 800.000 VND to buy the VIP package")
                        return False
                    balance -= int(self.vpn_packages[int(choice)]['price'])
                    system.logged_in_user.current_vpn_plan = int(choice)

                case "5":
                    if balance < int(self.vpn_packages[int(choice)]['price']):
                        print("You must have at least 1.850.000 VND to buy the VIP+ package")
                        return False
                    balance -= int(self.vpn_packages[int(choice)]['price'])

                case "6":
                    pass
                case _:
                    return False
            print(f"you have purchased {self.vpn_packages[system.logged_in_user.current_vpn_plan]['name']} package")
            return True
    # Display VPN info

    def vpn_info(self, system: System):
        vpn_id = system.logged_in_user.current_vpn_plan
        selected_vpn = self.vpn_packages[vpn_id]
        print(f"Your VPN: {selected_vpn['name']}")
        print(f"Price: {selected_vpn['price']} VND")

    def clear(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def web_domain_services(self, system: System):
        while True:
            print("")
            print(" == Web services menu == ")
            print("1. Buy Domain")
            print("2. Buy VPS")
            print("3. Check Domain Info")
            print("4. Buy VPN")
            print("5. Check VPN Info")
            print("6. Exit")
            choose = input("Choose your option: ")
            self.clear()
            match choose:
                # case with "" is turning case into a string
                case "1": self.buy_domain(system=system, user=system.logged_in_user)
                case "2": self.buy_vps(system=system, user=system.logged_in_user)
                case "3": self.domain_info(system=system)
                case "4": self.buy_vpn(system=system)
                case "5": self.vpn_info(system=system)
                case "6":
                    # return to main menu in main.py
                    return True
                case _:
                    print("You have not entered a valid option")
                    self.clear()
                    choose = input("Choose your option: ")
