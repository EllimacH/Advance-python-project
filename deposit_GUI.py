import customtkinter as ctk
from customtkinter import *
from tkinter import messagebox

class BateMoney:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("B.A.T.E Internet")
        self.root.geometry("820x500")
        self.root.resizable(FALSE, FALSE)
        self.root._apply_appearance_mode("system")

        global balance
        self.main_frame()
        self.deposit_menu()
        self.balance_menu()
        self.history_menu()

 
    def deposit(self):
        global amount
        global balance
        self.balance = 0
        self.amount = self.deposit_bar.get()
        if int(self.amount) >= 100000 and int(self.amount) <= 100000000:
            self.rep = messagebox.askyesno("B.A.T.E", "Do you want to deposit: " + self.amount + " VND?")
            if self.rep == 1:
                self.balance += int(self.amount)
                messagebox.showinfo("B.A.T.E", "Deposit Successful!")
                self.deposit_bar.delete(0, END)
            else:
                self.deposit_bar.delete(0, END)
        elif int(self.amount) < 100000:
            messagebox.showerror("B.A.T.E", "Insufficient amount! Please try again")
            self.deposit_bar.delete(0, END)
        elif int(self.amount) > 100000000:
            messagebox.showerror("B.A.T.E", "Exceeded maximum amount! Please try again")
            self.deposit_bar.delete(0, END)
        else:
            messagebox.showerror("B.A.T.E","Invalid input! Please try again")
            self.deposit_bar.delete(0, END)


    def main_frame(self):
        self.main_title_frame = ctk.CTkFrame(self.root, height=80, fg_color="light blue")
        self.main_title_frame.pack(side=TOP, fill="x")
        self.main_title_frame.pack_propagate(FALSE)
        self.content_frame = ctk.CTkFrame(self.root, height=420)
        self.content_frame.pack_propagate(FALSE)
        self.content_frame.configure(fg_color="dark cyan")
        self.content_frame.pack(side=TOP, fill="x")

        self.main_title = ctk.CTkLabel(self.main_title_frame, text="---Money Management System---", font=("Bodoni",32,"bold"), text_color="black")
        self.main_title.pack(pady=20)

        self.return_button = ctk.CTkButton(self.content_frame, text="Return", width=5, command=self.root.quit, fg_color="light blue", text_color="black")
        self.return_button.pack(side=BOTTOM, pady=10)


    def deposit_menu(self):
        self.deposit_frame = ctk.CTkFrame(self.content_frame, height=160, width=350, corner_radius=10, fg_color="light blue")
        self.deposit_frame.place(x=20, y=30)
        self.deposit_frame.pack_propagate(FALSE)

        self.deposit_frame_title = ctk.CTkLabel(self.deposit_frame, text="---Deposit Menu---", font=("Bodoni",25,"bold"), text_color="black", fg_color="light blue")
        self.deposit_frame_title.pack(pady=3)
        self.deposit_frame_text = ctk.CTkLabel(self.deposit_frame, text="Please enter the amount you'd like to deposit!", font=("Helvetica",16,"italic"), fg_color="light blue", text_color="black").pack()
        self.note = ctk.CTkLabel(self.deposit_frame, text="-Must be over 100k and under 100m VND-", font=("Helvetica",15,"italic","bold"), text_color="dark cyan").pack()

        self.deposit_bar = ctk.CTkEntry(self.deposit_frame, width=100, border_width=3, corner_radius=10, border_color="dark cyan", fg_color="light cyan", text_color="black")
        self.deposit_bar.place(x=160,y=90)
        self.money_sign = ctk.CTkLabel(self.deposit_frame, text="VND", font=("Helvetica",16,"bold"), text_color="black").place(x=285,y=86)
        self.text = ctk.CTkLabel(self.deposit_frame, text="Depositing:", font=("Helvetica",16,"bold"), text_color="black").place(x=20,y=86)

        self.deposit_button = ctk.CTkButton(self.deposit_frame, text="Deposit", font=("Bodoni",16,"bold"), command=self.deposit, fg_color="dark cyan", text_color="black")
        self.deposit_button.pack(side=BOTTOM, pady=6)


    def balance_menu(self):
        self.balance_frame = ctk.CTkFrame(self.content_frame, height=160, width=350, corner_radius=10, fg_color="light blue")
        self.balance_frame.place(x=20, y=210)
        self.balance_frame.pack_propagate(FALSE)

        self.balance_frame_title = ctk.CTkLabel(self.balance_frame, text="---Current Balance---", font=("Bodoni",25,"bold"), text_color="black", fg_color="light blue")
        self.balance_frame_title.pack()
        self.balance_frame_text = ctk.CTkLabel(self.balance_frame, text="Please check your account's balance\nIf there's any problem, report to an admin!", font=("Helvetica",16,"italic"), text_color="black").pack()

        self.show_current_user = ctk.CTkLabel(self.balance_frame, text="Current user:", font=("Helvetica",19,"bold"), text_color="black").place(x=20,y=80)

        self.show_current_balance = ctk.CTkLabel(self.balance_frame, text="Current balance: " + " VND", font=("Helvetica",19,"bold"), text_color="black").place(x=20,y=120)


    def history_menu(self):
        self.history_frame = ctk.CTkFrame(self.content_frame, height=340, width=420, fg_color="light blue")
        self.history_frame.place(x=380, y=30)
        self.history_frame.pack_propagate(FALSE)

        self.history_title = ctk.CTkLabel(self.history_frame, text="---Transaction History---", font=("Bodoni",25,"bold"), text_color="black", fg_color="light blue")
        self.history_title.pack(pady=3)
        # NEED TO ADD FUNCTION TO SHOW HISTORY (PRINT OUT MONEY DEPOSITED AND WITHDRAWN WITH CORRECT TIME AND DATE)

    def run(self):
        self.root.mainloop()


bate = BateMoney()
bate.run()