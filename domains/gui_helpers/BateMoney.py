if __name__ == "__main__":
    import sys

    print("\nTHIS FILE IS NOT INTENDED TO BE RUN DIRECTLY.\n")
    sys.exit(1)


import customtkinter as ctk
from tkinter import messagebox
import domains.gui_helpers.BateMain
from domains.system import System
from domains.web import Web
from datetime import datetime

FALSE = ctk.FALSE
END = ctk.END
TOP = ctk.TOP
BOTTOM = ctk.BOTTOM

system = System()


class BateMoney:
    def __init__(self, system: System, web: Web):
        self.root = ctk.CTk()
        self.root.title("B.A.T.E Internet")
        self.root.geometry("820x500")
        self.root.resizable(FALSE, FALSE)
        self.root._apply_appearance_mode("system")

        self.system = system
        self.web = web

        self.main_frame()
        self.deposit_menu()
        self.balance_menu()
        self.history_menu()

        # Display existing transaction history
        self.display_transaction_history()

    def action_deposit(self):
        """Deposit money into the user's account"""
        amount_input_field = self.deposit_bar.get()  # get the input box object
        try:
            amount = int(
                amount_input_field
            )  # convert the input box object to an integer to get the amount
        except:
            messagebox.showerror("B.A.T.E", "Invalid input! Please try again")
            self.deposit_bar.delete(0, END)
            return

        if amount < 100000 or amount > 100000000:
            messagebox.showerror("B.A.T.E", "Invalid amount! Please try again")
            self.deposit_bar.delete(0, END)
            return

        self.rep = messagebox.askyesno(
            "B.A.T.E", f"Do you want to deposit: {amount} VND?"
        )
        if self.rep == 1:
            self.system.logged_in_user.balance += amount
            self.show_current_balance = ctk.CTkLabel(
                self.balance_frame,
                text="Current balance: "
                + str(self.system.logged_in_user.balance)
                + " VND",
                font=("Helvetica", 19, "bold"),
                text_color="black",
            )
            self.show_current_balance.place(x=20, y=120)
            transaction = {
                "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "amount": amount,
                "description": "deposit",
            }
            self.update_transaction_history(transaction)
            self.system.logged_in_user.transaction_history.append(transaction)
            self.deposit_bar.delete(0, END)
            self.system.flush_data_to_json()

    # Function to display transaction history
    def display_transaction_history(self):
        transactions = self.system.logged_in_user.transaction_history
        # check if the list is empty
        if not transactions:  
         self.history = ctk.CTkLabel(
             self.transaction_history_frame,
             text="No transactions available",
             font=("Helvetica", 16, "bold"),
             text_color="black",
         )
         self.history.grid(row=0, column=0, pady=5)
         return
        for i, transaction in enumerate(transactions):
            if transaction["description"] == "deposit":
                transaction_amount = "+ {} VND".format(abs(int(transaction["amount"])))
            else:
                transaction_amount = "- {} VND".format(transaction["amount"])
            self.history = ctk.CTkLabel(
                self.transaction_history_frame,
                text="Transaction "
                + str(i + 1)
                + ": "
                + transaction_amount,
                font=("Helvetica", 16, "bold"),
                text_color="black",
            )
            self.history.grid(row=i, column=0, pady=5)

    # Destroy the current window and return to the main window
    def back_to_main(self):
        self.root.destroy()
        domains.gui_helpers.BateMain.BateMain(system=self.system, web=self.web).run()

    def update_transaction_history(self, transaction):
        """Update transaction history into logged in user's account"""
        if isinstance(transaction, dict) and "amount" in transaction:
            num_transactions = len(self.system.logged_in_user.transaction_history)
            self.system.logged_in_user.transaction_history.append(transaction) 
            if transaction["description"] == "deposit":
                transaction_amount = "+ {} VND".format(abs(transaction["amount"]))
            else:
                transaction_amount = "- {} VND".format(transaction["amount"])
            if num_transactions == 0:
                self.history = ctk.CTkLabel(
                    self.transaction_history_frame,
                    text="Transaction "
                    + str(num_transactions)
                    + ": "
                    + transaction_amount
                    + " Date: "
                    + datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    font=("Helvetica", 16, "bold"),
                    text_color="black",
                )
                self.history.grid(row=0, column=0, pady=5)
            else: # if the transaction history is not empty
                self.history = ctk.CTkLabel(
                    self.transaction_history_frame,
                    text="Transaction "
                    + str(num_transactions)
                    + ": "
                    + transaction_amount
                    + " Date: "
                    + datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    font=("Helvetica", 16, "bold"),
                    text_color="black",
                )
                self.history.grid(row=num_transactions - 1, column=0, pady=5)
        else:
            print("Error updating transaction history: invalid transaction")


    def main_frame(self):
        self.main_title_frame = ctk.CTkFrame(
            self.root, height=80, fg_color="light blue"
        )
        self.main_title_frame.pack(side=TOP, fill="x")
        self.main_title_frame.pack_propagate(FALSE)
        self.content_frame = ctk.CTkFrame(self.root, height=420)
        self.content_frame.pack_propagate(FALSE)
        self.content_frame.configure(fg_color="dark cyan")
        self.content_frame.pack(side=TOP, fill="x")

        self.main_title = ctk.CTkLabel(
            self.main_title_frame,
            text="Money Management System",
            font=("Bodoni", 32, "bold"),
            text_color="black",
        )
        self.main_title.pack(pady=20)

        self.return_button = ctk.CTkButton(
            self.content_frame,
            text="Return",
            width=5,
            command=self.back_to_main,
            fg_color="light blue",
            text_color="black",
        )
        self.return_button.pack(side=BOTTOM, pady=10)

    def deposit_menu(self):
        self.deposit_frame = ctk.CTkFrame(
            self.content_frame,
            height=160,
            width=350,
            corner_radius=10,
            fg_color="light blue",
        )
        self.deposit_frame.place(x=20, y=30)
        self.deposit_frame.pack_propagate(FALSE)

        self.deposit_frame_title = ctk.CTkLabel(
            self.deposit_frame,
            text="Deposit Menu",
            font=("Bodoni", 25, "bold"),
            text_color="black",
            fg_color="light blue",
        )
        self.deposit_frame_title.pack(pady=3)
        self.deposit_frame_text = ctk.CTkLabel(
            self.deposit_frame,
            text="Please enter the amount you'd like to deposit!",
            font=("Helvetica", 16, "italic"),
            fg_color="light blue",
            text_color="black",
        ).pack()
        self.note = ctk.CTkLabel(
            self.deposit_frame,
            text="-Must be over 100k and under 100m VND-",
            font=("Helvetica", 15, "italic", "bold"),
            text_color="dark cyan",
        ).pack()

        self.deposit_bar = ctk.CTkEntry(
            self.deposit_frame,
            width=100,
            border_width=3,
            corner_radius=10,
            border_color="dark cyan",
            fg_color="light cyan",
            text_color="black",
        )
        self.deposit_bar.place(x=160, y=90)
        self.money_sign = ctk.CTkLabel(
            self.deposit_frame,
            text="VND",
            font=("Helvetica", 16, "bold"),
            text_color="black",
        ).place(x=285, y=86)
        self.text = ctk.CTkLabel(
            self.deposit_frame,
            text="Depositing:",
            font=("Helvetica", 16, "bold"),
            text_color="black",
        ).place(x=20, y=86)

        self.deposit_button = ctk.CTkButton(
            self.deposit_frame,
            text="Deposit",
            font=("Bodoni", 16, "bold"),
            command=self.action_deposit,
            fg_color="dark cyan",
            text_color="black",
        )
        self.deposit_button.pack(side=BOTTOM, pady=6)

    def balance_menu(self):
        self.balance_frame = ctk.CTkFrame(
            self.content_frame,
            height=160,
            width=350,
            corner_radius=10,
            fg_color="light blue",
        )
        self.balance_frame.place(x=20, y=210)
        self.balance_frame.pack_propagate(FALSE)

        self.balance_frame_title = ctk.CTkLabel(
            self.balance_frame,
            text="Current Balance",
            font=("Bodoni", 25, "bold"),
            text_color="black",
            fg_color="light blue",
        )
        self.balance_frame_title.pack()
        self.balance_frame_text = ctk.CTkLabel(
            self.balance_frame,
            text="Please check your account's balance\nIf there's any problem, report to an admin!",
            font=("Helvetica", 16, "italic"),
            text_color="black",
        ).pack()

        self.show_current_user = ctk.CTkLabel(
            self.balance_frame,
            text="Current user: " + self.system.logged_in_user.username,
            font=("Helvetica", 19, "bold"),
            text_color="black",
        ).place(x=20, y=80)

        self.show_current_balance = ctk.CTkLabel(
            self.balance_frame,
            text="Current balance: " + str(self.system.logged_in_user.balance) + " VND",
            font=("Helvetica", 19, "bold"),
            text_color="black",
        ).place(x=20, y=120)

    def history_menu(self):
        self.history_frame = ctk.CTkFrame(
            self.content_frame, height=340, width=420, fg_color="light blue"
        )
        self.history_frame.place(x=380, y=30)
        self.history_frame.pack_propagate(FALSE)

        self.history_title = ctk.CTkLabel(
            self.history_frame,
            text="Transaction History",
            font=("Bodoni", 25, "bold"),
            text_color="black",
            fg_color="light blue",
        )
        self.history_title.pack(pady=3)
        self.transaction_history_frame = ctk.CTkScrollableFrame(
            self.history_frame, height=230, width=400, fg_color="light blue"
        )
        self.transaction_history_frame.pack(pady=3)
        self.transaction_history_frame.pack_propagate(FALSE)

    def run(self):
        self.root.mainloop()
