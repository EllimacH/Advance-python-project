import hashlib
import customtkinter as ctk
from customtkinter import *
from tkinter import messagebox
from domains.gui_helpers.BateMain import BateMain
from domains.system import System
from domains.web import Web
from domains.user import User

class BateSignIn:
    """Sign in GUI for B.A.T.E Internet"""
    def __init__(self, system: System, web: Web):
        self.users = {}
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.system = system
        self.web = web

    # Function to create an account
    def create_account(self):
        username = self.Username_bar.get()
        password = self.Password_bar.get()

        user = User()
        user.username = username
        user.password = user.encrypt_password(password)

        if str(self.Re_Password_bar.get()) == str(self.Password_bar.get()):
            if len(str(password)) >= 8:
                messagebox.showinfo("B.A.T.E", "Account created successfully!")
                self.back_to_home()
            # If the password is not long enough
            elif len(str(password)) < 8:
                messagebox.showerror("B.A.T.E", "Password must be at least 8 characters long!")
                self.Password_bar.delete(0, END)
                self.Username_bar.delete(0, END)
                self.Re_Password_bar.delete(0, END)
            # If the username is already taken
            elif username in self.system.users:
                messagebox.showerror("B.A.T.E", "Username already taken!")
                self.Password_bar.delete(0, END)
                self.Username_bar.delete(0, END)
                self.Re_Password_bar.delete(0, END)
        else:
            messagebox.showerror("B.A.T.E", "Passwords do not match!")
            self.Password_bar.delete(0, END)
            self.Username_bar.delete(0, END)
            self.Re_Password_bar.delete(0, END)

        # Add the user to the database
        self.system.users.append(user)
        self.system.flush_data_to_json()

    # Function to log in 
    def log_in(self):
        user = User() # just to use the encrypt_password method

        input_username = self.Username_bar.get()
        input_password = self.Password_bar.get()
        hashed_password = user.encrypt_password(input_password)

        if input_username not in [user.username for user in self.system.users]:
            messagebox.showerror("B.A.T.E", "Invalid username")
            self.Password_bar.delete(0, END)
            self.Username_bar.delete(0, END)
            return
        
        if [user for user in self.system.users if user.username == input_username][0].password != hashed_password:
            messagebox.showerror("B.A.T.E", "Invalid password")
            self.Password_bar.delete(0, END)
            self.Username_bar.delete(0, END)
            return

        messagebox.showinfo("B.A.T.E", "Logged in successfully!")
        self.top.destroy()
        self.root.destroy()
        # BateInternet(system=self.system, web=self.web).run()
        BateMain(system=self.system, web=self.web).run()

    # Function to open the account creation menu
    def open1(self):
    #     self.top = Toplevel()
    #     self.top.geometry("340x230")
    #     self.top.title("B.A.T.E Internet")
    #     self.top.resizable(0,0)
    #     self.frame = LabelFrame(self.top, padx=10, pady=10)
    #     self.frame.pack(padx=10, pady=3)

    #     self.Title = Label(self.frame, text="---ACCOUNT CREATION MENU---", font=("Bodoni",13,"bold"))
    #     self.Title.grid(row=0, column=0, columnspan=3)

    #     self.objective = Label(self.frame, text="Please enter information to create an account!")
    #     self.objective.grid(row=1, column=0, columnspan=3)

    #     self.Username = Label(self.frame, text="Username", font="Bodoni")
    #     self.Username.grid(row=2, column=0)
    #     self.Username_bar = Entry(self.frame, width=24, borderwidth=3)
    #     self.Username_bar.grid(row=2, column=1, columnspan=2, padx=3, pady=3)

    #     self.Password = Label(self.frame, text="Password", font="Bodoni")
    #     self.Password.grid(row=3, column=0)
    #     self.Password_bar = Entry(self.frame, width=24, borderwidth=3, show="*")
    #     self.Password_bar.grid(row=3, column=1, columnspan=2, padx=3, pady=3)

    #     self.Re_Password = Label(self.frame, text="Confirm Password", font="Bodoni")
    #     self.Re_Password.grid(row=4, column=0)
    #     self.Re_Password_bar = Entry(self.frame, width=24, borderwidth=3, show="*")
    #     self.Re_Password_bar.grid(row=4, column=1, columnspan=2, padx=3, pady=3)

    #     self.create_button = Button(self.top, text="Create account", font=("Bodoni",12,"bold"), command=self.create_account)
    #     self.create_button.pack()

    #     self.exit_button = Button(self.top, text="Return", command=self.top.destroy)
    #     self.exit_button.pack()

        self.top = ctk.CTkToplevel()
        self.top.geometry("400x300")
        self.top.title("B.A.T.E Internet")
        self.top.resizable(FALSE,FALSE)
        self.frame = ctk.CTkFrame(self.top)
        self.frame.configure(fg_color="dark cyan")
        self.frame.pack(padx=10, pady=30)

        self.Title = ctk.CTkLabel(self.frame, text="---ACCOUNT CREATION MENU---", font=("Bodoni",13,"bold"))
        self.Title.grid(row=0, column=0, columnspan=3)

        self.objective = ctk.CTkLabel(self.frame, text="Please enter information to create an account!")
        self.objective.grid(row=1, column=0, columnspan=3, padx=10, pady= 5)

        self.Username = ctk.CTkLabel(self.frame, text="Username")
        self.Username.grid(row=2, column=0)
        self.Username_bar = ctk.CTkEntry(self.frame, width=100)
        self.Username_bar.grid(row=2, column=1, columnspan=2, padx=3, pady=3)

        self.Password = ctk.CTkLabel(self.frame, text="Password")
        self.Password.grid(row=3, column=0)
        self.Password_bar = ctk.CTkEntry(self.frame, width=100,  show="*")
        self.Password_bar.grid(row=3, column=1, columnspan=2, padx=3, pady=3)

        self.Re_Password = ctk.CTkLabel(self.frame, text="Confirm Password")
        self.Re_Password.grid(row=4, column=0, padx=3, pady=3)
        self.Re_Password_bar = ctk.CTkEntry(self.frame, width=100, show="*")
        self.Re_Password_bar.grid(row=4, column=1, columnspan=2, padx=3, pady=3)

        self.create_button = ctk.CTkButton(self.top, text="Create account", font=("Bodoni",12,"bold"), command=self.create_account)
        self.create_button.pack(padx=5, pady=5)

        self.exit_button = ctk.CTkButton(self.top, text="Return", command=self.back_to_home)
        self.exit_button.pack(padx=5, pady=5)
        
        self.root.iconify()
        
    

    # Function to open the login menu
    def open2(self):
    #     self.top = Toplevel()
    #     self.top.geometry("340x200")
    #     self.top.title("B.A.T.E Internet")
    #     self.top.resizable(0,0)
    #     self.frame = LabelFrame(self.top, padx=10, pady=10)
    #     self.frame.pack(padx=10, pady=3)

    #     self.Title = Label(self.frame, text="---ACCOUNT LOGIN MENU---", font=("Bodoni",13,"bold"))
    #     self.Title.grid(row=0, column=0, columnspan=3)

    #     self.objective = Label(self.frame, text="Please enter information to login!")
    #     self.objective.grid(row=1, column=0, columnspan=3)

    #     self.Username = Label(self.frame, text="Username", font="Bodoni")
    #     self.Username.grid(row=2, column=0)
    #     self.Username_bar = Entry(self.frame, width=24, borderwidth=3)
    #     self.Username_bar.grid(row=2, column=1, columnspan=2, padx=3, pady=3)

    #     self.Password = Label(self.frame, text="Password", font="Bodoni")
    #     self.Password.grid(row=3, column=0)
    #     self.Password_bar = Entry(self.frame, width=24, borderwidth=3, show="*")
    #     self.Password_bar.grid(row=3, column=1, columnspan=2, padx=3, pady=3)

    #     self.login_button = Button(self.top, text="Login", font=("Bodoni",12,"bold"), command=self.log_in)
    #     self.login_button.pack()

    #     self.exit_button = Button(self.top, text="Return", command=self.top.destroy)
    #     self.exit_button.pack()

        self.top = ctk.CTkToplevel()
        self.top.geometry("400x300")
        self.top.title("B.A.T.E Internet")
        self.top.resizable(FALSE,FALSE)
        self.frame = ctk.CTkFrame(self.top)
        self.frame.pack(padx=10, pady=40)

        self.Title = ctk.CTkLabel(self.frame, text="---ACCOUNT LOGIN MENU---", font=("Bodoni",13,"bold"))
        self.Title.grid(row=0, column=0, columnspan=3)

        self.objective = ctk.CTkLabel(self.frame, text="Please enter information to login!")
        self.objective.grid(row=1, column=0, columnspan=3, padx=10, pady= 5)

        self.Username = ctk.CTkLabel(self.frame, text="Username", font=("Bodoni",12))
        self.Username.grid(row=2, column=0)
        self.Username_bar = ctk.CTkEntry(self.frame, width=100)
        self.Username_bar.grid(row=2, column=1, columnspan=2, padx=3, pady=3)

        self.Password = ctk.CTkLabel(self.frame, text="Password", font=("Bodoni",12))
        self.Password.grid(row=3, column=0)
        self.Password_bar = ctk.CTkEntry(self.frame, width=100, show="*")
        self.Password_bar.grid(row=3, column=1, columnspan=2, padx=3, pady=3)

        self.login_button = ctk.CTkButton(self.top, text="Login", font=("Bodoni",12,"bold"), command=self.log_in)
        self.login_button.pack(padx=5, pady=5)

        self.exit_button = ctk.CTkButton(self.top, text="Return", command=self.back_to_home)
        self.exit_button.pack(padx=5, pady=5)

        
        self.root.iconify()

    # Function to re-open the home menu
    def back_to_home(self):
        self.root.deiconify()
        self.top.destroy()
        self.Create_Acc_Menu.configure(state=NORMAL)
        self.Login_Menu.configure(state=NORMAL)

    # Function to open the create account menu
    def run_open1(self):
        self.open1()
        # Avoid create account menu and login menu to be opened multiple times
        self.Create_Acc_Menu.configure(state=DISABLED)
        self.Login_Menu.configure(state=DISABLED)

    # Function to open the login menu
    def run_open2(self):
        self.open2()
        # Avoid create account menu and login menu to be opened multiple times
        self.Create_Acc_Menu.configure(state=DISABLED)
        self.Login_Menu.configure(state=DISABLED)


    # Function to exit the program
    def exit(self):
        self.rep = messagebox.askyesno("B.A.T.E", "Do you want to exit the app?")
        if self.rep == 1:
            self.root.quit()
            
    # Main function
    def run(self):
        # self.root = Tk()
        # self.root.title("B.A.T.E Internet")
        # self.root.geometry("300x166")
        # self.root.config(bg="light cyan")
        # self.root.resizable(0,0)

        # self.frame = LabelFrame(self.root, padx=10, pady=10)
        # self.frame.pack(padx=10, pady=10)

        # self.Title1 = Label(self.frame, text="---WELCOME TO B.A.T.E---", font=("Bodoni",14,"bold"))
        # self.Title1.grid(row=0, column=0, columnspan=3)

        # self.SubTitle1 = Label(self.frame, text="Welcome customer! Please select your action!")
        # self.SubTitle1.grid(row=1, column=0, columnspan=2)

        # self.Create_Acc_Menu = Button(self.frame, text="Register", font=("Bodoni",12,"bold"), pady=5, command=self.open1)
        # self.Create_Acc_Menu.grid(row=2, column=0)

        # self.Login_Menu = Button(self.frame, text="Login", font=("Bodoni",12,"bold"), pady=5, command=self.open2)
        # self.Login_Menu.grid(row=2, column=1)

        # self.exit_button = Button(self.root, text="Exit", command=self.exit).pack()

        # self.root.mainloop()

        self.root = ctk.CTk()
        self.root.title("B.A.T.E Internet")
        self.root.geometry("400x300")
        self.root.resizable(FALSE,FALSE)

     
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(padx=5, pady=80)

        self.Title1 = ctk.CTkLabel(self.frame, text="---WELCOME TO B.A.T.E---", font=("Bodoni",14,"bold"))
        self.Title1.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        self.SubTitle1 = ctk.CTkLabel(self.frame, text="Welcome customer! Please select your action!")
        self.SubTitle1.grid(row=1, column=0, columnspan=2)

        self.Create_Acc_Menu = ctk.CTkButton(self.frame, text="Register", font=("Bodoni",12,"bold"), command=self.run_open1)
        self.Create_Acc_Menu.grid(row=2, column=0, padx=5, pady=10)

        self.Login_Menu =ctk.CTkButton(self.frame, text="Login", font=("Bodoni",12,"bold"), command=self.run_open2)
        self.Login_Menu.grid(row=2, column=1, padx=5, pady=10)

        self.exit_button = ctk.CTkButton(self.root, text="Exit", height=20, width=50, command=self.exit).pack()

        self.root.mainloop()


def main():
    system = System()
    web = Web(system)

    main_menu = BateSignIn(web=web, system=system)
    main_menu.run()


if __name__ == "__main__":
    main()