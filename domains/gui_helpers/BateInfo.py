if __name__ == "__main__":
    import sys

    print("\nTHIS FILE IS NOT INTENDED TO BE RUN DIRECTLY.\n")
    sys.exit(1)


import customtkinter as ctk
from customtkinter import *
import domains.gui_helpers.BateMain
from domains.system import System
from domains.web import Web


class BateInfo:
    def __init__(self, system: System, web: Web):
        self.system = system
        self.web = web

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        self.root = ctk.CTk()
        self.root.title("B.A.T.E Internet")
        self.root.geometry("800x550")
        self.root.resizable(FALSE, FALSE)
        self.main_frame()
        self.info_frame()


    def main_frame(self):
        # screen = ctk.CTkFrame(self.root)
        # screen.pack(fill=BOTH, expand=1)
        # screen.configure(fg_color="dark cyan")
        # screen.pack_propagate(FALSE)
        self.screen = ctk.CTkFrame(self.root)
        self.screen.pack(fill=BOTH, expand=1)
        self.screen.configure(fg_color="dark cyan")
        self.screen.pack_propagate(FALSE)

        self.return_button = ctk.CTkButton(
            self.screen,
            text="Return",
            width=10,
            fg_color="light blue",
            text_color="black",
            corner_radius=10,
            command=self.back_to_main,
        )
        self.return_button.pack(side=BOTTOM, pady=6)

    def info_frame(self):

        # print("====== USERNAME " + self.system.logged_in_user.username + " ======")

        self.info_title_frame = ctk.CTkFrame(
            self.screen, height=80, width=650, fg_color="light blue"
        )
        self.info_title_frame.pack(side=TOP, pady=20)
        self.info_title_frame.pack_propagate(FALSE)
        self.title = ctk.CTkLabel(
            self.info_title_frame,
            text="User's Information Menu",
            font=("Bodoni", 30, "bold"),
            fg_color="light blue",
            text_color="black",
        )
        self.title.pack(expand=1, pady=10)

        self.user_info_frame = ctk.CTkFrame(
            self.screen, height=390, width=650, fg_color="light blue"
        )
        self.user_info_frame.place(x=74, y=120)
        self.user_info_frame.pack_propagate(FALSE)
        self.text1 = ctk.CTkLabel(
            self.user_info_frame,
            text="Please check your personal information",
            font=("Bodoni", 18, "bold"),
            fg_color="light blue",
            text_color="black",
        )
        self.text1.pack(pady=10)
        self.text2 = ctk.CTkLabel(
            self.user_info_frame,
            text="If there is any problems, please contact an admin for help!",
            font=("Helvetica", 18, "italic"),
            fg_color="light blue",
            text_color="black",
        )
        self.text2.pack()

        # NEED IMPORT USER'S INFORMATION (NAME, BALANCE, PLANS, DOMAIN, RANDOMLY GENERATED IP)
        # self.username = ctk.CTkLabel(self.user_info_frame, text="Current user: " + self.system.logged_in_user.username, font=("Helvetica",20,"bold"), fg_color="light blue", text_color="black")
        self.username = ctk.CTkLabel(
            self.user_info_frame,
            # text=("Current user: ", +self.system.logged_in_user.username),
            text=f"Current user: {self.system.logged_in_user.username}",
            font=("Helvetica", 20, "bold"),
            fg_color="light blue",
            text_color="black",
        )
        self.username.pack(pady=10)
        self.balance = ctk.CTkLabel(
            self.user_info_frame,
            # text=("Current balance: ", +self.system.logged_in_user.balance),
            text=f"Current balance: {self.system.logged_in_user.balance} VND",
            font=("Helvetica", 20, "bold"),
            fg_color="light blue",
            text_color="black",
        )
        self.balance.pack(pady=10)
        self.current_plans = ctk.CTkLabel(
            self.user_info_frame,
            text=f"Current plans: {self.system.mobile_plans[self.system.logged_in_user.mobile_plan_id]['name']}",
            font=("Helvetica", 20, "bold"),
            fg_color="light blue",
            text_color="black",
        )
        self.current_plans.pack(pady=10)
        self.current_VPN_package = ctk.CTkLabel(
            self.user_info_frame,
            text=f"Current VPN package: {self.web.vpn_packages[self.system.logged_in_user.current_vpn_plan_id]['name']}",
            font=("Helvetica", 20, "bold"),
            fg_color="light blue",
            text_color="black",
        )
        self.current_VPN_package.pack(pady=10)
        self.current_VPS_package = ctk.CTkLabel(
            self.user_info_frame,
            text=f"Current VPS package: {self.web.vps_packages[self.system.logged_in_user.current_vps_plan_id]['name']}",
            font=("Helvetica", 20, "bold"),
            fg_color="light blue",
            text_color="black",
        )
        self.current_VPS_package.pack(pady=10)
        self.current_domain = ctk.CTkLabel(
            self.user_info_frame,
            text=f"Current domain: {self.system.logged_in_user.domain_name}",
            font=("Helvetica", 20, "bold"),
            fg_color="light blue",
            text_color="black",
        )
        self.current_domain.pack(pady=10)
        self.custom_ip = ctk.CTkLabel(
            self.user_info_frame,
            text=f"Current IP: {self.system.logged_in_user.domain_ip}",
            font=("Helvetica", 20, "bold"),
            fg_color="light blue",
            text_color="black",
        )
        self.custom_ip.pack(pady=10)

    def back_to_main(self):
        self.root.destroy()
        domains.gui_helpers.BateMain.BateMain(system=self.system, web=self.web).run()

    def run(self):
        self.root.mainloop()
