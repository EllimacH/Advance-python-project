import hashlib
import tkinter as tk

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()

class BATE:
    def __init__(self):
        self.users = {}

    def create_account(self, username_entry, password_entry):
        username = username_entry.get()
        password = password_entry.get()
        user = User(username, password)
        self.users[username] = user
        self.clear_entries(username_entry, password_entry)
        self.display_message("Account created successfully!")

    def log_in(self, username_entry, password_entry):
        username = username_entry.get()
        password = password_entry.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if username in self.users and self.users[username].password == hashed_password:
            self.clear_entries(username_entry, password_entry)
            self.display_message("Logged in successfully!")
        else:
            self.display_message("Invalid username or password")

    def clear_entries(self, username_entry, password_entry):
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    def display_message(self, message):
        root = tk.Tk()
        message_label = tk.Label(root, text=message)
        message_label.config(text=message)

    def run(self):
        root = tk.Tk()
        root.title("B.A.T.E")

        # Create UI elements
        welcome_label = tk.Label(root, text="Welcome to B.A.T.E!")
        username_label = tk.Label(root, text="Username:")
        password_label = tk.Label(root, text="Password:")
        username_entry = tk.Entry(root)
        password_entry = tk.Entry(root, show="*")
        create_button = tk.Button(root, text="Create account", command=lambda: self.create_account(username_entry, password_entry))
        login_button = tk.Button(root, text="Log in", command=lambda: self.log_in(username_entry, password_entry))
        quit_button = tk.Button(root, text="Quit", command=root.quit)
        message_label = tk.Label(root, text="")

        # Position UI elements
        welcome_label.pack()
        username_label.pack()
        username_entry.pack()
        password_label.pack()
        password_entry.pack()
        create_button.pack()
        login_button.pack()
        quit_button.pack()
        message_label.pack()

        root.mainloop()

bate = BATE()
bate.run()
