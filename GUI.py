from tkinter import *
from tkinter import messagebox

class BateInternet:
    balance = 0
    def __init__(self):
        self.root = Tk()
        self.root.title("B.A.T.E Internet")
        self.root.geometry("900x520")
        self.root.resizable(FALSE,FALSE)

        self.create_options_frame()
        self.create_buy_product_frame()
        self.create_mobile_frame()
        self.current_frame = self.mobile_frame  


    # Function to create the menu selections
    def create_options_frame(self):
        self.options_frame = Frame(self.root, width=160, bg="light cyan")
        self.options_frame.pack(side=LEFT, fill="y")
        self.options_frame.pack_propagate(FALSE)
        self.title = Label(self.options_frame, text="---Menu Select---", font=("Bodoni",14,"bold"), bg="light cyan")
        self.title.place(x=2, y=10)

        # Creating buttons for the 3 options
        self.mobile_plans = Button(self.options_frame, text="Mobile Plans", font=("Bodoni",12,"bold"), bg="light cyan", width=14, height=2, command=self.go_to_mobile, state=DISABLED)
        self.mobile_plans.place(x=4, y=110)
        self.vps_packages = Button(self.options_frame, text="VPS Packages", font=("Bodoni",12,"bold"), bg="light cyan", width=14, height=2, command=self.go_to_vps)
        self.vps_packages.place(x=4, y=210)
        self.vpn_packages = Button(self.options_frame, text="VPN Packages", font=("Bodoni",12,"bold"), bg="light cyan", width=14, height=2, command=self.go_to_vpn)
        self.vpn_packages.place(x=4, y=310)

        # Creating the return button
        self.return_button = Button(self.options_frame, text="Return", bg="light cyan", width=5, command=self.root.quit)
        self.return_button.place(x=55, y=480)


    # Creating a function for the purchase button
    balance = 1000000 # Creating a variable for the balance
    def purchase_mobile_plan(self):
        # Creating a messagebox to ask for user conformation 
        # After confirming, if the balance is enough, the purchase will be made and the "Purchase" button will be disabled, replaced with "Purchased"
        rep = messagebox.askyesno("Purchase Confirmation", "Are you sure you want to purchase this plan?")
        if rep == True:
            # If the balance is enough, the purchase will be made and the "Purchase" button will be disabled, replaced with "Purchased"
            # If the balance is not enough, a messagebox will appear saying "Not enough balance"
            global Mobile # Making the variable "Mobile" global
            for Mobile in [self.Mobile_Item1, self.Mobile_Item2, self.Mobile_Item3, self.Mobile_Item4]:
                # make the function to display only the selected item
                if Mobile == self.Mobile_Item1:
                    self.balance -= 50000
                    if self.balance < 50000:
                        messagebox.showinfo("Purchase Information" ,"You do not have enough balance to purchase this plan")
                    else:
                        messagebox.showinfo("Purchase Information" , "Purchase successful!\nYour balance is now: " + str(self.balance))
                elif Mobile == self.Mobile_Item2:
                    self.balance -= 100000
                    if self.balance < 100000:
                        messagebox.showinfo("You do not have enough balance to purchase this plan")
                    else:
                        messagebox.showinfo("Purchase Information" , "Purchase successful!\nYour balance is now: " + str(self.balance))
                elif Mobile == self.Mobile_Item3:
                    self.balance -= 150000
                    if self.balance < 200000:
                        messagebox.showinfo("You do not have enough balance to purchase this plan")
                    else:
                        messagebox.showinfo("Purchase Information" , "Purchase successful!\nYour balance is now: " + str(self.balance))
                elif Mobile == self.Mobile_Item4:
                    self.balance -= 200000
                    if self.balance < 200000:
                        messagebox.showinfo("You do not have enough balance to purchase this plan")
                    else:
                        messagebox.showinfo("Purchase Information" , "Purchase successful!\nYour balance is now: " + str(self.balance))
        else:
            # If the user clicks "No", the messagebox will close
            pass
        

    def go_to_mobile(self):
        # Disable the "Mobile Plans" button and enable the rest of the buttons
        self.mobile_plans.config(state=DISABLED)
        self.vps_packages.config(state=NORMAL)
        self.vpn_packages.config(state=NORMAL)
        # Creating a new frame for the Mobile Plans page


    def go_to_vps(self):
        # Disable the "VPS Packages" button and enable the rest of the buttons
        self.vps_packages.config(state=DISABLED)
        self.mobile_plans.config(state=NORMAL)
        self.vpn_packages.config(state=NORMAL)
        # Creating a new frame for the VPS Packages page
        
    

    def go_to_vpn(self):
        # Disable the "VPN Packages" button and enable the rest of the buttons
        self.vpn_packages.config(state=DISABLED)
        self.mobile_plans.config(state=NORMAL)
        self.vps_packages.config(state=NORMAL)
        # Creating a new frame for the VPN Packages page


    # Function to create the frame for the purchase page
    def create_buy_product_frame(self):
        self.buy_product_frame = Frame(self.root, width=740, bg="light blue")
        self.buy_product_frame.pack(side=LEFT, fill="y")
        self.buy_product_frame.pack_propagate(FALSE)


    # Function to create the frame for the Mobile Plans page
    def create_mobile_frame(self):
        # Creating the frame for the default page (default page is Mobile Plans)
        self.mobile_frame = Frame(self.buy_product_frame, bg="light blue", width=740)
        self.mobile_frame.pack(side=LEFT, fill="y")
        self.mobile_frame.pack_propagate(FALSE)
        self.mobile_title = Label(self.mobile_frame, text="---Mobile Plans---", font=("Bodoni",20,"bold"), bg="light blue").pack(pady=12)
        # Creating the items of Mobile Plans
        
        # Bronze Plan
        self.Mobile_Item1 = Frame(self.mobile_frame, width=180, height=132, bg="cyan")
        self.Mobile_Item1.place(x=30, y=100)
        self.Mobile_Item1.pack_propagate(FALSE)
        self.Mobile_Item1_title = Label(self.Mobile_Item1, text="Bronze", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.Mobile_Item1_text = Label(self.Mobile_Item1, text="5GB/month\n50,000 VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=5)
                
        # Silver Plan
        self.Mobile_Item2 = Frame(self.mobile_frame, width=180, height=132, bg="cyan")
        self.Mobile_Item2.place(x=290, y=100)
        self.Mobile_Item2.pack_propagate(FALSE)
        self.Mobile_Item2_title = Label(self.Mobile_Item2, text="Silver", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.Mobile_Item2_text = Label(self.Mobile_Item2, text="10GB/month\n100,000 VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=5)

        # Gold Plan
        self.Mobile_Item3 = Frame(self.mobile_frame, width=180, height=132, bg="cyan")
        self.Mobile_Item3.place(x=30, y=300)
        self.Mobile_Item3.pack_propagate(FALSE)
        self.Mobile_Item3_title = Label(self.Mobile_Item3, text="Gold", font=("Bodoni",16,"bold"), bg="cyan").pack()
        self.Mobile_Item3_text = Label(self.Mobile_Item3, text="15GB/month\n150,000 VND", font=("Helvetica",13,"italic"), bg="cyan").pack(pady=5)

        # Diamond Plan
        self.Mobile_Item4 = Frame(self.mobile_frame, width=180, height=132, bg="cyan")
        self.Mobile_Item4.place(x=290, y=300)
        self.Mobile_Item4.pack_propagate(FALSE)
        self.Mobile_Item4_title = Label(self.Mobile_Item4, text="Diamond", font=("Bodoni",15,"bold"), bg="cyan").pack()
        self.Mobile_Item4_text = Label(self.Mobile_Item4, text="20GB/month\n200,000 VND", font=("Helvetica",13,"italic"), bg="cyan").pack(pady=5)

        # Creating a button to purchase selected item
        global Mobile # Making the variable "Mobile" global so that it can be used in the purchase_mobile_plan function
        for Mobile in [self.Mobile_Item1, self.Mobile_Item2, self.Mobile_Item3, self.Mobile_Item4]:
            self.purchase_button = Button(Mobile, text="Purchase", bg="light cyan", width=10, state="normal" ,command=self.purchase_mobile_plan).place(x=50, y=90)

    #pur




    def run(self):
        self.root.mainloop()


bate = BateInternet()
bate.run()
