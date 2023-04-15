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
            print("-"*10)
            print("[3] Delete mobile plan from a user")
            print("[4] Change balance of a user")
            print("-"*10)
            print("[5] Remove domain from a user")
            print("[6] Modify plans (add/remove/edit a plan)")
            print("-"*10)
            print("[else] Go back")
            choice: str = input("\nEnter your choice: ")
            match choice:
                case "1": self.check_all_users_info()
                case "2": self.delete_user()
                case "3": self.delete_user_mobile_plan()
                case "4": self.change_balance()
                case "5": self.remove_domain()
                case "6": self.modify_plan()
                case _: return
            input("\nPress Enter to continue...")


    def check_all_users_info(self) -> None:
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
                print("Balance changed")
            case "-":
                amount: int = int(input("Enter the amount to subtract: "))
                selected_user.balance -= amount
                print("Balance changed")
            case _: print("Invalid operation")



    def remove_domain(self) -> None:
        username: str = input("Enter username of the user whose domain you want to remove: ")
        for del_user in self.system.users:
            if del_user.username == username:
                confirm = input(f"Are you sure you want to delete {del_user.username}'s domain? (y/N): ")
                if confirm.upper() != "N":
                    return
                del_user.domain_name = ""
                print("Domain deleted")
                break



    def modify_plan(self) -> None:
        print(" ==Modify plan== ")
        mod_id = input("[1] Edit plan\n[2] Remove plan\n[else] Return to menu\nEnter your choice: ")
        if mod_id == "1":
            self.edit_plan()
        elif mod_id == "2":
            self.remove_plan()
        else:
            return


    def edit_plan(self) -> None:
        print(" ==Edit plan== ")
        add_id = input("[1] Add mobile plan\n[2] Add VPS plan\n[3] Add VPN Plan\n[4] Back to Mod Plan Menu\n[else] Return to menu\nEnter your choice: ")
        match add_id:
            case 1: self.add_mobile_plan()
            case 2: self.add_vps_plan()
            case 3: self.add_vpn_plan()
            case 4: self.modify_plan()
            case _: self.admin_menu()

    def add_mobile_plan(self) -> None:
        print(" ==Add mobile plan== ")
        plan_id = int(input("Add new plan id : "))
        plan_name = input("Add new plan name : ")
        plan_price = int(input("Add new plan price : "))
        plan_gb = int(input("Add new plan gb : "))
        plan_description = input("Add new plan description : ")
        
        for key in self.system.mobile_plans.items():
            if plan_id == key:
                print("Plan id already exists")
                retry = input("Do you want to retry? (y/N): ")
                if retry.lower() == "y":
                    self.add_mobile_plan()
                self.modify_plan()

            elif plan_name in self.system.mobile_plans.values():
                print("Plan name already exists")
                retry = input("Do you want to retry? (y/N): ")
                if retry.lower() == "y":
                    self.add_mobile_plan()
                self.modify_plan()

    
        self.system.mobile_plans[plan_id] = {"id": plan_id, "name": plan_name, "price": plan_price, "gb": plan_gb, "description": plan_description}
        print("Plan added")
        more_id = input("[1] Add more mobile plan\n[2] Return to Mod plan Menu\n[else] Return to menu\nEnter your choice: ")
        match more_id:
            case "1": self.add_mobile_plan()
            case "2": self.modify_plan()
            case _: self.admin_menu()


    def add_vps_plan(self) -> None:
        print(" ==Add VPS plan== ")
        plan_id = int(input("Add new plan id : "))
        plan_name = input("Add new plan name : ")
        plan_price = int(input("Add new plan price : "))
        plan_description = input("Add new plan description : ")

        if plan_id in self.web.vps_packages.keys():
            print("Plan id already exists")
            retry = input("Do you want to retry? (y/N): ")
            if retry.lower() == "y":
                self.add_vps_plan()
            self.modify_plan()

        elif plan_name in self.web.vps_packages.values():
            print("Plan name already exists")
            retry = input("Do you want to retry? (y/N): ")
            if retry.lower() == "y":
                self.add_vps_plan()
            self.modify_plan()


        self.web.vps_packages[plan_id] = {"id": plan_id, "name": plan_name, "price": plan_price, "description": plan_description}
        print("Plan added")
        more_id = input("[1] Add more vps plan\n[2] Back to Mod plan Menu\n[else] Return to menu\nEnter your choice: ")
        if more_id == 1:
            self.add_vps_plan()
        elif more_id == 2:
            self.modify_plan()
        else:
            self.admin_menu()


    def add_vpn_plan(self) -> None:
        print(" ==Add VPN plan== ")
        plan_id = int(input("Add new plan id : "))
        plan_name = input("Add new plan name : ")
        plan_price = int(input("Add new plan price : "))
        plan_description = input("Add new plan description : ")
        if plan_id in self.web.vpn_packages.keys():
            print("Plan id already exists")
            retry = input("Do you want to retry? (y/N): ")
            if retry.lower() == "y":
                self.add_vpn_plan()
            self.modify_plan()

        elif plan_name in self.web.vpn_packages.values():
            print("Plan name already exists")
            retry = input("Do you want to retry? (y/N): ")
            if retry.lower() == "y":
                self.add_vpn_plan()
            self.modify_plan()

        self.web.vpn_packages[plan_id] = {"id": plan_id, "name": plan_name, "price": plan_price, "description": plan_description}
        print("Plan added")
        more_id = int(input("[1] Add more vpn plan\n[2] Back to Mod plan Menu\n[else] Return to menu\nEnter your choice: "))
        match more_id:
            case "1": self.add_vpn_plan()
            case "2": self.modify_plan()
            case _: self.admin_menu()



    def remove_plan(self) -> None:
        print(" ==Remove plan== ")
        remove_id = input("[1] Remove mobile plan\n[2] Remove VPS plan\n[3] Remove VPN Plan\n[4] Back to Mod plan Menu\n[else] Return to menu \n Enter your choice: ")
        match remove_id:
            case 1: self.remove_mobile_plan()
            case 2: self.remove_vps_plan()
            case 3: self.remove_vpn_plan()
            case 3: self.modify_plan()
            case _: self.admin_menu()


    def remove_mobile_plan(self) -> None:
        print(" ==Remove mobile plan== ")
        mb_plan_id = int(input("Enter plan id : "))
        for key, plan in self.system.mobile_plans.items():
            if key == mb_plan_id:
                confirm = input(f"Are you sure you want to delete {plan['name']} plan? (y/N): ")
                if confirm.lower() != "y":
                    return
                del self.system.mobile_plans[key]
                print("plan deleted")
                break
        else:
            print("plan not found")
            remove_id = int(input("[1] Try again\n[2] Back to Mod plan Menu\n[else] Return to menu\nEnter your choice: "))
            match remove_id:
                case "1": self.remove_mobile_plan()
                case "2": self.modify_plan()
                case _: self.admin_menu()



    def remove_vps_plan(self) -> None:
        print(" ==Remove VPS plan== ")
        vps_plan_id = int(input("Enter plan id : "))
        for key, plan in self.web.vps_packages.items():
            if key == vps_plan_id:
                confirm = input(f"Are you sure you want to delete {plan['name']} plan? (y/N): ")
                if confirm.lower() != "y":
                    return
                del self.web.vps_packages[key]
                print("plan deleted")
                break
        else:
            print("plan not found")
            remove_id = int(input("[1] Try again\n[2] Back to Mod plan Menu\n[else] Return to menu\nEnter your choice: "))
            match remove_id:
                case "1": self.remove_vps_plan()
                case "2": self.modify_plan()
                case _: self.admin_menu()



    def remove_vpn_plan(self) -> None:
        print(" ==Remove VPN plan== ")
        plan_id = int(input("Enter plan id : "))
        for key, plan in self.web.vpn_packages.items():
            if key == plan_id:
                confirm = input(f"Are you sure you want to delete {plan['name']} plan? (y/N): ")
                if confirm.lower() != "y":
                    return
                del self.web.vpn_packages[key]
                print("plan deleted")
                break
        else:
            print("plan not found")
            remove_id = int(input("[1] Try again\n[2] Back to Mod plan Menu\n[else] Return to menu\nEnter your choice: "))
            match remove_id:
                case "1": self.remove_vpn_plan()
                case "2": self.modify_plan()
                case _: self.admin_menu()


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