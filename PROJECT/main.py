from domains.system import System
from domains.web import Web
from domains.admin import Admin
class Menu:
    def __init__(self, web: Web , admin: Admin):
        self.web = web
        self.system = web.system
        self.admin = admin

    def is_not_logged_in(self) -> bool:
        """Return True if user is logged in, False otherwise"""
        while True:

            self.system.clear_screen()
            print("== Internet Service Provider (B.A.T.E) ==")
            print("[1] Sign-up")
            print("[2] Log-in")
            print("[else] Exit")
            choice = input("Enter your choice: ")
            match choice:
                case "1": self.system.create_account()
                case "2": return self.system.log_in()
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
            print("-"*10)
            print("[5] Top-up")
            print("[6] Web domain service")
            print("-"*10)
            print("[7] Log-out")
            if self.admin.is_admin(): # check if the current user is an admin
                print("[8] Admin menu") # show an extra option for the admin to interact with the database

            choice = input("Enter your choice: ")
            match choice:
                case "1": self.system.check_balance()
                case "2": self.system.list_mobile_plans()
                case "3": self.system.register_mobile_plan()
                case "4": self.system.check_current_plan()
                case "5": self.system.top_up()
                case "6": self.web.web_domain_service_menu()
                case "7": return self.system.log_out() # Here's the exit point of this method's loop. `log_out()` return False, assign to `is_logged_in` in `main()` function to get back to `is_not_logged_in()` menu.
                case "8": 
                    if self.admin.is_admin(): # only allow the admin to access this option
                        self.admin.admin_menu()
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
    # Reasons why we need to pass System object to Web object:
    # - for VPN/VPS service, each user is independent, only need the "current logged in user" to modify their data
    # - for Domain service, each user has a distinct domain name, we need to have a function-can-access-all-users-data to check if the domain name is already taken or not
    # - on another side, the "current logged in user" is already in the System object for us to manage VPN/VPS infos anyway
    admin = Admin(system, web)
    # Split the main menu into 2 parts:
    # - Not signed in (create account, sign in, exit)
    # - Signed in (everything else)
    # Originally, we have to pass both System and Web object to the Menu object, but we can just pass Web object, because Web object already contains System object
    menu = Menu(web,admin)
    is_logged_in = False

    while True:
        # Flush user data to json file when ever return to login/signup menu
        system.flush_data_to_json()

        if is_logged_in:
            is_logged_in = menu.is_signed_in()
        else:
            is_logged_in = menu.is_not_logged_in()

        input("\nPress Enter to continue...")

    #create admin account

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        exit()