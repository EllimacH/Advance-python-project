import time
import re
from os import system, name
import os
from domains.user import User


class Web:
    def __init__(self):
        self.domain_list = []
        self.service = None
        self.vpn_package = None

    # Register a new domain and IP address
    def setDomain(self, user):
        print("")
        print("1. Register a new domain")
        print("2. Back to main menu")
        choose = int(input("Enter your choice: "))
        if choose == 1:
            print("The price for a domain is 100.000VNĐ.")
            confirm = input("Do you want to proceed? (Y/N) ")
            if confirm == "Y" or confirm == "y":
                # Check if user has enough money to buy a domain
                if user.balance < 100000:
                    print("You do not have enough money to buy a domain.")
                else:
                    user.balance -= 100000
                    user.current_domain = domain_input
                    print("You have successfully bought a domain.")
                    print("Your balance is now: ", user.balance)
                    print("Please enter the domain name you want to register.")
                    print("How to type your domain: a-z, 0-9, - (a-z, 0-9, - are characters) \n For example: your-domain")
                    domain_input = input("Type your domain: ")
                    while True:
                        if re.match(r'^[a-z0-9-]+$', domain_input):
                            break
                        else:
                            print("Invalid domain name. Please try again.")
                            domain_input = input("Type your domain: ")
                    print("How to type your IP address: a.b.c.d (a, b, c, d are numbers from 0 to 255)")
                    ip_input = input("Type your IP address: ")
                    while True:
                        if re.match(
                                r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
                                ip_input):
                            break
                        else:
                            print("Invalid IP address")
                            ip_input = input("Type your IP address: ")
                    password = input("Set a password to protect your domain: ")
                    while True:
                        if password == "":
                            print("You have not entered a password")
                            password = input("Set a password to protect your domain: ")
                        else:
                            break
                    self.domain_list.append([domain_input, ip_input, password])
                    print("You have successfully registered a new domain.")
                    print("Your domain list: ", self.domain_list)
                    time.sleep(2)
                    print("")
                    input("Press Enter to continue...")
            else:
                print("You have cancelled the domain registration.")
                time.sleep(2)
                print("")
                input("Press Enter to continue...")
        elif choose == 2:
            #return to domain menu
            pass
        else:
            print("Invalid choice. Please try again.")
            time.sleep(2)
            print("")
            input("Press Enter to continue...")

        #             print(f" == Domain == ")
        #             print("By default, your domain will be: www.yourdomain.com")
        #             print("How to make your own domain: a-z, 0-9, - (a-z, 0-9, - are characters) \n For example: your-domain")
        #             domain_input = input("Make a unique domain of your own: ")
        #             while True:
        #                 if domain_input == "":
        #                     print("You have not entered a domain")
        #                     domain_input = input("Make a unique domain of your own: ")
        #                 else:
        #                     break

        #     print("How to type your IP address: a.b.c.d (a, b, c, d are numbers from 0 to 255)")
        #     ip_input = input("Type your IP address: ")
        #     while True:
        #         if re.match(
        #                 r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip_input):
        #             break
        #         else:
        #             print("Invalid IP address")
        #             ip_input = input("Type your IP address: ")

        #     password = input("Set a password to protect your domain: ")
        #     while True:
        #         if password == "":
        #             print("You have not entered a password")
        #             password = input("Set a password to protect your domain: ")
        #         else:
        #             break

        #     print("Checking your domain...")
        #     time.sleep(1)
        #     print("Domain is valid")
        #     print("Checking your IP address...")
        #     time.sleep(1)
        #     print("IP address is valid")
        #     print("Saving your information...")
        #     time.sleep(1)
        #     print("Your domain has been registered successfully")

        #     self.domain_list += [{"Domain": domain_input,
        #                           "IP": ip_input,
        #                           "Password": password}]
        #     time.sleep(1)
        #     print("")
        #     input("Press Enter to continue...")
        # else:
        #     print("")
        #     input("Press Enter to continue...")

    # Choose and buy a service package

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
                case 1:
                    self.service = "Basic Package"
                case 2:
                    self.service = "Advanced Package"
                case 3:
                    self.service = "High End Package"
                case 4:
                    self.service = "VIP Package"
                case 5:
                    self.service = "VIP+ Package"
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
                case 1:
                    self.setDomain("Domain")
                case 2:
                    self.buy_service()
                case 3:
                    self.domain_info()
                case 4:
                    self.vpn()
                case 5:
                    self.vpn_info()
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
            
#write def buy_domain() using balance from class User 

    def buy_domain(self):
        print("")
        print("1. Buy a domain")
        print("2. Back to main menu")
        choose = int(input("Enter your choice: "))
        if choose == 1:
            print("The price for a domain is 100.000VNĐ.")
            confirm = input("Do you want to proceed? (Y/N) ")
            if confirm == "Y":
                if self.balance < 100000:
                    print("You do not have enough money to buy a domain.")
                else:
                    self.balance -= 100000
                    self.setDomain()
            else:
                print("Transaction canceled.")
        else:
            print("")
            input("Press Enter to continue...")

