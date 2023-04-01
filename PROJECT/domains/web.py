import time
import re
from os import system, name
import os
from domains.user import User
from domains.system2 import System

class Web:
    """Managing web, domain and VPN services"""

    def __init__(self):
        self.domain_list = []
        self.service = None
        self.vpn_package = None

    # Register a new domain and IP address
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
                domain_input = input("Make a unique domain of your own: ")
                while True:
                    domain_is_valid = re.match(r"^(?=.{1,255}$)[a-zA-Z0-9](?:(?:[a-zA-Z0-9\-]){0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z]{2,})+$", domain_input)
                    domain_is_available = system.is_domain_name_available(domain_input)

                    if domain_is_valid and domain_is_available:
                        break
                    domain_input = input("Domain is invalid or already taken. Press Enter to try again...")

                user.domain_name = domain_input
                user.domain_ip = system.get_random_ip()
                user.balance -= 200000

                

            case "2": return True
            case _: return False

    def buy_service(self):
        print("")
        print("1. Buy a service package")
        print("2. Back to main menu")
        choose = int(input("Enter your choice: "))
        if choose == 1:
            print("")
            print(" == Service Packages == ")
            print("1. Basic: 200.000đ/year")
            print("2. Advanced: 350.000đ/2 years")
            print("3. High End: 500.000đ/3 years")
            print("4. VIP: 800.000đ/5 years")
            print("5. VIP+: 1.850.000đ/10 years")
            choose_service = int(input("Choose your package: "))
            match choose_service:
                case 1: self.service = "Basic Package"
                case 2: self.service = "Advanced Package"
                case 3: self.service = "High End Package"
                case 4: self.service = "VIP Package"
                case 5: self.service = "VIP+ Package"
                case _:
                    print("You have not entered a valid package")
                    choose_service = int(input("Choose your package: "))

            print("Payment is in progress, please wait...")
            time.sleep(1)
            print("")
            print("Payment Completed")
            print(f"You have purchased {self.service}")
            print("")
            input("Press Enter to continue...")
        else:
            print("")
            input("Press Enter to continue...")

    # Check domain info

    def domain_info(self):
        print("")
        print(" == Domain Info == ")
        password_input = input("Enter your domain password: ")
        while True:
            for domain in self.domain_list:
                if password_input == domain["Password"]:
                    print(f"Your domain:  + www.{domain['Domain']}.com")
                    print("IP: " + domain["IP"])
                    print(f"Service: {self.service}")
                    if self.service == None:
                        print("Status: Offline")
                    else:
                        print("Status: Online")
                    print("")
                    input("Press Enter to continue...")
                    break
            else:
                print("Wrong password/You have not registered a domain")
                print("Do you want to try again?")
                print("1. Yes")
                print("2. No")
                choose = int(input("Enter your choice: "))
                if choose == 1:
                    password_input = input("Enter your domain password: ")
                    continue
                else:
                    print("")
                    input("Press Enter to continue...")
                    break
            break

    # Buy VPN

    def vpn(self):
        print("")
        print("1. Buy a VPN package")
        print("2. Back to main menu")
        choose = int(input("Enter your choice: "))
        if choose == 1:
            print(" == VPN Packages == ")
            print("1. Basic: 100.000đ/year")
            print("2. Advanced: 150.000đ/2 years")
            print("3. High End: 200.000đ/3 years")
            print("4. VIP: 300.000đ/5 years")
            print("5. VIP+: 500.000đ/10 years")
            choose_vpn = int(input("Choose your package: "))
            match choose_vpn:
                case 1:
                    self.vpn_package = "Basic Package"
                case 2:
                    self.vpn_package = "Advanced Package"
                case 3:
                    self.vpn_package = "High End Package"
                case 4:
                    self.vpn_package = "VIP Package"
                case 5:
                    self.vpn_package = "VIP+ Package"
                case _:
                    print("You have not entered a valid package")
                    choose_vpn = int(input("Choose your package: "))

            print("Payment is in progress, please wait...")
            time.sleep(1)
            print("")
            print("Payment Completed")
            print(f"You have purchased {self.vpn_package}")
            print("")
            input("Press Enter to continue...")
        else:
            print("")
            input("Press Enter to continue...")

    # Display VPN info

    def vpn_info(self):
        print(f"VPN Package: {self.vpn_package}")
        while True:
            if self.vpn_package == None:
                print("Status: Offline")
                break
            else:
                print("Status: Online")
            break
        print("")
        input("Press Enter to continue...")

    def clear(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def web_domain_services(self):
        while True:
            print("")
            print(" == Main Menu == ")
            print("1. Buy Domain")
            print("2. Buy Service")
            print("3. Check Domain Info")
            print("4. Buy VPN")
            print("5. Check VPN Info")
            print("6. Exit")
            choose = int(input("Choose your option: "))
            self.clear()
            match choose:
                case 1: self.set_domain("Domain")
                case 2: self.buy_service()
                case 3: self.domain_info()
                case 4: self.vpn()
                case 5: self.vpn_info()
                case 6:
                    print("Exiting...")
                    time.sleep(1)
                    print(" Have a nice day!")
                    break
                case _:
                    print("You have not entered a valid option")
                    self.clear()
                    choose = int(input("Choose your option: "))

    # def buy_domain():
    #     print("")
    #     print("1. Buy a domain")
    #     print("2. Back to main menu")
    #     choose = int(input("Enter your choice: "))
    #     if choose == 1:
    #         print("The price for a domain is 100.000VNĐ.")
    #         confirm = input("Do you want to proceed? (Y/N) ")
    #         if confirm == "Y":
    #             if self.balance < 100000:
    #                 print("You do not have enough money to buy a domain.")
    #             else:
    #                 self.balance -= 100000
    #                 self.setDomain()
    #         else:
    #             print("Transaction canceled.")
    #     else:
    #         print("")
    #         input("Press Enter to continue...")

# write def buy_domain() using balance from class User
