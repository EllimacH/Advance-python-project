from tkinter import *
from tkinter import messagebox
from domains.web import Web
from domains.system import System
from domains.admin import AdminGUI
from domains.user import User

class BateInternet:
    def __init__(self, web: Web, system: System):
        self.web = web
        self.system = system

        self.screen = Tk()
        self.screen.title("B.A.T.E Internet")
        self.screen.geometry("700x520")
        self.screen.resizable(FALSE, FALSE)

        self.create_options_frame()
        self.create_buy_product_frame()
        self.create_mobile_frame()
        # Set current frame to mobile frame
        self.current_frame = self.mobile_frame

    # Function to create the menu selections
    def create_options_frame(self):
        self.options_frame = Frame(self.screen, width=160, bg="light cyan")
        self.options_frame.pack(side=LEFT, fill="y")
        self.options_frame.pack_propagate(FALSE)
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
        self.return_button = Button(self.options_frame, text="Return", bg="light cyan", width=5, command=self.screen.quit)
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
        self.buy_product_frame = Frame(self.screen, width=740, bg="light blue")
        self.buy_product_frame.pack(side=LEFT, fill="y")
        self.buy_product_frame.pack_propagate(FALSE)


    # Function to create the frame for the Mobile Plans page
    def create_mobile_frame(self):
        self.mobile_frame = Frame(self.buy_product_frame, bg="light blue", width=740)
        self.mobile_frame.pack(side=LEFT, fill="y")
        self.mobile_frame.pack_propagate(FALSE)
        self.mobile_title = Label(self.mobile_frame, text="---Mobile Plans---", font=("Bodoni",20,"bold"), bg="light blue").pack(pady=12)

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
            self.Mobile_Item = Frame(self.mobile_frame, width=180, height=132, bg="cyan")
            self.Mobile_Item.place(x=positions[id][0], y=positions[id][1])
            self.Mobile_Item.pack_propagate(FALSE)
            self.Mobile_Item_title = Label(self.Mobile_Item, text=mobile_plan["name"], font=("Bodoni",16,"bold"), bg="cyan").pack()
            self.Mobile_Item_text = Label(self.Mobile_Item, text=f'{mobile_plan["gb"]}GB/month', font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)
            self.Mobile_Item_price = Label(self.Mobile_Item, text=f'{mobile_plan["price"]} VND', font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)
            Button(self.Mobile_Item, text="Purchase", bg="light cyan", width=10, state="normal", command= lambda id=id: self.system.purchase_mobile_plan(id)).place(x=50, y=90)

    # Function to create the frame for the VPS Packages page
    def create_vps_frame(self):
        self.vps_frame = Frame(self.buy_product_frame, bg="light blue", width=740)
        self.vps_frame.pack(side=LEFT, fill="y")
        self.vps_frame.pack_propagate(FALSE)
        self.vps_title = Label(self.vps_frame, text="---VPS Packages---", font=("Bodoni",20,"bold"), bg="light blue").pack(pady=12)

        # Creating the items of VPS Packages

        # positions of the items shown on the screen
        positions = [[0, 0], [30, 65], [290, 65], [30, 215], [290, 215], [158, 365]]

        for id, vps_packge in self.web.vps_packages.items():
            self.vps_item = Frame(self.vps_frame, width=180, height=132, bg="cyan")
            self.vps_item.place(x=positions[id][0], y=positions[id][1])
            self.vps_item.pack_propagate(FALSE)
            self.vps_item_title = Label(self.vps_item, text=vps_packge["name"], font=("Bodoni",16,"bold"), bg="cyan").pack()
            self.vps_item_text = Label(self.vps_item, text=f"{vps_packge['price']} VND", font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)
            Button(self.vps_item, text="Purchase", bg="light cyan", width=10, state="normal" ,command=lambda id=id: self.web.buy_a_service_gui("vps", id)).place(x=50, y=90)

    # Function to create the frame for the VPN Packages page
    def create_vpn_frame(self):
        self.vpn_frame = Frame(self.buy_product_frame, bg="light blue", width=740)
        self.vpn_frame.pack(side=LEFT, fill="y")
        self.vpn_frame.pack_propagate(FALSE)
        self.vpn_title = Label(self.vpn_frame, text="---VPN Packages---", font=("Bodoni",20,"bold"), bg="light blue").pack(pady=12)

        # positions of the items shown on the screen
        positions = [[0, 0], [30, 65], [290, 65], [30, 215], [290, 215], [158, 365]]

        for id, vpn_packge in self.web.vpn_packages.items():
            self.vpn_item = Frame(self.vpn_frame, width=180, height=132, bg="cyan")
            self.vpn_item.place(x=positions[id][0], y=positions[id][1])
            self.vpn_item.pack_propagate(FALSE)
            self.vpn_item_title = Label(self.vpn_item, text=vpn_packge["name"], font=("Bodoni",16,"bold"), bg="cyan").pack()
            self.vpn_item_text = Label(self.vpn_item, text=f'{vpn_packge["price"]} VND', font=("Helvetica",14,"italic"), bg="cyan").pack(pady=3)
            Button(self.vpn_item, text="Purchase", bg="light cyan", width=10, state="normal" ,command=lambda id=id: self.web.buy_a_service_gui("vpn", id)).place(x=50, y=90)

    # Function to run the program
    def run(self):
        self.screen.mainloop()

def main() -> None:

    system = System()
    web = Web(system)
    admin = AdminGUI(system)

    bate = BateInternet(web, system)
    bate.run()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)