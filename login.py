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


import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()

class BATE:
    def __init__(self):
        self.users = {}

    def create_account(self):
        print("Create a new account\n")
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        user = User(username, password)
        self.users[username] = user
        print("Account created successfully!")
        print("")

    def log_in(self):
        print("Log in to your account\n")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if username in self.users and self.users[username].password == hashed_password:
            print("Logged in successfully!")
        else:
            print("Invalid username or password")
        print("")

    def run(self):
        while True:
            print("Welcome to B.A.T.E!")
            print("1. Create a new account")
            print("2. Log in")
            print("3. Quit")
            choice = input("Enter your choice: ")
            print("")
            
            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.log_in()
            elif choice == "3":
                break
            else:
                print("Invalid choice")

bate = BATE()
bate.run()