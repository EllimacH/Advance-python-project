from domains.user import User
from domains.system import System
from domains.web import Web

class Admin(User):
    def __init__(self, system: System, web: Web):
        super().__init__()
        self.system: System = system
        self.web: Web = web
        

    def admin_menu(self) -> bool:
        while True:
            self.system.clear_screen()
            print(f"== Welcome {self.system.logged_in_user.username}! ==")
            print("[1] Check all users")
            print("[2] Delete user")
            print("[3] Delete user plan")
            print("[4] Log-out")
            choice: str = input("Enter your choice: ")
            match choice:
                case "1":
                    self.check_all_users()
                case "2":
                    self.delete_user()
                case "3":
                    self.delete_user_mobile_plan()
                case "4":
                    return self.system.log_out()
                case _:
                    print("Invalid choice! Please try again.")
            input("\nPress Enter to continue...")

    def check_all_users(self) -> None:
        for user in self.system.users:
            print(f"Username: {user.username}, Balance: {user.balance}")

    def delete_user(self) -> None:
        username: str = input("Enter username account that you want to delete: ")
        for user in self.system.users:
            if user.username == username:
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
