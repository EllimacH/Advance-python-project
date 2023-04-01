import os
import time
import hashlib
from datetime import datetime
from domains.system2 import System
from domains.web import Web
from domains.user import User


class Menu:
    def __init__(self, system: System, web: Web):
        self.system = system
        self.web = web
        self.username = ""

    def is_not_signed_in(self) -> bool:
        while True:
            self.system.clear_screen()
            print("== Internet Service Provider (B.A.T.E) ==")
            print("1. Create account")
            print("2. Sign in")
            print("3. Exit")
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    self.system.create_account()
                    return False
                case "2":
                    self.username = self.system.sign_in()
                    return True if (self.username != "") else False
                case "3":
                    print("Goodbye!")
                    raise KeyboardInterrupt
                case _:
                    print("Invalid choice! Please try again.")

    def is_signed_in(self) -> bool:
        while True:
            self.system.clear_screen()
            print(f"== Welcome {self.username}! ==")
            print("1. Buy product")
            print("2. Check balance")
            print("3. Check current plan")
            print("4. Top-up")
            print("5. Sign out")
            print("6. Check product")
            print("7. Web domain service")

            choice = input("Enter your choice: ")
            match choice:
                case "1": self.system.buy_product(self.username)
                case "2": self.system.check_balance(self.username)
                case "3": self.system.check_plan(self.username)
                case "4": self.system.top_up(self.username)
                case "5": return self.system.sign_out()
                case "6": self.system.check_product()
                case "7":
                    self.system.clear_screen()
                    print("== Main Menu ==")
                    print("1. Buy Domain")
                    print("2. Buy Service")
                    print("3. Check Domain Info")
                    print("4. Buy VPN")
                    print("5. Check VPN Info")
                    print("6. Return to main menu")
                    while True:
                        try:
                            choose = int(input("Choose your option: "))
                            break
                        except ValueError:
                            print("Invalid input! Please enter a valid integer.")
                    self.system.clear_screen()
                    match choose:
                        case 1:
                            user_object = self.system.get_user_object(self.username)
                            self.web.buy_domain(user_object, self.system)
                        case 2: self.web.buy_service()
                        case 3: self.web.domain_info()
                        case 4: self.web.vpn()
                        case 5: self.web.vpn_info()
                        case 6: return True
                        case _:
                            print("You have not entered a valid option")
                            self.system.clear_screen()
                            choose = int(input("Choose your option: "))
                    self.system.clear_screen()
                # else:
                case _:
                    print("Invalid choice! Please try again.")
                    self.system.clear_screen()

            input("Press Enter to continue...")



def main():
    # create an instance of the System class
    system = System()
    web = Web()
    menu = Menu(system, web)
    is_logged_in = False

    while True:
        if is_logged_in:
            is_logged_in = menu.is_signed_in()
        else:
            is_logged_in = menu.is_not_signed_in()

    

if __name__ == "__main__":
    # main()
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        exit()