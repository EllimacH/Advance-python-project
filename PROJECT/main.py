from domains.system2 import System
from domains.web import Web

class Menu:
    def __init__(self, system: System, web: Web):
        self.system = system
        self.web = web

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
                    return self.system.sign_in()
                case "3":
                    print("Goodbye!")
                    raise KeyboardInterrupt
                case _:
                    print("Invalid choice! Please try again.")

    def is_signed_in(self) -> bool:
        while True:
            self.system.clear_screen()
            print(f"== Welcome {self.system.logged_in_user}! ==")
            print("1. Buy product")
            print("2. Check balance")
            print("3. Check current plan")
            print("4. Top-up")
            print("5. Sign out")
            print("6. Check product")
            print("7. Web domain service")

            choice = input("Enter your choice: ")
            match choice:
                case "1": self.system.buy_product()
                case "2": self.system.check_balance()
                case "3": self.system.check_plan()
                case "4": self.system.top_up()
                case "5": return self.system.sign_out()
                case "6": self.system.check_product()
                case "7": self.web.web_domain_services(system = self.system)
                case _:
                    print("Invalid choice! Please try again.")
            input("Press Enter to continue...")



def main():
    # create an instance of the System class
    system = System()
    web = Web()
    menu = Menu(system, web)
    is_logged_in = False

    while True:
        system.flush_data_to_json()
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