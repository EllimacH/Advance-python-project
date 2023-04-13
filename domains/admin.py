from domains.user import User
from domains.system import System
from domains.web import Web

class AdminCLI(User):
    """Admin class for the command line interface, DO NOT MODIFY THIS CLASS"""
    def __init__(self, system: System, web: Web):
        super().__init__()
        self.system: System = system
        self.web: Web = web
        self.user = system.logged_in_user

    def admin_menu(self):
        while True:
            self.system.flush_data_to_json()
            self.system.clear_screen()

            print(f"== Welcome {self.system.logged_in_user.username}! ==")
            print("[1] Check all users")
            print("[2] Delete user")
            print("[3] Delete mobile plan from a user")
            print("[4] Change balance of a user")
            print("[5] Modify domain of a user")
            print("[6] Remove domain from a user")
            print("[7] Add a mobile plan")
            print("[8] Remove a mobile plan")
            print("[else] Go back")
            choice: str = input("\nEnter your choice: ")
            match choice:
                case "1": self.check_all_users()
                case "2": self.delete_user()
                case "3": self.delete_user_mobile_plan()
                case "4": self.change_balance()
                case "5": self.add_domain()
                case "6": self.remove_domain()
                case "7": self.add_mobile_plan()
                case "8": self.remove_mobile_plan()
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
        selected_user: User = User() # blank placeholder

        # find the user
        for user in self.system.users:
            if user.username == username:
                selected_user = user
                break
        else:
            print("User not found")
            return

        # change the balance
        operation: str = input("Do you want to add or subtract from the balance? (+/-): ")
        match operation:
            case "+":
                amount: int = int(input("Enter the amount to add: "))
                selected_user.balance += amount
            case "-":
                amount: int = int(input("Enter the amount to subtract: "))
                selected_user.balance -= amount
            case _: print("Invalid operation")

    def add_domain(self) -> None:
        username: str = input("Enter username of the user whose domain you want to change: ")
        for user in self.system.users:
            if user.username == username:
                domain_name: str = input("Enter domain name: ")
                domain_ip: str = input("Enter domain IP: ")
                print("Domain added")
                break
        else:
            print("User not found")

    def remove_domain(self) -> None:
        username: str = input("Enter username of the user whose domain you want to remove: ")
        for user in self.system.users:
            if user.username == username:
                user.domain_name = ""
                user.domain_ip = ""

    def add_mobile_plan(self) -> None:
        id: int = int(input("Enter plan id: "))
        name: str = input("Enter plan name: ")
        price: int = int(input("Enter plan price: "))
        data: int = int(input("Enter plan data: "))
        description: str = input("Enter plan description: ")
        self.system.mobile_plans[id] = {
            "name": name,
            "price": price,
            "gb": data,
            "description": description
        }
        print("Plan added")

    def remove_mobile_plan(self) -> None:
        plan_id: int = int(input("Enter plan id : "))
        for key, plan in self.system.mobile_plans.items():
            if key == plan_id:
                confirm = input(f"Are you sure you want to delete {plan['name']} plan? (y/N): ")
                if confirm.lower() != "y":
                    return
                del self.system.mobile_plans[key]
                print("plan deleted")
                break
        else:
            print("plan not found")

class AdminGUI(User):
    def __init__(self, system: System) -> None:
        self.system = system
    # def remove_vpn_package(self) -> None:
    #     package_id: str = input("Enter the package id : ")
    #     for package in self.web.vpn_packages:
    #         if package[0] == package_id:
    #             confirm = input(f"Are you sure you want to delete {package[1]} vpn package? (y/N): ")
    #             if confirm.lower() != "y":
    #                 return
    #             self.web.vpn_packages.remove(package)
    #             print("VPN package deleted")
    #             break
    #     else:
    #         print("VPN package not found")

    # def add_vpn_package(self) -> None:
    #     vpn_package_name: str = input("Enter package name: ")
    #     vpn_package_price: int = int(input("Enter package price: "))
    #     self.web.vpn_packages.append((vpn_package_name, vpn_package_price))
    #     print("VPN package added")

    # def add_vps_package(self) -> None:
    #     vps_package_name: str = input("Enter package name: ")
    #     vps_package_price: int = int(input("Enter package price: "))
    #     vps_package_description: str = input("Enter package description: ")
    #     self.web.vps_packages.append((vps_package_name, vps_package_price, vps_package_description))
    #     print("VPS package added")

    # def remove_vps_package(self) -> None:
    #     vps_package_id: str = input("Enter vps packages id : ")
    #     for package in self.web.vps_packages:
    #         if package[0] == vps_package_id:
    #             confirm = input(f"Are you sure you want to delete {package[1]} vps package? (y/N): ")
    #             if confirm.lower() != "y":
    #                 return
    #             self.web.vps_packages.remove(package)
    #             print("VPS Package deleted")
    #             break
    #     else:
    #         print("VPS Package not found")