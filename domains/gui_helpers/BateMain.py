if __name__ == "__main__":
    import sys
    print("\nTHIS FILE IS NOT INTENDED TO BE RUN DIRECTLY.\n")
    sys.exit(1)

from tkinter import *
import customtkinter as ctk
import datetime
from domains.system import System
from domains.web import Web
from domains.gui_helpers.BateMarket import BateMarket
from domains.gui_helpers.BateInfo import BateInfo
from domains.gui_helpers.BateMoney import BateMoney

class BateMain:
    def __init__(self, system: System, web: Web):
        self.root1 = ctk.CTk()
        self.root1.title("B.A.T.E Internet")
        self.root1.geometry("620x390")
        self.root1.resizable(FALSE, FALSE)
        self.main_frame()

        self.system = system
        self.web = web

    def greeting(self):
        self.currentTime = datetime.datetime.now()
        self.currentTime.hour
        if self.currentTime.hour < 12:
            self.morn_text = ctk.CTkLabel(self.main_menu_title_frame, text="-Good morning! What would you like to do today?-", font=("Helvetica",16,"italic"), fg_color="light blue", text_color="black")
            self.morn_text.pack(pady=5)
        elif self.currentTime.hour >= 12 and self.currentTime.hour < 18:
            self.aft_text = ctk.CTkLabel(self.main_menu_title_frame, text="-Good afternoon! What would you like to do today?-", font=("Helvetica",16,"italic"), fg_color="light blue", text_color="black")
            self.aft_text.pack(pady=5)
        else:
            self.eve_text = ctk.CTkLabel(self.main_menu_title_frame, text="-Good evening! What would you like to do tonight?-", font=("Helvetica",16,"italic"), fg_color="light blue", text_color="black")
            self.eve_text.pack(pady=5)

    # Import the correct GUI with the correct class name
    def deposit(self):
        #import deposit_GUI
        self.root1.destroy()
        BateMoney(system=self.system, web=self.web).run()

    def market(self):
        self.root1.destroy()
        market_screen = BateMarket(system=self.system, web=self.web)
        market_screen.run()

    def user_info(self):
        self.root1.destroy()
        BateInfo().run()
        # BateInfo(system=self.system, web=self.web).run()

    # Import the Sign In GUI with the correct class name
    def sign_out(self):
        self.root1.destroy()
        self.sign_out.BateSignIn().run()

    def main_frame(self):
        self.m_frame = ctk.CTkFrame(self.root1, fg_color="dark cyan")
        self.m_frame.pack(fill=BOTH, expand=TRUE)
        self.m_frame.pack_propagate(FALSE)

        self.main_menu_title_frame = ctk.CTkFrame(self.m_frame, height=100, width=440, fg_color="light blue", corner_radius=10)
        self.main_menu_title_frame.pack(pady=6)
        self.main_menu_title_frame.pack_propagate(FALSE)
        self.main_menu_title = ctk.CTkLabel(self.main_menu_title_frame, text="---Welcome to B.A.T.E Internet---", font=("Bodoni",26,"bold"), fg_color="light blue", text_color="black")
        self.main_menu_title.pack(pady=12)
        self.greeting()

        self.go_to_deposit = ctk.CTkButton(self.m_frame, text="Deposit Menu", font=("Bodoni",16,"bold"),width=150, height=54, fg_color="light blue", text_color="black", corner_radius=10, command=self.deposit)
        self.go_to_deposit.pack(pady=10)
        self.go_to_market = ctk.CTkButton(self.m_frame, text="Market Menu", font=("Bodoni",16,"bold"),width=150, height=54, fg_color="light blue", text_color="black", corner_radius=10, command=self.market)
        self.go_to_market.pack(pady=10)
        self.go_to_user_info = ctk.CTkButton(self.m_frame, text="User Info", font=("Bodoni",16,"bold"),width=150, height=54, fg_color="light blue", text_color="black", corner_radius=10, command=self.user_info)
        self.go_to_user_info.pack(pady=10)

        self.return_button = ctk.CTkButton(self.m_frame, text="Return", width=10, fg_color="light blue", text_color="black", corner_radius=10, command=self.sign_out)
        self.return_button.pack(side=BOTTOM, pady=6)


    def run(self):
        self.root1.mainloop()