from domains.system import System
from domains.web import Web
from domains.admin import AdminCLI

class Menu:
    def __init__(self, system: System, web: Web, admin: AdminCLI):
        self.web = web # access web domain service menu
        self.system = system # access all accounts data
        self.admin = admin # access admin menu

    def is_not_logged_in(self) -> bool:
        """Return True if user is logged in, False otherwise"""

        is_first_account = False
        if len(self.system.users) == 0:
            is_first_account = True

        while True:
            self.system.clear_screen()
            print("== Internet Service Provider (B.A.T.E) ==")
            print("[1] Sign-up")
            print("[2] Log-in")
            print("[else] Exit")
            if is_first_account:
                print("-"*10)
                print("There is no account in the system, this first account will be an admin account")
            choice = input("\nEnter your choice: ")
            match choice:
                case "1": self.system.create_account()
                case "2": return self.system.log_in() # Return True if logged-in successfully to go to `is_signed_in()` menu, False otherwise to stay in this menu.
                case _: raise KeyboardInterrupt
            return False

    def is_signed_in(self) -> bool:
        """Return True if user is logged in, False otherwise"""
        while True:
            # Flush user data to json file when ever return to main menu
            self.system.flush_data_to_json()
            self.system.clear_screen()
            print(f"== Welcome {self.system.logged_in_user.username}! ==") # self.system.users contains list of User objects, after signing in, that user object is assigned to self.system.logged_in_user, so we can access its attributes conveniently, like the `username` here.
            print("[1] Check your balance")
            print("[2] Find more about our mobile plans")
            print("[3] Register a mobile plan")
            print("[4] Check your current plan")
            print("[5] Top-up")
            print("-"*10)
            print("[6] Web domain service menu")
            print("-"*10)
            print("[7] Log-out")
            print("[8]: Transaction history")
            if self.system.logged_in_user.is_admin:
                print("[*] Admin menu")

            choice = input("Enter your choice: ")
            match choice:
                case "1": self.system.check_balance()
                case "2": self.system.list_mobile_plans()
                case "3": self.system.register_mobile_plan()
                case "4": self.system.check_current_plan()
                case "5": self.system.top_up()
                case "6": self.web.web_domain_service_menu()
                case "7": return self.system.log_out() # Here's the exit point of this method's loop. `log_out()` return False, assign to `is_logged_in` in `main()` function to get back to `is_not_logged_in()` menu.
                case "8": self.system.transaction_history()
                case "*":
                    if self.system.logged_in_user.is_admin:
                        self.admin.admin_menu()
                    else:
                        print("Invalid choice! Please try again.")
                case _: print("Invalid choice! Please try again.")

            input("\nPress Enter to continue...")


def main():
    # System object:
    # - Containing all users data
    # - Managing login, logout, create account,...
    # - Managing a mobile data plan
    system = System()

    # Web object:
    # - VPN service
    # - VPS service
    # - Domain service
    web = Web(system)

    admin = AdminCLI(system, web)
    menu = Menu(system, web, admin)

    is_logged_in = False
    while True:
        # Flush user data to json file when ever return to login/signup menu
        system.flush_data_to_json()

        if is_logged_in:
            is_logged_in = menu.is_signed_in()
        else:
            is_logged_in = menu.is_not_logged_in()

        input("\nPress Enter to continue...")

    # create admin account


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        exit()
