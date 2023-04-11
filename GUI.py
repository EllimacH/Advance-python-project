from tkinter import *
from tkinter import messagebox

class BateInternet:
    def __init__(self):
        self.root = Tk()
        self.root.title("B.A.T.E Internet")
        self.root.geometry("700x520")
        self.root.resizable(0,0)

        self.create_options_frame()
        self.create_buy_product_frame()
        self.create_mobile_frame()
        # Set current frame to mobile frame
        self.current_frame = self.mobile_frame

    # Function to create the menu selections
    def create_options_frame(self):
        self.options_frame = Frame(self.root, width=160, bg="light cyan")
        self.options_frame.pack(side=LEFT, fill="y")
        self.options_frame.pack_propagate(0)
        self.title = Label(self.options_frame, text="---Menu Select---", font=("Bodoni",14,"bold"), bg="light cyan")
        self.title.place(x=2, y=10)

        # Creating buttons for the 3 options
        self.select_mobile_plans = Button(self.options_frame, text="Mobile Plans", font=("Bodoni",12,"bold"), bg="light cyan", width=14, height=2, command=self.go_to_mobile, state=DISABLED)
        self.select_mobile_plans.place(x=4, y=110)
        self.select_vps_packages = Button(self.options_frame, text="VPS Packages", font=("Bodoni",12,"bold"), bg="light cyan", width=14, height=2, command=self.go_to_vps)
        self.select_vps_packages.place(x=4, y=210)
        self.select_vpn_packages = Button(self.options_frame, text="VPN Packages", font=("Bodoni",12,"bold"), bg="light cyan", width=14, height=2, command=self.go_to_vpn)
        self.select_vpn_packages.place(x=4, y=310)

        # Creating the return button
        self.return_button = Button(self.options_frame, text="Return", bg="light cyan", width=5, command=self.root.quit)
        self.return_button.place(x=55, y=480)


    # Creating a function for the purchase button
    def purchase_item(self):
        # MISSING CODE HERE, NEED TO ADD THE PURCHASE FUNCTIONALITY ASAP
        # Creating a messagebox to ask for user conformation
        # After confirming, the purchase will be made and the "Purchase" button will be disabled, replaced with "Purchased"
        return


    def go_to_mobile(self):
        # Disable the "Mobile Plans" button and enable the rest of the buttons
        self.select_mobile_plans.config(state=DISABLED)
        self.select_vps_packages.config(state=NORMAL)
        self.select_vpn_packages.config(state=NORMAL)
        # Erasing the current frame
        self.current_frame.pack_forget()
        # Adding the Mobile Plans page
        self.create_mobile_frame()
        # Assigning current frame with mobile frame
        self.current_frame = self.mobile_frame
    

    def go_to_vps(self):
        # Disable the "VPS Packages" button and enable the rest of the buttons
        self.select_vps_packages.config(state=DISABLED)
        self.select_mobile_plans.config(state=NORMAL)
        self.select_vpn_packages.config(state=NORMAL)

        # Erasing the current frame
        self.current_frame.pack_forget()
        # Adding the VPS Packages page
        self.create_vps_frame()
        # Assigning current frame with vps frame
        self.current_frame = self.vps_frame



    def go_to_vpn(self):
        # Disable the "VPN Packages" button and enable the rest of the buttons
        self.select_vpn_packages.config(state=DISABLED)
        self.select_mobile_plans.config(state=NORMAL)
        self.select_vps_packages.config(state=NORMAL)
        # Erasing the current frame
        self.current_frame.pack_forget()
        # Creating a new frame for the VPN Packages page
        self.create_vpn_frame()
        # Assigning current frame with vpn frame
        self.current_frame = self.vpn_frame


    # Function to create the frame for the purchase page
    def create_buy_product_frame(self):
        self.buy_product_frame = Frame(self.root, width=740, bg="light blue")
        self.buy_product_frame.pack(side=LEFT, fill="y")
        self.buy_product_frame.pack_propagate(0)


    # Function to create the frame for the Mobile Plans page
    def create_mobile_frame(self):
        # Creating the frame for the Mobile Plans page
        self.mobile_frame = Frame(self.buy_product_frame, bg="light blue", width=740)
        self.mobile_frame.pack(side=LEFT, fill="y")
        self.mobile_frame.pack_propagate(0)
        self.mobile_title = Label(self.mobile_frame, text="---Mobile Plans---", font=("Bodoni",20,"bold"), bg="light blue").pack(pady=12)
        # Creating the items of Mobile Plans
        
        # Bronze Plan
        self.Mobile_Item1 = Frame(self.mobile_frame, width=180, height=132, bg="cyan")
        self.Mobile_Item1.place(x=30, y=100)
        self.Mobile_Item1.pack_propagate(0)
        self.Mobile_Item1_title = Label(self.Mobile_Item1, text="Bronze", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.Mobile_Item1_text = Label(self.Mobile_Item1, text="30GB/month\n150,000 VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)
                
        # Silver Plan
        self.Mobile_Item2 = Frame(self.mobile_frame, width=180, height=132, bg="cyan")
        self.Mobile_Item2.place(x=290, y=100)
        self.Mobile_Item2.pack_propagate(0)
        self.Mobile_Item2_title = Label(self.Mobile_Item2, text="Silver", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.Mobile_Item2_text = Label(self.Mobile_Item2, text="50GB/month\n250,000 VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)

        # Gold Plan
        self.Mobile_Item3 = Frame(self.mobile_frame, width=180, height=132, bg="cyan")
        self.Mobile_Item3.place(x=30, y=300)
        self.Mobile_Item3.pack_propagate(0)
        self.Mobile_Item3_title = Label(self.Mobile_Item3, text="Gold", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.Mobile_Item3_text = Label(self.Mobile_Item3, text="100GB/month\n500,000 VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)

        # Diamond Plan
        self.Mobile_Item4 = Frame(self.mobile_frame, width=180, height=132, bg="cyan")
        self.Mobile_Item4.place(x=290, y=300)
        self.Mobile_Item4.pack_propagate(0)
        self.Mobile_Item4_title = Label(self.Mobile_Item4, text="Diamond", font=("Bodoni",15,"bold"), bg="cyan").pack()
        self.Mobile_Item4_text = Label(self.Mobile_Item4, text="500GB/month\n2,500,000 VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)

        # Creating a button to purchase selected item
        for Mobile in [self.Mobile_Item1, self.Mobile_Item2, self.Mobile_Item3, self.Mobile_Item4]:
            self.purchase_button = Button(Mobile, text="Purchase", bg="light cyan", width=10, state="normal" ,command=self.purchase_item).place(x=50, y=90)


    # Function to create the frame for the VPS Packages page
    def create_vps_frame(self):
        self.vps_frame = Frame(self.buy_product_frame, bg="light blue", width=740)
        self.vps_frame.pack(side=LEFT, fill="y")
        self.vps_frame.pack_propagate(0)
        self.vps_title = Label(self.vps_frame, text="---VPS Packages---", font=("Bodoni",20,"bold"), bg="light blue").pack(pady=12)
        # Creating the items of VPS Packages
        # Basic Package
        self.VPS_Item1 = Frame(self.vps_frame, width=180, height=132, bg="cyan")
        self.VPS_Item1.place(x=30, y=65)
        self.VPS_Item1.pack_propagate(0)
        self.VPS_Item1_title = Label(self.VPS_Item1, text="Basic", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.VPS_Item1_text = Label(self.VPS_Item1, text="500,000 VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)

        # Advanced Package
        self.VPS_Item2 = Frame(self.vps_frame, width=180, height=132, bg="cyan")
        self.VPS_Item2.place(x=290, y=65)
        self.VPS_Item2.pack_propagate(0)
        self.VPS_Item2_title = Label(self.VPS_Item2, text="Advanced", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.VPS_Item2_text = Label(self.VPS_Item2, text="700,000 VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)

        # High End Package
        self.VPS_Item3 = Frame(self.vps_frame, width=180, height=132, bg="cyan")
        self.VPS_Item3.place(x=30, y=215)
        self.VPS_Item3.pack_propagate(0)
        self.VPS_Item3_title = Label(self.VPS_Item3, text="High End", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.VPS_Item3_text = Label(self.VPS_Item3, text="1,000,000 VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)

        # VIP Package
        self.VPS_Item4 = Frame(self.vps_frame, width=180, height=132, bg="cyan")
        self.VPS_Item4.place(x=290, y=215)
        self.VPS_Item4.pack_propagate(0)
        self.VPS_Item4_title = Label(self.VPS_Item4, text="VIP", font=("Bodoni",15,"bold"), bg="cyan").pack()
        self.VPS_Item4_text = Label(self.VPS_Item4, text="1,300,000 VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)

        # VIP+ Package
        self.VPS_Item5 = Frame(self.vps_frame, width=180, height=132, bg="cyan")
        self.VPS_Item5.place(x=158, y=365)
        self.VPS_Item5.pack_propagate(0)
        self.VPS_Item5_title = Label(self.VPS_Item5, text="VIP+", font=("Bodoni",15,"bold"), bg="cyan").pack()
        self.VPS_Item5_text = Label(self.VPS_Item5, text="1,500,000 VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)

        # Creating a button to purchase selected item
        for VPS in [self.VPS_Item1, self.VPS_Item2, self.VPS_Item3, self.VPS_Item4, self.VPS_Item5]:
            self.purchase_button = Button(VPS, text="Purchase", bg="light cyan", width=10, state="normal" ,command=self.purchase_item).place(x=50, y=90)


    # Function to create the frame for the VPN Packages page
    def create_vpn_frame(self):
        self.vpn_frame = Frame(self.buy_product_frame, bg="light blue", width=740)
        self.vpn_frame.pack(side=LEFT, fill="y")
        self.vpn_frame.pack_propagate(0)
        self.vpn_title = Label(self.vpn_frame, text="---VPN Packages---", font=("Bodoni",20,"bold"), bg="light blue").pack(pady=12)
        # Creating the items of VPN Packages
        # Basic Package
        self.VPN_Item1 = Frame(self.vpn_frame, width=180, height=132, bg="cyan")
        self.VPN_Item1.place(x=30, y=65)
        self.VPN_Item1.pack_propagate(0)
        self.VPN_Item1_title = Label(self.VPN_Item1, text="Basic", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.VPN_Item1_text = Label(self.VPN_Item1, text="100,000 VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)

        # Advanced Package
        self.VPN_Item2 = Frame(self.vpn_frame, width=180, height=132, bg="cyan")
        self.VPN_Item2.place(x=290, y=65)
        self.VPN_Item2.pack_propagate(0)
        self.VPN_Item2_title = Label(self.VPN_Item2, text="Advanced", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.VPN_Item2_text = Label(self.VPN_Item2, text="150,000 VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)

        # High End Package
        self.VPN_Item3 = Frame(self.vpn_frame, width=180, height=132, bg="cyan")
        self.VPN_Item3.place(x=30, y=215)
        self.VPN_Item3.pack_propagate(0)
        self.VPN_Item3_title = Label(self.VPN_Item3, text="High End", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.VPN_Item3_text = Label(self.VPN_Item3, text="200,000 VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)

        # VIP Package
        self.VPN_Item4 = Frame(self.vpn_frame, width=180, height=132, bg="cyan")
        self.VPN_Item4.place(x=290, y=215)
        self.VPN_Item4.pack_propagate(0)
        self.VPN_Item4_title = Label(self.VPN_Item4, text="VIP", font=("Bodoni",15,"bold"), bg="cyan").pack()
        self.VPN_Item4_text = Label(self.VPN_Item4, text="300,000 VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)

        # VIP+ Package
        self.VPN_Item5 = Frame(self.vpn_frame, width=180, height=132, bg="cyan")
        self.VPN_Item5.place(x=158, y=365)
        self.VPN_Item5.pack_propagate(0)
        self.VPN_Item5_title = Label(self.VPN_Item5, text="VIP+", font=("Bodoni",15,"bold"), bg="cyan").pack()
        self.VPN_Item5_text = Label(self.VPN_Item5, text="500,000 VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)

        # Creating a button to purchase selected item
        for VPN in [self.VPN_Item1, self.VPN_Item2, self.VPN_Item3, self.VPN_Item4, self.VPN_Item5]:
            self.purchase_button = Button(VPN, text="Purchase", bg="light cyan", width=10, state="normal" ,command=self.purchase_item).place(x=50, y=90)


    # Function to run the program
    def run(self):
        self.root.mainloop()



bate = BateInternet()
bate.run()