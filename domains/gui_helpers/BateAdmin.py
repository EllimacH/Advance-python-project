if __name__ == "__main__":
    import sys
    print("\nTHIS FILE IS NOT INTENDED TO BE RUN DIRECTLY.\n")
    sys.exit(1)

import customtkinter as ctk
#from tkinter import *
from tkinter import messagebox

FALSE = ctk.FALSE
LEFT = ctk.LEFT
BOTTOM = ctk.BOTTOM
NORMAL = ctk.NORMAL
DISABLED = ctk.DISABLED

class BateAdmin:
    def __init__(self):
        self.screen = ctk.CTk()
        self.screen.title("B.A.T.E Internet")
        self.screen.geometry("980x560")
        self.screen.resizable(FALSE, FALSE)
        
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        # Frame for option buttons (buttons to change frames)
        self.options_frame()
        # Frame for the main screen
        self.create_main_frame()
        # Frame for the users info menu
        self.create_check_users_info_frame()
        # Set current frame to User info frame (default frame)
        self.current_screen = self.info_frame
    

    def options_frame(self):
        self.frame1 = ctk.CTkFrame(self.screen, width=185, fg_color="dark cyan")
        self.frame1.pack(side=LEFT, fill="y")
        self.frame1.pack_propagate(FALSE)

        self.frame1_welcome1 = ctk.CTkLabel(self.frame1, text="-Welcome Admin-", font=("Helvetica",20,"bold"), text_color="black")
        self.frame1_welcome1.pack(padx=5, pady=5)
        self.frame1_welcome2 = ctk.CTkLabel(self.frame1, text="What do you want to do?", font=("Helvetica",16), text_color="black")
        self.frame1_welcome2.pack()
    
        # Creating buttons to change screen
        self.change_to_users_info = ctk.CTkButton(self.frame1, text="Users Information",  font=("Bodoni",13,"bold"), state=DISABLED, width=280, height=40, command=self.select_users_info)
        self.change_to_users_info.pack(padx=10, pady=50)
        self.change_to_change_info = ctk.CTkButton(self.frame1, text="Change Users Info", font=("Bodoni",13,"bold"), width=280, height=40, command=self.select_change_info)
        self.change_to_change_info.pack(padx=10, pady=50)
        self.change_to_change_plan = ctk.CTkButton(self.frame1, text="Add/Remove Products", font=("Bodoni",13,"bold"), width=280, height=40, command=self.select_change_products)
        self.change_to_change_plan.pack(padx=10, pady=50)

        # Creating a "Return" button
        self.return_button = ctk.CTkButton(self.frame1, text="Return", width=80, command=self.screen.quit)
        self.return_button.pack(side=BOTTOM, pady=10)


    def select_users_info(self):
        # Disabled Users Info button
        self.change_to_users_info.configure(state=DISABLED)
        self.change_to_change_info.configure(state=NORMAL)
        self.change_to_change_plan.configure(state=NORMAL)
        # Delete previous frame
        self.current_screen.pack_forget()
        # Display the correct frame (Users Info)
        self.create_check_users_info_frame()
        # Set current screen to Users info frame
        self.current_screen = self.info_frame


    def select_change_info(self):
        # Disabled Change Users Info button
        self.change_to_users_info.configure(state=NORMAL)
        self.change_to_change_info.configure(state=DISABLED)
        self.change_to_change_plan.configure(state=NORMAL)
        # Delete previous frame
        self.current_screen.pack_forget()
        # Display the correct frame (Change Users Info)
        self.create_change_users_info_frame()
        # Set current screen to Change Users info frame
        self.current_screen = self.change_info_frame


    def select_change_products(self):
        # Disabled Change Products button
        self.change_to_users_info.configure(state=NORMAL)
        self.change_to_change_info.configure(state=NORMAL)
        self.change_to_change_plan.configure(state=DISABLED)
        # Delete previous frame
        self.current_screen.pack_forget()
        # Display the correct frame (Change Products)
        self.create_change_products_frame()
        # Set current screen to Change Products frame
        self.current_screen = self.products_frame

    
    def create_main_frame(self):
        self.main_frame = ctk.CTkFrame(self.screen,width=795)
        self.main_frame.pack(side=LEFT, fill="y")
        self.main_frame.configure(fg_color="dark cyan")
        self.main_frame.pack_propagate(FALSE)


    # Default frame
    def create_check_users_info_frame(self):
        self.info_frame = ctk.CTkFrame(self.main_frame, width=795, fg_color="light blue")
        self.info_frame.pack(side=LEFT, fill="y")
        self.info_frame.pack_propagate(FALSE)
        self.info_frame_title = ctk.CTkLabel(self.info_frame, text="---Users' Information---", font=("Bodoni",20,"bold"), text_color="black").pack(pady=10)
        self.search_user_label = ctk.CTkLabel(self.info_frame, text="Search User:", font=("Bodoni",15,"bold"), text_color="black").place(x=250, y=50)
        self.search_user = ctk.CTkEntry(self.info_frame, width=300, font=("Bodoni",15,"bold") , text_color="white").place(x=380, y=50)

    def create_change_users_info_frame(self):
        self.change_info_frame = ctk.CTkFrame(self.main_frame, width=795, fg_color="light blue")
        self.change_info_frame.pack(side=LEFT, fill='y')
        self.change_info_frame.pack_propagate(FALSE)
        self.change_info_frame_title = ctk.CTkLabel(self.change_info_frame, text="---Change Users' Information---", font=("Bodoni",20,"bold"), text_color="black").pack(pady=10)
        self.search_user_label = ctk.CTkLabel(self.change_info_frame, text="Search User:", font=("Bodoni",15,"bold"), text_color="black").place(x=250, y=50)
        self.search_user = ctk.CTkEntry(self.change_info_frame, width=300, font=("Bodoni",15,"bold") , text_color="white").place(x=380, y=50)

    def create_change_products_frame(self):
        self.products_frame = ctk.CTkFrame(self.main_frame, width=795, fg_color="light blue")
        self.products_frame.pack(side=LEFT, fill='y')
        self.products_frame.pack_propagate(FALSE)
        self.products_frame_title = ctk.CTkLabel(self.products_frame, text="---Products Management---", font=("Bodoni",20,"bold"), text_color="black").pack(pady=10)

    
    def run(self):
        self.screen.mainloop()