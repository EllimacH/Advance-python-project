if __name__ == "__main__":
    import sys

    print("\nTHIS FILE IS NOT INTENDED TO BE RUN DIRECTLY.\n")
    sys.exit(1)

import customtkinter as ctk
import domains.gui_helpers.BateMain
from domains.web import Web
from domains.system import System
from tkinter import messagebox
from datetime import datetime


class BateMarket:
    def __init__(self, web: Web, system: System):
        self.web = web
        self.system = system

        self.screen = ctk.CTk()
        self.screen.title("B.A.T.E Internet")
        self.screen.geometry("700x520")
        self.screen.resizable(ctk.FALSE, ctk.FALSE)

        self.create_options_frame()
        self.create_buy_product_frame()
        self.create_mobile_frame()
        # Set current frame to mobile frame
        self.current_frame = self.mobile_frame

    def back_to_main(self):
        self.screen.destroy()
        domains.gui_helpers.BateMain.BateMain(system=self.system, web=self.web).run()

    # Create the menu selections
    def create_options_frame(self):
        self.options_frame = ctk.CTkFrame(self.screen, width=200, fg_color="light blue")
        self.options_frame.pack(side=ctk.LEFT, fill="y")
        self.options_frame.pack_propagate(ctk.FALSE)
        self.title = ctk.CTkLabel(
            self.options_frame,
            text="---Menu Select---",
            font=("Bodoni", 20, "bold"),
            text_color="black",
        )
        self.title.pack(padx=5, pady=5)

        # Creating buttons for the 3 options
        self.select_mobile_plans = ctk.CTkButton(
            self.options_frame,
            text="Mobile Plans",
            font=("Bodoni", 16, "bold"),
            fg_color="dark cyan",
            width=280,
            height=50,
            command=self.go_to_mobile,
            state=ctk.DISABLED,
        )
        self.select_mobile_plans.pack(padx=10, pady=20)
        self.register_domain = ctk.CTkButton(
            self.options_frame,
            text="Register Domain",
            font=("Bodoni", 16, "bold"),
            fg_color="dark cyan",
            width=280,
            height=50,
            command=self.go_to_domain,
        )
        self.register_domain.pack(padx=10, pady=20)
        self.select_vps_packages = ctk.CTkButton(
            self.options_frame,
            text="VPS Packages",
            font=("Bodoni", 16, "bold"),
            fg_color="dark cyan",
            width=280,
            height=50,
            command=self.go_to_vps,
        )
        self.select_vps_packages.pack(padx=10, pady=20)
        self.select_vpn_packages = ctk.CTkButton(
            self.options_frame,
            text="VPN Packages",
            font=("Bodoni", 16, "bold"),
            fg_color="dark cyan",
            width=280,
            height=50,
            command=self.go_to_vpn,
        )
        self.select_vpn_packages.pack(padx=10, pady=20)

        # Creating the return button
        self.return_button = ctk.CTkButton(
            self.options_frame,
            text="Return",
            fg_color="dark cyan",
            width=80,
            command=self.back_to_main,
        )
        self.return_button.pack(side=ctk.BOTTOM, pady=10)

    def go_to_mobile(self):
        # Disable the "Mobile Plans" button and enable the rest of the buttons
        self.select_mobile_plans.configure(state=ctk.DISABLED)
        self.select_vps_packages.configure(state=ctk.NORMAL)
        self.select_vpn_packages.configure(state=ctk.NORMAL)
        self.register_domain.configure(state=ctk.NORMAL)
        # Erasing the current frame
        self.current_frame.pack_forget()
        # Adding the Mobile Plans page
        self.create_mobile_frame()
        # Assigning current frame with mobile frame
        self.current_frame = self.mobile_frame

    def go_to_domain(self):
        # Disable the "Register Domain" button and enable the rest of the buttons
        self.register_domain.configure(state=ctk.DISABLED)
        self.select_mobile_plans.configure(state=ctk.NORMAL)
        self.select_vps_packages.configure(state=ctk.NORMAL)
        self.select_vpn_packages.configure(state=ctk.NORMAL)
        # Erasing the current frame
        self.current_frame.pack_forget()
        # Adding the Register Domain page
        self.create_domain_frame()
        # Assigning current frame with domain frame
        self.current_frame = self.domain_frame

    def go_to_vps(self):
        # Disable the "VPS Packages" button and enable the rest of the buttons
        self.select_vps_packages.configure(state=ctk.DISABLED)
        self.select_mobile_plans.configure(state=ctk.NORMAL)
        self.select_vpn_packages.configure(state=ctk.NORMAL)
        self.register_domain.configure(state=ctk.NORMAL)
        # Erasing the current frame
        self.current_frame.pack_forget()
        # Adding the VPS Packages page
        self.create_vps_frame()
        # Assigning current frame with vps frame
        self.current_frame = self.vps_frame

    def go_to_vpn(self):
        # Disable the "VPN Packages" button and enable the rest of the buttons
        self.select_vpn_packages.configure(state=ctk.DISABLED)
        self.select_mobile_plans.configure(state=ctk.NORMAL)
        self.select_vps_packages.configure(state=ctk.NORMAL)
        self.register_domain.configure(state=ctk.NORMAL)
        # Erasing the current frame
        self.current_frame.pack_forget()
        # Creating a new frame for the VPN Packages page
        self.create_vpn_frame()
        # Assigning current frame with vpn frame
        self.current_frame = self.vpn_frame

    # Function to create the frame for the purchase page
    def create_buy_product_frame(self):
        self.buy_product_frame = ctk.CTkFrame(
            self.screen, width=740, fg_color="dark cyan"
        )
        self.buy_product_frame.pack(side=ctk.LEFT, fill="y")
        self.buy_product_frame.pack_propagate(ctk.FALSE)

    # Function to create the frame for the Mobile Plans page
    def create_mobile_frame(self):
        self.mobile_frame = ctk.CTkFrame(
            self.buy_product_frame, fg_color="dark cyan", width=740
        )
        self.mobile_frame.pack(side=ctk.LEFT, fill="y")
        self.mobile_frame.pack_propagate(ctk.FALSE)
        self.mobile_title = ctk.CTkLabel(
            self.mobile_frame,
            text="---Mobile Plans---",
            font=("Bodoni", 24, "bold"),
            text_color="black",
        ).pack(pady=12)

        # Creating the items of Mobile Plans

        # positions of the items shown on the screen
        positions = [[0, 0], [30, 100], [290, 100], [30, 300], [290, 300]]
        # below, we're using the [id of the mobile plan] to get the [position value from the positions list]
        #
        # [id of the mobile plan] counts from 1
        # [position value from the positions list] counts from 0
        #
        # so we need to
        # - either subtract 1 from the [id of the mobile plan] to get the correct [position value from the positions list]
        # - or add an empty [0, 0] value to the beginning of the positions list

        for id, mobile_plan in self.system.mobile_plans.items():
            if id == 0:
                continue
            self.Mobile_Item = ctk.CTkFrame(
                self.mobile_frame, width=180, height=132, fg_color="light blue"
            )
            self.Mobile_Item.place(x=positions[id][0], y=positions[id][1])
            self.Mobile_Item.pack_propagate(ctk.FALSE)
            self.Mobile_Item_title = ctk.CTkLabel(
                self.Mobile_Item,
                text=mobile_plan["name"],
                font=("Bodoni", 18, "bold"),
                text_color="black",
            ).pack()
            self.Mobile_Item_text = ctk.CTkLabel(
                self.Mobile_Item,
                text=f'{mobile_plan["gb"]}GB/month',
                font=("Helvetica", 14, "italic"),
                text_color="black",
            ).pack()
            self.Mobile_Item_price = ctk.CTkLabel(
                self.Mobile_Item,
                text=f'{mobile_plan["price"]} VND',
                font=("Helvetica", 14, "italic", "bold"),
                text_color="black",
            ).pack()
            self.purchase_button = ctk.CTkButton(
                self.Mobile_Item,
                text="Purchase",
                width=10,
                state="normal",
                fg_color="dark cyan",
                command=lambda id=id: self.purchase_mobile_plan(id),
            ).pack(pady=10)

    def create_domain_frame(self):
        self.domain_frame = ctk.CTkFrame(
            self.buy_product_frame, fg_color="dark cyan", width=740
        )
        self.domain_frame.pack(side=ctk.LEFT, fill="y")
        self.domain_frame.pack_propagate(ctk.FALSE)
        self.domain_title = ctk.CTkLabel(
            self.domain_frame,
            text="---Register Domain---",
            font=("Bodoni", 24, "bold"),
            text_color="black",
        ).pack(pady=12)
        self.frame = ctk.CTkFrame(
            self.domain_frame, width=740, height=132, fg_color="light blue"
        )
        self.frame.pack_propagate(ctk.FALSE)
        self.frame.pack(pady=10) 
        # Creating the items of Register Domain
        self.domain_bar = ctk.CTkEntry(
            self.frame, 
            placeholder_text=".com, .org, ... EX: bate.com", 
            font=("Bodoni", 16, "bold"), 
            width=320, 
            border_color="dark cyan",
            fg_color="light cyan",
        )
        self.domain_bar.pack(pady=20)
        self.domain_button = ctk.CTkButton(
            self.frame,
            text="Register",
            font=("Bodoni", 14, "bold"),
            width=15,
            state="normal",
            fg_color="dark cyan",
            command=self.buy_a_domain,
        )
        self.domain_button.pack(pady=10)

    # Create the frame for the VPS Packages page
    def create_vps_frame(self):
        self.vps_frame = ctk.CTkFrame(
            self.buy_product_frame, fg_color="dark cyan", width=740
        )
        self.vps_frame.pack(side=ctk.LEFT, fill="y")
        self.vps_frame.pack_propagate(ctk.FALSE)
        self.vps_title = ctk.CTkLabel(
            self.vps_frame,
            text="---VPS Packages---",
            font=("Bodoni", 24, "bold"),
            text_color="black",
        ).pack(pady=12)

        # positions of the items shown on the screen
        positions = [[0, 0], [30, 65], [290, 65], [30, 215], [290, 215], [158, 365]]

        # Creating the items of VPS Packages
        for vps_id, vps_packge in self.web.vps_packages.items():
            if vps_id == 0:
                continue
            self.vps_item = ctk.CTkFrame(
                self.vps_frame, width=180, height=132, fg_color="light blue"
            )
            self.vps_item.place(x=positions[vps_id][0], y=positions[vps_id][1])
            self.vps_item.pack_propagate(ctk.FALSE)
            self.vps_item_title = ctk.CTkLabel(
                self.vps_item,
                text=vps_packge["name"],
                font=("Bodoni", 18, "bold"),
                text_color="black",
            ).pack()

            # splitting description
            raw_desc = vps_packge["description"].split("\n")
            desc = {}
            for i in raw_desc:
                desc[i.split(":")[0].strip().replace("- ", "")] = i.split(":")[
                    1
                ].strip()

            self.vps_item_text = ctk.CTkLabel(
                self.vps_item,
                text=f"Ram: {desc['Ram']}\nHDD: {desc['HDD']}",
                font=("Helvetica", 14, "italic"),
                text_color="black",
            ).pack()
            self.vps_item_price = ctk.CTkLabel(
                self.vps_item,
                text=f'{vps_packge["price"]} VND',
                font=("Helvetica", 14, "italic", "bold"),
                text_color="black",
            ).pack()
            ctk.CTkButton(
                self.vps_item,
                text="Purchase",
                width=10,
                state="normal",
                fg_color="dark cyan",
                command=lambda vps_id=vps_id: self.buy_a_service("vps", vps_id),
            ).place(x=50, y=90)

    # Create the frame for the VPN Packages page
    def create_vpn_frame(self):
        self.vpn_frame = ctk.CTkFrame(
            self.buy_product_frame, fg_color="dark cyan", width=740
        )
        self.vpn_frame.pack(side=ctk.LEFT, fill="y")
        self.vpn_frame.pack_propagate(ctk.FALSE)
        self.vpn_title = ctk.CTkLabel(
            self.vpn_frame,
            text="---VPN Packages---",
            font=("Bodoni", 24, "bold"),
            text_color="black",
        ).pack(pady=12)

        # positions of the items shown on the screen
        positions = [[0, 0], [30, 65], [290, 65], [30, 215], [290, 215], [158, 365]]

        for vpn_id, vpn_packge in self.web.vpn_packages.items():
            if vpn_id == 0:
                continue
            self.vpn_item = ctk.CTkFrame(
                self.vpn_frame, width=180, height=132, fg_color="light blue"
            )
            self.vpn_item.place(x=positions[vpn_id][0], y=positions[vpn_id][1])
            self.vpn_item.pack_propagate(ctk.FALSE)
            self.vpn_item_title = ctk.CTkLabel(
                self.vpn_item,
                text=f'{vpn_packge["name"]}',
                font=("Bodoni", 18, "bold"),
                text_color="black",
            ).pack()
            self.vpn_item_text = ctk.CTkLabel(
                self.vpn_item,
                text=f'{vpn_packge["price"]} VND',
                font=("Helvetica", 16, "bold", "italic"),
                text_color="black",
            ).pack(pady=20)
            ctk.CTkButton(
                self.vpn_item,
                text="Purchase",
                width=10,
                state="normal",
                fg_color="dark cyan",
                command=lambda vpn_id=vpn_id: self.buy_a_service("vpn", vpn_id),
            ).place(x=50, y=90)

    # Logic for purchasing a mobile plan
    def purchase_mobile_plan(self, new_plan_id: int):
        logged_in_user = self.system.logged_in_user
        mobile_plans = self.system.mobile_plans

        # checks if user has a current plan
        if logged_in_user.mobile_plan_id != 0:
            current_plan_name = mobile_plans[logged_in_user.mobile_plan_id]["name"]
            choice = messagebox.askyesno(
                "Bate",
                f"Your current plan is: {current_plan_name}. Do you want to change to {mobile_plans[new_plan_id]['name']}?",
            )
            if not choice:
                messagebox.showinfo("Bate", "Purchase cancelled.")
                return

        # checks if user has sufficient balance
        if logged_in_user.balance < int(mobile_plans[new_plan_id]["price"]):
            messagebox.showerror(
                "Bate",
                f"Insufficient balance. Your balance: {logged_in_user.balance} VND",
            )
            return

        # updates user's product and balance
        logged_in_user.mobile_plan_id = new_plan_id
        logged_in_user.balance -= int(mobile_plans[new_plan_id]["price"])
        # add transaction to user's transaction history
        logged_in_user.transaction_history.append(
                {
                    "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    "amount": int(int(mobile_plans[new_plan_id]["price"])),
                    "description": f"Purchase {mobile_plans[new_plan_id]['name']}",
                }
            )
        messagebox.showinfo(
            "Bate",
            f"Moble plan {mobile_plans[new_plan_id]['name']} purchased successfully.",
        )
        self.system.flush_data_to_json()
        return

    def buy_a_domain(self):
        """Register a new domain and IP address, return True if success, False otherwise"""
        # Check balance
        if self.system.logged_in_user.balance < 200000:
            messagebox.showerror("B.A.T.E","You must have at least 200.000 VND to buy a domain")
            return
        
        # Register a new domain
        domain_input = self.domain_bar.get()
        if not self.system.is_valid_domain(domain_input):
            messagebox.showinfo(
            "B.A.T.E","Domain is invalid or already taken. Please try again."
            )
        else:
            # domain is valid, so assign domain and IP to user and deduct balance
            self.system.logged_in_user.domain_name = domain_input
            self.system.logged_in_user.domain_ip = self.system.get_random_ip()
            self.system.logged_in_user.balance -= 200000
            self.system.logged_in_user.transaction_history.append(
                {
                    "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    "amount": 200000,
                    "description": "Register a new domain",
                }
            )
            self.domain_bar.delete(0, "end")
            messagebox.showinfo("B.A.T.E", "Domain registered successfully!")
            self.system.flush_data_to_json()
        return 

    # Logic for purchasing a service
    def buy_a_service(self, service_type: str, service_id: int) -> None:
        service_type = service_type.upper()

        # this variable is just for convenience variable calling, DO NOT ASSIGN NEW VALUE TO IT
        current_package_id: int = 0
        match service_type:
            case "VPN":
                current_package_id = self.system.logged_in_user.current_vpn_plan_id
            case "VPS":
                current_package_id = self.system.logged_in_user.current_vps_plan_id
            case _:
                return

        # check if user already has this service plan
        if current_package_id == service_id:
            messagebox.showinfo(
                "Bate",
                f"You already have {service_type} plan {self.web.vpn_packages[service_id]['name']}",
            )
            return

        # check if user has enough balance to purchase this service plan
        # if self.system.logged_in_user.balance < int(self.vpn_packages[service_id]['price']):
        #     mb.showinfo("Bate","You don't have enough balance to purchase this product")
        #     return

        # check if user already has a service plan and ask for confirmation to upgrade
        if current_package_id != 0:
            choice = messagebox.askyesno(
                "Bate",
                f"You current {service_type} plan is {self.web.vpn_packages[current_package_id]['name']}. Do you want to change?",
            )
            if not choice:
                messagebox.showinfo("Bate", "Purchase cancelled")
                return

        # deduct user balance and assign new service plan to user
        self.system.logged_in_user.balance -= int(
            self.web.vpn_packages[service_id]["price"]
        )
        match service_type:
            case "VPN":
                self.system.logged_in_user.current_vpn_plan_id = service_id
            case "VPS":
                self.system.logged_in_user.current_vps_plan_id = service_id
            case _:
                return

        # add transaction to user's transaction history
        self.system.logged_in_user.transaction_history.append(
            {
                "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "amount": int(self.web.vpn_packages[service_id]["price"]),
                "description": f"Buy {service_type} package: {self.web.vpn_packages[service_id]['name']}",
            }
        )

        messagebox.showinfo("Bate", f"You have purchase your {service_type} plan")
        self.system.flush_data_to_json()
    # Function to run the program
    def run(self):
        self.screen.mainloop()
