from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox
from domains.web import Web
from domains.system import System
from domains.admin import AdminGUI
from domains.user import User

class BateMarket:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("B.A.T.E Internet")
        self.root.geometry("700x520")
        self.root.resizable(FALSE,FALSE)

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        self.create_options_frame()
        self.create_buy_product_frame()
        self.create_mobile_frame()
        # Set current frame to mobile frame
        self.current_frame = self.mobile_frame

    # Function to create the menu selections
    def create_options_frame(self):
        self.options_frame = ctk.CTkFrame(self.root, width=200, fg_color="light blue")
        self.options_frame.pack(side=LEFT, fill="y")
        self.options_frame.pack_propagate(FALSE)
        self.title = ctk.CTkLabel(self.options_frame, text="---Menu Select---", font=("Bodoni",20,"bold"), text_color="black")
        self.title.pack(padx=5, pady=5)

        # Creating buttons for the 3 options
        self.select_mobile_plans = ctk.CTkButton(self.options_frame, text="Mobile Plans", font=("Bodoni",16,"bold"), fg_color="dark cyan", width=280, height=50, command=self.go_to_mobile, state=DISABLED)
        self.select_mobile_plans.pack(padx=10, pady=40)
        self.select_vps_packages = ctk.CTkButton(self.options_frame, text="VPS Packages", font=("Bodoni",16,"bold"), fg_color="dark cyan", width=280, height=50, command=self.go_to_vps)
        self.select_vps_packages.pack(padx=10, pady=40)
        self.select_vpn_packages = ctk.CTkButton(self.options_frame, text="VPN Packages", font=("Bodoni",16,"bold"), fg_color="dark cyan", width=280, height=50, command=self.go_to_vpn)
        self.select_vpn_packages.pack(padx=10, pady=40)

        # Creating the return button
        self.return_button = ctk.CTkButton(self.options_frame, text="Return", fg_color="dark cyan", width=80, command=self.root.quit)
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
        self.buy_product_frame = ctk.CTkFrame(self.root, width=740, fg_color="dark cyan")
        self.buy_product_frame.pack(side=LEFT, fill="y")
        self.buy_product_frame.pack_propagate(FALSE)


    # Function to create the frame for the Mobile Plans page
    def create_mobile_frame(self):
        # Creating the frame for the Mobile Plans page
        self.mobile_frame = ctk.CTkFrame(self.buy_product_frame, fg_color="dark cyan", width=740)
        self.mobile_frame.pack(side=LEFT, fill="y")
        self.mobile_frame.pack_propagate(FALSE)
        self.mobile_title = ctk.CTkLabel(self.mobile_frame, text="---Mobile Plans---", font=("Bodoni",24,"bold"), text_color="black").pack(pady=12)
        # Creating the items of Mobile Plans
        
        # Bronze Plan
        self.Mobile_Item1 = ctk.CTkFrame(self.mobile_frame, width=180, height=132, fg_color="light blue")
        self.Mobile_Item1.place(x=30, y=100)
        self.Mobile_Item1.pack_propagate(FALSE)
        self.Mobile_Item1_title = ctk.CTkLabel(self.Mobile_Item1, text="Bronze", font=("Bodoni",18,"bold"), text_color="black").pack()
        self.Mobile_Item1_text = ctk.CTkLabel(self.Mobile_Item1, text="30GB/month", font=("Helvetica",14,"italic"), text_color="black").pack()
        self.Mobile_Item1_price = ctk.CTkLabel(self.Mobile_Item1, text="150,000 VND", font=("Helvetica",16,"italic","bold"), text_color="black").pack()
                
        # Silver Plan
        self.Mobile_Item2 = ctk.CTkFrame(self.mobile_frame, width=180, height=132, fg_color="light blue")
        self.Mobile_Item2.place(x=290, y=100)
        self.Mobile_Item2.pack_propagate(FALSE)
        self.Mobile_Item2_title = ctk.CTkLabel(self.Mobile_Item2, text="Silver", font=("Bodoni",18,"bold"), text_color="black").pack()
        self.Mobile_Item2_text = ctk.CTkLabel(self.Mobile_Item2, text="50GB/month", font=("Helvetica",14,"italic"), text_color="black").pack()
        self.Mobile_Item2_price = ctk.CTkLabel(self.Mobile_Item2, text="250,000 VND", font=("Helvetica",16,"italic","bold"), text_color="black").pack()

        # Gold Plan
        self.Mobile_Item3 = ctk.CTkFrame(self.mobile_frame, width=180, height=132, fg_color="light blue")
        self.Mobile_Item3.place(x=30, y=300)
        self.Mobile_Item3.pack_propagate(FALSE)
        self.Mobile_Item3_title = ctk.CTkLabel(self.Mobile_Item3, text="Gold", font=("Bodoni",18,"bold"), text_color="black").pack()
        self.Mobile_Item3_text = ctk.CTkLabel(self.Mobile_Item3, text="100GB/month", font=("Helvetica",14,"italic"), text_color="black").pack()
        self.Mobile_Item3_price = ctk.CTkLabel(self.Mobile_Item3, text="500,000 VND", font=("Helvetica",16,"italic","bold"), text_color="black").pack()

        # Diamond Plan
        self.Mobile_Item4 = ctk.CTkFrame(self.mobile_frame, width=180, height=132, fg_color="light blue")
        self.Mobile_Item4.place(x=290, y=300)
        self.Mobile_Item4.pack_propagate(FALSE)
        self.Mobile_Item4_title = ctk.CTkLabel(self.Mobile_Item4, text="Diamond", font=("Bodoni",18,"bold"), text_color="black").pack()
        self.Mobile_Item4_text = ctk.CTkLabel(self.Mobile_Item4, text="500GB/month", font=("Helvetica",14,"italic"), text_color="black").pack()
        self.Mobile_Item4_price = ctk.CTkLabel(self.Mobile_Item4, text="2,500,000 VND", font=("Helvetica",16,"italic","bold"), text_color="black").pack()

        # Creating a button to purchase selected item
        for id, mobile_plan in self.system.mobile_plans.items():
            if id == 0:
                continue
            self.Mobile_Item = Frame(self.mobile_frame, width=180, height=132, bg="cyan")
            self.Mobile_Item.place(x=positions[id][0], y=positions[id][1])
            self.Mobile_Item.pack_propagate(FALSE)
            self.Mobile_Item_title = ctk.CTkLabel(self.Mobile_Item, text=mobile_plan["name"], font=("Bodoni",16,"bold"), bg="cyan").pack()
            self.Mobile_Item_text = ctk.CTkLabel(self.Mobile_Item, text=f'{mobile_plan["gb"]}GB/month', font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)
            self.Mobile_Item_price = ctk.CTkLabel(self.Mobile_Item, text=f'{mobile_plan["price"]} VND', font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)
            Button(self.Mobile_Item, text="Purchase", bg="light cyan", width=10, state="normal", command= lambda id=id: self.system.purchase_mobile_plan(id)).place(x=50, y=90)



    # Function to create the frame for the VPS Packages page
    def create_vps_frame(self):
        self.vps_frame = ctk.CTkFrame(self.buy_product_frame, fg_color="dark cyan", width=740)
        self.vps_frame.pack(side=LEFT, fill="y")
        self.vps_frame.pack_propagate(FALSE)
        self.vps_title = ctk.CTkLabel(self.vps_frame, text="---VPS Packages---", font=("Bodoni",24,"bold"), text_color="black").pack(pady=12)
       
        # Creating the items of VPS Packages
        
        # Basic Package
        self.VPS_Item1 = ctk.CTkFrame(self.vps_frame, width=180, height=132, fg_color="light blue")
        self.VPS_Item1.place(x=30, y=65)
        self.VPS_Item1.pack_propagate(FALSE)
        self.VPS_Item1_title = ctk.CTkLabel(self.VPS_Item1, text="Basic", font=("Bodoni",18,"bold"), text_color="black").pack()
        self.VPS_Item1_text = ctk.CTkLabel(self.VPS_Item1, text="Ram: 01 GB\nHDD: 50 GB", font=("Helvetica",14,"italic"), text_color="black").pack()
        self.VPS_Item1_price = ctk.CTkLabel(self.VPS_Item1, text="500,000 VND", font=("Helvetica",16,"bold","italic"), text_color="black").pack()

        # Advanced Package
        self.VPS_Item2 = ctk.CTkFrame(self.vps_frame, width=180, height=132, fg_color="light blue")
        self.VPS_Item2.place(x=290, y=65)
        self.VPS_Item2.pack_propagate(FALSE)
        self.VPS_Item2_title = ctk.CTkLabel(self.VPS_Item2, text="Advanced", font=("Bodoni",18,"bold"), text_color="black").pack()
        self.VPS_Item2_text = ctk.CTkLabel(self.VPS_Item2, text="Ram: 02 GB\nHDD: 100 GB", font=("Helvetica",14,"italic"), text_color="black").pack()
        self.VPS_Item2_price = ctk.CTkLabel(self.VPS_Item2, text="700,000 VND", font=("Helvetica",16,"bold","italic"), text_color="black").pack()

        # High End Package
        self.VPS_Item3 = ctk.CTkFrame(self.vps_frame, width=180, height=132, fg_color="light blue")
        self.VPS_Item3.place(x=30, y=215)
        self.VPS_Item3.pack_propagate(FALSE)
        self.VPS_Item3_title = ctk.CTkLabel(self.VPS_Item3, text="High End", font=("Bodoni",18,"bold"), text_color="black").pack()
        self.VPS_Item3_text = ctk.CTkLabel(self.VPS_Item3, text="Ram: 04 GB\nHDD: 200 GB", font=("Helvetica",14,"italic"), text_color="black").pack()
        self.VPS_Item3_price = ctk.CTkLabel(self.VPS_Item3, text="1,000,000 VND", font=("Helvetica",16,"bold","italic"), text_color="black").pack()

        # VIP Package
        self.VPS_Item4 = ctk.CTkFrame(self.vps_frame, width=180, height=132, fg_color="light blue")
        self.VPS_Item4.place(x=290, y=215)
        self.VPS_Item4.pack_propagate(FALSE)
        self.VPS_Item4_title = ctk.CTkLabel(self.VPS_Item4, text="VIP", font=("Bodoni",18,"bold"), text_color="black").pack()
        self.VPS_Item4_text = ctk.CTkLabel(self.VPS_Item4, text="Ram: 08 GB\nHDD: 400 GB", font=("Helvetica",14,"italic"), text_color="black").pack()
        self.VPS_Item4_price = ctk.CTkLabel(self.VPS_Item4, text="1,500,000 VND", font=("Helvetica",16,"bold","italic"), text_color="black").pack()


        # VIP+ Package
        self.VPS_Item5 = ctk.CTkFrame(self.vps_frame, width=180, height=132, fg_color="light blue")
        self.VPS_Item5.place(x=158, y=365)
        self.VPS_Item5.pack_propagate(FALSE)
        self.VPS_Item5_title = ctk.CTkLabel(self.VPS_Item5, text="VIP+", font=("Bodoni",18,"bold"), text_color="black").pack()
        self.VPS_Item5_text = ctk.CTkLabel(self.VPS_Item5, text="Ram: 16 GB\nHDD: 800 GB", font=("Helvetica",14,"italic"), text_color="black").pack()
        self.VPS_Item5_price = ctk.CTkLabel(self.VPS_Item5, text="2,000,000 VND", font=("Helvetica",16,"bold","italic"), text_color="black").pack()

        # Creating a button to purchase selected item
        for VPS in [self.VPS_Item1, self.VPS_Item2, self.VPS_Item3, self.VPS_Item4, self.VPS_Item5]:
            self.purchase_button = ctk.CTkButton(VPS, text="Purchase", width=10, state="normal", fg_color="dark cyan" ,command=self.purchase_item).pack(pady= 8)


    # Function to create the ctk.CTkFrame for the VPN Packages page
    def create_vpn_frame(self):
        self.vpn_frame = ctk.CTkFrame(self.buy_product_frame, fg_color="dark cyan", width=740)
        self.vpn_frame.pack(side=LEFT, fill="y")
        self.vpn_frame.pack_propagate(FALSE)
        self.vpn_title = ctk.CTkLabel(self.vpn_frame, text="---VPN Packages---", font=("Bodoni",24,"bold"), text_color="black").pack(pady=12)
        # Creating the items of VPN Packages
        # Basic Package
        self.VPN_Item1 = ctk.CTkFrame(self.vpn_frame, width=180, height=132, fg_color="light blue")
        self.VPN_Item1.place(x=30, y=65)
        self.VPN_Item1.pack_propagate(FALSE)
        self.VPN_Item1_title = ctk.CTkLabel(self.VPN_Item1, text="Basic", font=("Bodoni",18,"bold"), text_color="black").pack()
        self.VPN_Item1_text = ctk.CTkLabel(self.VPN_Item1, text="100,000 VND", font=("Helvetica",16,"bold","italic"), text_color="black").pack(pady=20)

        # Advanced Package
        self.VPN_Item2 = ctk.CTkFrame(self.vpn_frame, width=180, height=132, fg_color="light blue")
        self.VPN_Item2.place(x=290, y=65)
        self.VPN_Item2.pack_propagate(FALSE)
        self.VPN_Item2_title = ctk.CTkLabel(self.VPN_Item2, text="Advanced", font=("Bodoni",18,"bold"), text_color="black").pack()
        self.VPN_Item2_text = ctk.CTkLabel(self.VPN_Item2, text="150,000 VND", font=("Helvetica",16,"bold","italic"), text_color="black").pack(pady=20)

        # High End Package
        self.VPN_Item3 = ctk.CTkFrame(self.vpn_frame, width=180, height=132, fg_color="light blue")
        self.VPN_Item3.place(x=30, y=215)
        self.VPN_Item3.pack_propagate(FALSE)
        self.VPN_Item3_title = ctk.CTkLabel(self.VPN_Item3, text="High End", font=("Bodoni",18,"bold"), text_color="black").pack()
        self.VPN_Item3_text = ctk.CTkLabel(self.VPN_Item3, text="200,000 VND", font=("Helvetica",16,"bold","italic"), text_color="black").pack(pady=20)

        # VIP Package
        self.VPN_Item4 = ctk.CTkFrame(self.vpn_frame, width=180, height=132, fg_color="light blue")
        self.VPN_Item4.place(x=290, y=215)
        self.VPN_Item4.pack_propagate(FALSE)
        self.VPN_Item4_title = ctk.CTkLabel(self.VPN_Item4, text="VIP", font=("Bodoni",18,"bold"), text_color="black").pack()
        self.VPN_Item4_text = ctk.CTkLabel(self.VPN_Item4, text="300,000 VND", font=("Helvetica",16,"bold","italic"), text_color="black").pack(pady=20)

        # VIP+ Package
        self.VPN_Item5 = ctk.CTkFrame(self.vpn_frame, width=180, height=132, fg_color="light blue")
        self.VPN_Item5.place(x=158, y=365)
        self.VPN_Item5.pack_propagate(FALSE)
        self.VPN_Item5_title = ctk.CTkLabel(self.VPN_Item5, text="VIP+", font=("Bodoni",18,"bold"), text_color="black").pack()
        self.VPN_Item5_text = ctk.CTkLabel(self.VPN_Item5, text="500,000 VND", font=("Helvetica",16,"bold","italic"), text_color="black").pack(pady=20)

        # Creating a button to purchase selected item
        for VPN in [self.VPN_Item1, self.VPN_Item2, self.VPN_Item3, self.VPN_Item4, self.VPN_Item5]:
            self.purchase_button = ctk.CTkButton(VPN, text="Purchase", width=10, state="normal", fg_color="dark cyan" ,command=self.purchase_item).pack(pady=5)


    # Function to run the program
    def run(self):
        self.root.mainloop()



bate = BateMarket()
bate.run()