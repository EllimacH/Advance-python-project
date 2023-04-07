from domains.system import System
from domains.web import Web
from domains.admin import Admin
from domains.menu import Menu


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

    admin = Admin(system, web)
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
