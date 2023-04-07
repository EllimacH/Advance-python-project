from domains.user import User
from domains.system import System
from domains.web import Web

class Admin(User):
    def __init__(self, system: System, web: Web):
        super().__init__()
        self.system: System = system
        self.web: Web = web

    def admin_menu(self):


        while True:
            self.system.flush_data_to_json()
            self.system.clear_screen()

            print(f"== Welcome {self.system.logged_in_user.username}! ==")
            print("[1] Check all users")
            print("[2] Delete user")
            print("[3] Delete user plan")
            print("[4] Change balance ")
            # print("[5] Add Domain")
            # print("[6] Remove Domain")
            print("[else] Go back")
            choice: str = input("\nEnter your choice: ")
            match choice:
                case "1": self.check_all_users()
                case "2": self.delete_user()
                case "3": self.delete_user_mobile_plan()
                case "4": self.change_balance()
                # case "5": self.add_domain()
                # case "6": self.remove_domain()
                case _: return
            input("\nPress Enter to continue...")

    def check_all_users(self) -> None:
        for user in self.system.users:
            print(f"Username: {user.username}, Balance: {user.balance}")

    def delete_user(self) -> None:
        username: str = input("Enter username account that you want to delete: ")
        for user in self.system.users:
            if user.username == username:
                confirm = input(f"Are you sure you want to delete {user.username} account? (y/N): ")
                if confirm.lower() != "y":
                    return
                self.system.users.remove(user)
                print("User deleted")
                break
        else:
            print("User not found")

    def delete_user_mobile_plan(self) -> None:
        username: str = input("Enter username that you want to delete mobile plan: ")
        for user in self.system.users:
            if user.username == username:
                user.mobile_plan_id = 0
                print("User plan deleted")
                break
        else:
            print("User not found")

    def change_balance(self) -> None:
        username: str = input("Enter username of the user whose balance you want to change: ")
        for user in self.system.users:
            if self.username == username:
                operation: str = input("Do you want to add or subtract from the balance? (+/-): ")
                amount: int = int(input("Enter the amount to add or subtract: "))
                if operation == "+":
                    user.balance += amount
                elif operation == "-":
                    user.balance -= amount
                    if user.balance < 0:
                        user.balance = 0
                else:
                    print("Invalid operation")
                    return
                print(f"Balance updated: {user.username}, New balance: {user.balance}")
                break
        else:
            print("User not found")

    # def add_domain(self) -> None:
    #     username: str = input("Enter username of the user whose domain you want to change: ")
    #     for user in self.system.users:
    #         if user.username == username:
    #             domain_name: str = input("Enter domain name: ")
    #             domain_ip: str = input("Enter domain IP: ")
    #             user.domain_name.append((domain_name, domain_ip)) # type: ignore
    #             print("Domain added")
    #             break
    #     else:
    #         print("User not found")

    # def remove_domain(self) -> None:
    #     username: str = input("Enter username of the user whose domain you want to change: ")
    #     for user in self.system.users:
    #         if user.username == username:
    #             domain_name: str = input("Enter domain name: ")
    #             domain_ip: str = input("Enter domain IP: ")
    #             user.domain_name.remove((domain_name, domain_ip)) # type: ignore
    #             print("Domain removed")
    #             break
    #     else:
    #         print("User not found")
