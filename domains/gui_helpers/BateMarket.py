if __name__ == "__main__":
    import sys
    print("\nTHIS FILE IS NOT INTENDED TO BE RUN DIRECTLY.\n")
    sys.exit(1)

from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox
import domains.gui_helpers.BateMain
from domains.web import Web
from domains.system import System
from domains.admin import AdminGUI
from domains.user import User
import domains.gui_helpers.BateMain

class BateMarket:
    def __init__(self, web: Web, system: System):
        self.web = web
        self.system = system

        self.screen = ctk.CTk()
        self.screen.title("B.A.T.E Internet")
        self.screen.geometry("700x520")
        self.screen.resizable(FALSE, FALSE)

        self.create_options_frame()
        self.create_buy_product_frame()
        self.create_mobile_frame()
        # Set current frame to mobile frame
        self.current_frame = self.mobile_frame


    def back_to_main(self):
        self.screen.destroy()
        domains.gui_helpers.BateMain.BateMain(system=self.system, web=self.web).run()

    # Function to create the menu selections
    def create_options_frame(self):
        self.options_frame = ctk.CTkFrame(self.screen, width=200, fg_color="light blue")
        self.options_frame.pack(side=LEFT, fill="y")
        self.options_frame.pack_propagate(FALSE)
        self.title = ctk.CTkLabel(self.options_frame, text="---Menu Select---", font=("Bodoni", 20, "bold"), text_color="black")
        self.title.pack(padx=5, pady=5)

        # Creating buttons for the 3 options
        self.select_mobile_plans = ctk.CTkButton(
            self.options_frame, text="Mobile Plans",
            font=("Bodoni", 16, "bold"),
            fg_color="dark cyan",
            width=280,
            height=50,
            command=self.go_to_mobile,
            state=DISABLED)
        self.select_mobile_plans.pack(padx=10, pady=40)
        self.select_vps_packages = ctk.CTkButton(self.options_frame, text="VPS Packages", font=("Bodoni", 16, "bold"), fg_color="dark cyan", width=280, height=50, command=self.go_to_vps)
        self.select_vps_packages.pack(padx=10, pady=40)
        self.select_vpn_packages = ctk.CTkButton(self.options_frame, text="VPN Packages", font=("Bodoni", 16, "bold"), fg_color="dark cyan", width=280, height=50, command=self.go_to_vpn)
        self.select_vpn_packages.pack(padx=10, pady=40)

        # Creating the return button
        self.return_button = ctk.CTkButton(self.options_frame, text="Return", fg_color="dark cyan", width=80, command=self.back_to_main)
        self.return_button.pack(side=BOTTOM, pady=10)

    def go_to_mobile(self):
        # Disable the "Mobile Plans" button and enable the rest of the buttons
        self.select_mobile_plans.configure(state=DISABLED)
        self.select_vps_packages.configure(state=NORMAL)
        self.select_vpn_packages.configure(state=NORMAL)
        # Erasing the current frame
        self.current_frame.pack_forget()
        # Adding the Mobile Plans page
        self.create_mobile_frame()
        # Assigning current frame with mobile frame
        self.current_frame = self.mobile_frame

    def go_to_vps(self):
        # Disable the "VPS Packages" button and enable the rest of the buttons
        self.select_vps_packages.configure(state=DISABLED)
        self.select_mobile_plans.configure(state=NORMAL)
        self.select_vpn_packages.configure(state=NORMAL)

        # Erasing the current frame
        self.current_frame.pack_forget()
        # Adding the VPS Packages page
        self.create_vps_frame()
        # Assigning current frame with vps frame
        self.current_frame = self.vps_frame

    def go_to_vpn(self):
        # Disable the "VPN Packages" button and enable the rest of the buttons
        self.select_vpn_packages.configure(state=DISABLED)
        self.select_mobile_plans.configure(state=NORMAL)
        self.select_vps_packages.configure(state=NORMAL)
        # Erasing the current frame
        self.current_frame.pack_forget()
        # Creating a new frame for the VPN Packages page
        self.create_vpn_frame()
        # Assigning current frame with vpn frame
        self.current_frame = self.vpn_frame

    # Function to create the frame for the purchase page

    def create_buy_product_frame(self):
        self.buy_product_frame = ctk.CTkFrame(self.screen, width=740, fg_color="dark cyan")
        self.buy_product_frame.pack(side=LEFT, fill="y")
        self.buy_product_frame.pack_propagate(FALSE)

    # Function to create the frame for the Mobile Plans page

    def create_mobile_frame(self):
        self.mobile_frame = ctk.CTkFrame(self.buy_product_frame, fg_color="dark cyan", width=740)
        self.mobile_frame.pack(side=LEFT, fill="y")
        self.mobile_frame.pack_propagate(FALSE)
        self.mobile_title = ctk.CTkLabel(self.mobile_frame, text="---Mobile Plans---", font=("Bodoni", 24, "bold"), text_color="black").pack(pady=12)

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
            self.Mobile_Item = ctk.CTkFrame(self.mobile_frame, width=180, height=132, fg_color="light blue")
            self.Mobile_Item.place(x=positions[id][0], y=positions[id][1])
            self.Mobile_Item.pack_propagate(FALSE)
            self.Mobile_Item_title = ctk.CTkLabel(self.Mobile_Item, text=mobile_plan["name"], font=("Bodoni", 18, "bold"), text_color="black").pack()
            self.Mobile_Item_text = ctk.CTkLabel(self.Mobile_Item, text=f'{mobile_plan["gb"]}GB/month', font=("Helvetica", 14, "italic"), text_color="black").pack()
            self.Mobile_Item_price = ctk.CTkLabel(self.Mobile_Item, text=f'{mobile_plan["price"]} VND', font=("Helvetica", 14, "italic", "bold"), text_color="black").pack()
            self.purchase_button = ctk.CTkButton(self.Mobile_Item, text="Purchase", width=10, state="normal", fg_color="dark cyan", command=lambda: self.system.purchase_mobile_plan(id)).pack(pady=10)

    # Function to create the frame for the VPS Packages page
    def create_vps_frame(self):
        self.vps_frame = ctk.CTkFrame(self.buy_product_frame, fg_color="dark cyan", width=740)
        self.vps_frame.pack(side=LEFT, fill="y")
        self.vps_frame.pack_propagate(FALSE)
        self.vps_title = ctk.CTkLabel(self.vps_frame, text="---VPS Packages---", font=("Bodoni", 24, "bold"), text_color="black").pack(pady=12)


        # positions of the items shown on the screen
        positions = [[0, 0], [30, 65], [290, 65], [30, 215], [290, 215], [158, 365]]

        # Creating the items of VPS Packages
        for vps_id, vps_packge in self.web.vps_packages.items():
            self.vps_item = ctk.CTkFrame(self.vps_frame, width=180, height=132, fg_color="light blue")
            self.vps_item.place(x=positions[vps_id][0], y=positions[vps_id][1])
            self.vps_item.pack_propagate(FALSE)
            self.vps_item_title = ctk.CTkLabel(self.vps_item, text=vps_packge["name"], font=("Bodoni", 18, "bold"), text_color="black").pack()

            # splitting description
            raw_desc = vps_packge["description"].split("\n")
            desc = {}
            for i in raw_desc:
                desc[i.split(":")[0].strip().replace("- ", "")] = i.split(":")[1].strip()

            self.vps_item_text = ctk.CTkLabel(self.vps_item, text=f"Ram: {desc['Ram']}\nHDD: {desc['HDD']}", font=("Helvetica", 14, "italic"), text_color="black").pack()
            self.vps_item_price = ctk.CTkLabel(self.vps_item, text=f'{vps_packge["price"]} VND', font=("Helvetica", 14, "italic", "bold"), text_color="black").pack()
            ctk.CTkButton(self.vps_item, text="Purchase", width=10, state="normal", fg_color="dark cyan", command=lambda: self.web.buy_a_service_gui("vps", vps_id)).place(x=50, y=90)

    # Function to create the frame for the VPN Packages page
    def create_vpn_frame(self):
        self.vpn_frame = ctk.CTkFrame(self.buy_product_frame, fg_color="dark cyan", width=740)
        self.vpn_frame.pack(side=LEFT, fill="y")
        self.vpn_frame.pack_propagate(FALSE)
        self.vpn_title = ctk.CTkLabel(self.vpn_frame, text="---VPN Packages---", font=("Bodoni",24,"bold"), text_color="black").pack(pady=12)

        # positions of the items shown on the screen
        positions = [[0, 0], [30, 65], [290, 65], [30, 215], [290, 215], [158, 365]]

        for vpn_id, vpn_packge in self.web.vpn_packages.items():
            self.vpn_item = ctk.CTkFrame(self.vpn_frame, width=180, height=132, fg_color="light blue")
            self.vpn_item.place(x=positions[vpn_id][0], y=positions[vpn_id][1])
            self.vpn_item.pack_propagate(FALSE)
            self.vpn_item_title = ctk.CTkLabel(self.vpn_item, text=f'{vpn_packge["name"]}',font=("Bodoni",18,"bold"), text_color="black").pack()
            self.vpn_item_text = ctk.CTkLabel(self.vpn_item, text=f'{vpn_packge["price"]} VND',font=("Helvetica",16,"bold","italic"), text_color="black").pack(pady=20)
            ctk.CTkButton(self.vpn_item, text="Purchase", width=10, state="normal", fg_color="dark cyan", command=lambda: self.web.buy_a_service_gui("vpn", vpn_id)).place(x=50, y=90)


    # Function to run the program
    def run(self):
        self.screen.mainloop()