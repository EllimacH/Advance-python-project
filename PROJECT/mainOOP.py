import os
import time
import hashlib
from datetime import datetime
from domains.system import System
from domains.web import Web

#array thingy
users = []

def main():
    # create an instance of the System class
    system = System()
    web = Web()
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
            print("7. Web domain services")
            choice = input("Enter your choice: ")
            if choice == "1":
                system.clear_screen()
                system.buy_product(user)
                input("Press Enter to continue...")
                system.clear_screen()
            elif choice == "2":
                system.clear_screen()
                system.check_balance(user)
                input("Press Enter to continue...")
                system.clear_screen()
            elif choice == "3":
                system.clear_screen()
                system.check_plan(user)
                input("Press Enter to continue...")
                system.clear_screen()
            elif choice == "4":
                system.clear_screen()
                system.top_up(user)
                input("Press Enter to continue...")
                system.clear_screen()
            elif choice == "5":
                user = system.sign_out()
            elif choice == "6":
                system.clear_screen()
                system.check_product()
                input("Press Enter to continue...")
                system.clear_screen()
            elif choice == "7":
                system.clear_screen()
                print("")
                print(" == Main Menu == ")
                print("1. Buy Domain")
                print("2. Buy Service")
                print("3. Check Domain Info")
                print("4. Buy VPN")
                print("5. Check VPN Info")
                choose = int(input("Choose your option: "))
                system.clear_screen()
                match choose:
                    case 1:
                        web.setDomain("Domain")
                    case 2:
                        web.buy_service()
                    case 3:
                        web.domain_info()
                    case 4:
                        web.vpn()
                    case 5:
                        web.vpn_info()
                    case _:
                        print("You have not entered a valid option")
                        system.clear_screen()
                        choose = int(input("Choose your option: "))
                system.clear_screen()
            else:
                print("Invalid choice! Please try again.")
                system.clear_screen()
        else:
            print("1. Create account")
            print("2. Sign in")
            print("3. Exit")
            choice = input("Enter your choice: ")
            system.clear_screen()
            if choice == "1":
                system.create_account()
            elif choice == "2":
                user = system.sign_in()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

# sign in process: access user through users list and check if the password is correct
# check balance test: access user object through users list 
# change to only using txt files as saving data, access temporary data through memory 
