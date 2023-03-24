# import hashlib

# # Define a dictionary to store user information
# users = {}

# # Function to create a new account
# def create_account():
#     print("Create a new account\n")
#     username = input("Enter a username: ")
#     password = input("Enter a password: ")
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()
#     users[username] = hashed_password
#     print("Account created successfully!")
#     print("")

# # Function to log in
# def log_in():
#     print("Log in to your account\n")
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()
#     if username in users and users[username] == hashed_password:
#         print("Logged in successfully!")
#     else:
#         print("Invalid username or password")
#     print("")

# # Main program loop
# while True:
#     print("Welcome to B.A.T.E!")
#     print("1. Create a new account")
#     print("2. Log in")
#     print("3. Quit")
#     choice = input("Enter your choice: ")
#     print("")
    
#     if choice == "1":
#         create_account()
#     elif choice == "2":
#         log_in()
#     elif choice == "3":
#         break
#     else:
#         print("Invalid choice")




#create GUI for login.py

from tkinter import *
from tkinter import messagebox
import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()

class BATE:
    def __init__(self):
        self.users = {}

    def create_account(self):
        username = self.username.get()
        password = self.password.get()
        user = User(username, password)
        self.users[username] = user
        messagebox.showinfo("Success", "Account created successfully!")

    def log_in(self):
        username = self.username.get()
        password = self.password.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if username in self.users and self.users[username].password == hashed_password:
            messagebox.showinfo("Success", "Logged in successfully!")
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def run(self):
        self.root = Tk()
        self.root.title("B.A.T.E")
        self.root.geometry("300x200")

        self.username_label = Label(self.root, text="Username")
        self.username_label.grid(row=0, column=0)
        self.username = Entry(self.root)
        self.username.grid(row=0, column=1)

        self.password_label = Label(self.root, text="Password")
        self.password_label.grid(row=1, column=0)
        self.password = Entry(self.root, show="*")
        self.password.grid(row=1, column=1)

        self.create_account_button = Button(self.root, text="Create Account", command=self.create_account)
        self.create_account_button.grid(row=2, column=0)

        self.log_in_button = Button(self.root, text="Log In", command=self.log_in)
        self.log_in_button.grid(row=2, column=1)

        self.root.mainloop()

bate = BATE()
bate.run()

