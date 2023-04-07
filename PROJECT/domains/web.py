from domains.system import System

class Web:
    """Managing web, domain and VPN services"""

    def __init__(self, system: System):
        self.vps_packages = {
            1: {"name": "Basic", "price": 200000},
            2: {"name": "Advanced", "price": 350000},
            3: {"name": "High End", "price": 500000},
            4: {"name": "VIP", "price": 800000},
            5: {"name": "VIP+", "price": 1850000}
        }
        self.vpn_packages = {
            1: {"name": "Basic", "price": 100000},
            2: {"name": "Advanced", "price": 150000},
            3: {"name": "High End", "price": 200000},
            4: {"name": "VIP", "price": 300000},
            5: {"name": "VIP+", "price": 500000}
        }
        self.system = system

    def buy_domain(self) -> bool:
        """Register a new domain and IP address, return True if success, False otherwise"""

        # Check balance
        if self.system.logged_in_user.balance < 200000:
            print("You must have at least 200.000 VND to buy a domain")
            return False

        # Menu
        print("\n[1] Register a new domain (200.000 VND)")
        print("[else] Back to main menu")
        choose = input("Enter your choice: ")

        # Back to main menu
        if choose != "1":
            return False

        # Register a new domain
        domain_input = input("Make a unique domain of your own: ")
        while True:
            if self.system.is_valid_domain(domain_input):
                break
            domain_input = input("Domain is invalid or already taken. Please input a new one: ")

        # Assign domain and IP to user and deduct balance
        self.system.logged_in_user.domain_name = domain_input
        self.system.logged_in_user.domain_ip = self.system.get_random_ip()
        self.system.logged_in_user.balance -= 200000

        print("Domain registered successfully!")
        return True

    def buy_a_service(self, type: str) -> None:
        match type:
            case "VPN":
                packages = self.vpn_packages
                current_package_id = self.system.logged_in_user.current_vpn_plan_id
            case "VPS":
                packages = self.vps_packages
                current_package_id = self.system.logged_in_user.current_vps_plan_id
            case _: return

        # print every available service package
        print(f"\n== {type} Service Packages ==")
        for id, package in packages.items():
            print(f"[{id}] {package['name']} ({package['price']} VND)")
        print("[else] Back to main menu")

        # get user choice for service package id
        selected_package_id = input("\nChoose your package: ")
        if not selected_package_id.isdigit():
            return # if user choose to go back to main menu

        # validate user choice
        selected_package_id = int(selected_package_id)
        if selected_package_id not in packages.keys():
            print("Invalid package id")
            return

        # get selected package for convenience variable calling
        selected_package = packages[int(selected_package_id)]
        package_price = int(selected_package['price'])
        package_name = selected_package['name']

        # check user balance
        if self.system.logged_in_user.balance < package_price:
            print(f"\nNot enough balance ({self.system.logged_in_user.balance} VND) to buy '{package_name}' package ({package_price} VND)")
            return

        # check if user already has a service package
        if current_package_id != 0:
            print(f"\nYou already have a service package: {packages[current_package_id]['name']}")

            # it's called "upgrade" if user buy a higher tier package (higher id), else it's called "downgrade"
            change_tier = "upgrade" if current_package_id < int(selected_package_id) else "downgrade"

            # confirm to down/upgrade
            confirm = input(f"Do you want to {change_tier} to {package_name} package? [1] Yes | [else] No: ")
            if confirm != "1":
                return

        # confirm to buy
        print(f"\nCurrent balance: {self.system.logged_in_user.balance} VND")
        print(f"You have selected '{package_name}' package for {package_price} VND. Are you sure?")
        print("[1] Yes")
        print("[else] No, go back to main menu")
        confirm = input("Enter your choice: ")
        if confirm != "1":
            return

        # deduct user balance
        self.system.logged_in_user.balance -= package_price
        match type:
            case "VPN":
                self.system.logged_in_user.current_vpn_plan_id = selected_package_id
            case "VPS":
                self.system.logged_in_user.current_vps_plan_id = selected_package_id
        print(f"\nYou have purchased {package_name} package")
        return

    def domain_info(self) -> None:
        domain_name = self.system.logged_in_user.domain_name
        domain_ip = self.system.logged_in_user.domain_ip
        if domain_name == "":
            print("You don't have a domain yet")
        else:
            print(f"Domain name: {domain_name} | Domain IP: {domain_ip}")

    def check_service_info(self, type: str) -> None:
        match type:
            case "VPN":
                user_service_id = self.system.logged_in_user.current_vpn_plan_id
                services = self.vpn_packages
            case "VPS":
                user_service_id = self.system.logged_in_user.current_vps_plan_id
                services = self.vps_packages
            case _: return

        # check if user has a service package
        if user_service_id == 0:
            print(f"You don't have any {type} service package")
            return

        # print user service package info
        service = services[user_service_id]
        print(f"Your {type}: {service['name']} | Price: {service['price']} VND")

    def web_domain_service_menu(self) -> None:
        while True:
            self.system.flush_data_to_json() # flush data to json file every time user return to this menu
            self.system.clear_screen()
            print("== Web services menu ==")
            print("[1] Buy Domain")
            print("[2] Check Domain Info")
            print("-"*10)
            print("[3] Buy VPS")
            print("[4] Check VPS Info")
            print("-"*10)
            print("[5] Buy VPN")
            print("[6] Check VPN Info")
            print("-"*10)
            print("[else] Back to main menu")
            choose = input("\nChoose your option: ")
            match choose:
                case "1": self.buy_domain()
                case "2": self.domain_info()
                case "3": self.buy_a_service("VPS")
                case "4": self.check_service_info("VPS")
                case "5": self.buy_a_service("VPN")
                case "6": self.check_service_info("VPN")
                case _:
                    return
            input("\nPress Enter to continue...")
