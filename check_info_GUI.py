from tkinter import *
import customtkinter as ctk

class BateInfo:
    def __init__(self):
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        self.root = ctk.CTk()
        self.root.title("B.A.T.E Internet")
        self.root.geometry("800x550")
        self.root.resizable(FALSE, FALSE)
        self.main_frame()
        self.info_frame()


    def main_frame(self):
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill=BOTH, expand=1)
        self.main_frame.configure(fg_color="dark cyan")
        self.main_frame.pack_propagate(FALSE)


    def info_frame(self):
        self.info_title_frame = ctk.CTkFrame(self.main_frame, height=80, width=650, fg_color="light blue")
        self.info_title_frame.pack(side=TOP,pady=20)
        self.info_title_frame.pack_propagate(FALSE)
        self.title = ctk.CTkLabel(self.info_title_frame, text="---User's Information Menu---", font=("Bodoni",30,"bold"), fg_color="light blue", text_color="black")
        self.title.pack(expand=1, pady=10)

        self.info_frame = ctk.CTkFrame(self.main_frame, height=390, width=650, fg_color="light blue")
        self.info_frame.place(x=74, y=120)
        self.info_frame.pack_propagate(FALSE)
        self.text1 = ctk.CTkLabel(self.info_frame, text="-Please check your personal information-", font=("Bodoni",18,"bold"), fg_color="light blue", text_color="black")
        self.text1.pack(pady=10)
        self.text2 = ctk.CTkLabel(self.info_frame, text="If there is any problems, please contact an admin for help!", font=("Helvetica",18,"italic"), fg_color="light blue", text_color="black")
        self.text2.pack()

        # NEED IMPORT USER'S INFORMATION (NAME, BALANCE, PLANS, DOMAIN, RANDOMLY GENERATED IP)
        self.username = ctk.CTkLabel(self.info_frame, text="Current user: ", font=("Helvetica",20,"bold"), fg_color="light blue", text_color="black")
        self.username.pack(pady=10)
        self.balance = ctk.CTkLabel(self.info_frame, text="Current balance: ", font=("Helvetica",20,"bold"), fg_color="light blue", text_color="black")
        self.balance.pack(pady=10)
        self.current_plans = ctk.CTkLabel(self.info_frame, text="Current plans: ", font=("Helvetica",20,"bold"), fg_color="light blue", text_color="black")
        self.current_plans.pack(pady=10)
        self.registered_domain = ctk.CTkLabel(self.info_frame, text="Registered domain: ", font=("Helvetica",20,"bold"), fg_color="light blue", text_color="black")
        self.registered_domain.pack(pady=10)
        self.custom_ip = ctk.CTkLabel(self.info_frame, text="Custom IP: ", font=("Helvetica",20,"bold"), fg_color="light blue", text_color="black")
        self.custom_ip.pack(pady=10)
        self.custom_ip_box = ctk.CTkTextbox(self.info_frame, width=500, height=1, fg_color="light cyan", text_color="black", corner_radius=10)
        self.custom_ip_box.pack()
        self.custom_ip_box.insert("0.0", "Need to add a function that create random IP! (The IP will be placed here!)")
        self.custom_ip_box.configure(state="disabled")


        self.return_button = ctk.CTkButton(self.main_frame, text="Return", width=10, fg_color="light blue", text_color="black", corner_radius=10, command=self.root.destroy)
        self.return_button.pack(side=BOTTOM, pady=6)

    def run(self):
        self.root.mainloop()

bate = BateInfo()
bate.run()