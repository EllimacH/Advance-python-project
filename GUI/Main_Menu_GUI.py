from tkinter import *
import datetime
from tkinter import messagebox
from PIL import ImageTk,Image


# Creating a root for GUI
menu = Tk()
menu.geometry("580x375")
menu.title('B.A.T.E Internet')
menu.config(bg="light cyan")
menu.resizable(0,0)


# Function for the "Return" button
def log_out():
    rep = messagebox.askyesno("B.A.T.E", "Do you want to sign out?")
    if rep == 1:
        menu.destroy()
        import Login_System_GUI


# Function to greet customers with correct phrases according to time
def greeting():
    currentTime = datetime.datetime.now()
    currentTime.hour
    if currentTime.hour < 12:
        morn_text = Label(frame, text="-Good morning! What would you like to do today?-", font=("Helvetica",12,"italic"))
        morn_text.grid(row=1, column=0, columnspan=3)
    elif currentTime.hour >= 12 and currentTime.hour < 18:
        aft_text = Label(frame, text="-Good afternoon! What would you like to do today?-", font=("Helvetica",12,"italic"))
        aft_text.grid(row=1, column=0, columnspan=3)
    else:
        eve_text = Label(frame, text="-Good evening! What would you like to do tonight?-", font=("Helvetica",12,"italic"))
        eve_text.grid(row=1, column=0, columnspan=3)

    
# Function for users to deposit money into their accounts
balance = 0
def deposit():
    global amount
    global balance
    amount = money.get()
    if int(amount) >= 100000:
        balance += int(amount)
        messagebox.showinfo("B.A.T.E","Success! The amount you've deposited is: " + str(amount) + " VND")
        money.delete(0, END)
    elif int(amount) < 100000:
        messagebox.showerror("B.A.T.E","Insufficient amount! Please try again")
        money.delete(0, END)
    

# Function for users to check their balances
def check_balance():
    return


# Function for users to check available products to purchase 
def check_product():
    return


# Function for users to buy selected products
def buy_product():
    return


# Function for users to check their current plans and renew/cancel those plans
def current_plan():
    return


# Function for the deposit GUI
def deposit_menu():
    top = Toplevel()
    top.title("B.A.T.E")
    top.geometry("350x280")
    top.resizable(0,0)

    frame = LabelFrame(top, padx=20, pady=20)
    frame.pack(padx=10, pady=10)

    Title = Label(frame, text="---DEPOSIT MENU---", font=("Bodoni",20,"bold"), padx=5, pady=2)
    Title.grid(row=0, column=0, columnspan=3)

    text = Label(frame, text="-Please enter the amount you'd like to deposit!-", font=("Helvetica",10,"italic"), padx=2)
    text.grid(row=1, column=0, columnspan=3)
    text1 = Label(frame, text="- Must be over 100,000 VND -", font=("Helvetica",10,"bold"), padx=2).grid(row=2, column=0, columnspan=3)

    global money
    money = Entry(frame, width=13, borderwidth=3)
    money_sign = Label(frame, text="VND", font=("Helvetica",10,"bold")).grid(row=3, column=2)
    text2 = Label(frame, text="Depositing: ", font=("Helvetica",10,"bold")).grid(row=3, column=0)
    money.grid(row=3, column=1)

    deposit_button = Button(frame, text="ENTER", font=("Helvetica",13,"bold"), padx=11, pady=7, command=deposit)
    decor1 = Label(frame, text="", font=("Helvetica",14,"bold")).grid(row=4, column=0, columnspan=3)
    deposit_button.grid(row=5, column=0, columnspan=3)

    back_button = Button(top, text="Return", command=top.destroy)
    back_button.pack()


# Function for the balance GUI
def check_balance_menu():
    top = Toplevel()
    top.title("B.A.T.E")
    top.geometry("350x210")
    top.resizable(0,0)

    frame = LabelFrame(top, padx=20, pady=20)
    frame.pack(padx=10, pady=10)

    Title = Label(frame, text="---CURRENT BALANCE---", font=("Bodoni",17,"bold"), padx=3, pady=2)
    Title.grid(row=0, column=0, columnspan=3)

    text = Label(frame, text="-Please check if your balance number is correct!-", font=("Helvetica",10,"italic"), padx=2)
    text.grid(row=1, column=0, columnspan=2)

    text2 = Label(frame, text="Current user: ", font=("Helvetica",11,"bold"), padx=1)
    text2.grid(row=2, column=0)

    text3 = Label(frame, text="Current balance: ", font=("Helvetica",11,"bold"), padx=5)
    text3.grid(row=3, column=0)

    money_text = Label(frame, text=str(balance) + " VND", font=("Helvetica",10,"italic"))
    money_text.grid(row=3, column=1, columnspan=2)

    back_button = Button(top, text="Return", command=top.destroy)
    back_button.pack()


# Function for the market GUI
def check_product_menu():
    # Function for the forward button
    def forward(image_number):
        global my_display
        global forward_button
        global backward_button

        # Clear the screen and display the next image
        my_display.grid_forget()
        my_display = Label(frame, image=product_list[image_number-1])
        forward_button = Button(frame, text=">>", font=("Helvetica",11,"bold"), padx=10, pady=3, command= lambda: forward(image_number+1))
        backward_button = Button(frame, text="<<", font=("Helvetica",11,"bold"), padx=10, pady=3, command= lambda: backward(image_number-1))
    
        my_display.grid(row=2, column=0, columnspan=3)
        forward_button.grid(row=4, column=2)
        backward_button.grid(row=4, column=0)

        # Disable the forward button when the last image is displayed
        if image_number == 4:
            forward_button = Button(frame, text=">>", font=("Helvetica",11,"bold"), padx=10, pady=3, state=DISABLED)
            forward_button.grid(row=4, column=2)
       

    # Function for the backward button
    def backward(image_number):
        global my_display
        global forward_button
        global backward_button

        # Clear the screen and display the previous image
        my_display.grid_forget()
        my_display = Label(frame, image=product_list[image_number-1])
        forward_button = Button(frame, text=">>", font=("Helvetica",11,"bold"), padx=10, pady=3, command= lambda: forward(image_number+1))
        backward_button = Button(frame, text="<<", font=("Helvetica",11,"bold"), padx=10, pady=3, command= lambda: backward(image_number-1))
    
        my_display.grid(row=2, column=0, columnspan=3)
        forward_button.grid(row=4, column=2)
        backward_button.grid(row=4, column=0)

        # Disable the backward button when the first image is displayed
        if image_number == 1:
            backward_button = Button(frame, text="<<", font=("Helvetica",11,"bold"), padx=10, pady=3, state=DISABLED)
            backward_button.grid(row=4, column=0)


    top = Toplevel()
    top.title("B.A.T.E")
    top.geometry("605x320")
    top.resizable(0,0)

    frame = LabelFrame(top, padx=20, pady=20)
    frame.pack(padx=10, pady=10)

    label = Label(frame, text="---PRODUCT MENU---", font=("Bodoni",20,"bold"), padx=8, pady=2)
    label.grid(row=0, column=0, columnspan=3)

    text = Label(frame, text="-If you want to purchase, press 'Return' and select 'Buy product'!-", font=("Helvetica",10,"italic"), padx=2)
    text.grid(row=1, column=0, columnspan=3)

    bronze = ImageTk.PhotoImage(Image.open("D:\Studying\Adv.Python\GUI\Basics\Images/bronze.png"))
    silver = ImageTk.PhotoImage(Image.open("D:\Studying\Adv.Python\GUI\Basics\Images\silver.png"))
    gold = ImageTk.PhotoImage(Image.open("D:\Studying\Adv.Python\GUI\Basics\Images/gold.png"))
    diamond = ImageTk.PhotoImage(Image.open("D:\Studying\Adv.Python\GUI\Basics\Images/diamond.png"))
    
    # Create a list of images
    global product_list
    product_list = [bronze, silver, gold, diamond]
    # Display the first image and the rest of the images
    global my_display
    my_display = Label(frame, image=bronze, pady=5)
    my_display.grid(row=2, column=0, columnspan=3)

    forward_button = Button(frame, text=">>", font=("Helvetica",11,"bold"), padx=10, pady=3, command= lambda: forward(2))
    forward_button.grid(row=4, column=2)

    backward_button = Button(frame, text="<<", font=("Helvetica",11,"bold"), padx=10, pady=3, command=lambda: backward(1))
    backward_button.grid(row=4, column=0)

    back_button = Button(top, text="Return", command=top.destroy)
    back_button.pack()


# Function for the purchasing GUI
def buy_product_menu():
    top = Toplevel()
    top.title("B.A.T.E")
    top.geometry("605x320")
    top.resizable(0,0)

    frame = LabelFrame(top, padx=20, pady=20)
    frame.pack(padx=10, pady=10)

    label = Label(frame, text="---PURCHASING MENU---", font=("Bodoni",20,"bold"), padx=8, pady=2)
    label.grid(row=0, column=0, columnspan=3)

    back_button = Button(top, text="Return", command=top.destroy)
    back_button.pack()


# Function for the current plan GUI
def current_plan_menu():
    top = Toplevel()
    top.title("B.A.T.E")
    top.geometry("605x320")
    top.resizable(0,0)

    frame = LabelFrame(top, padx=20, pady=20)
    frame.pack(padx=10, pady=10)

    label = Label(frame, text="---CURRENT PLAN MENU---", font=("Bodoni",20,"bold"), padx=8, pady=2)
    label.grid(row=0, column=0, columnspan=3)

    back_button = Button(top, text="Return", command=top.destroy)
    back_button.pack()


# Creating and displaying frame for main menu 
frame = LabelFrame(menu, padx=10, pady=20)
frame.pack(padx=20, pady=20)


# Creating and displaying the main title in main menu
Title = Label(frame, text="---WELCOME TO B.A.T.E SYSTEM---", font=("Bodoni",19,"bold"), padx=7, pady=2)
Title.grid(row=0, column=0, columnspan=3)


# Call the greeting() function below the main title
greeting()


# Creating and displaying widgets for Buttons
opt1 = Button(frame, text="1. Deposit", padx=5, pady=5, command=deposit_menu)
opt1.grid(row=2, column=0, columnspan=3)
opt2 = Button(frame, text="2. Check balance", padx=5, pady=5, command=check_balance_menu)
opt2.grid(row=3, column=0, columnspan=3)
opt3 = Button(frame, text="3. Check product", padx=5, pady=5, command=check_product_menu)
opt3.grid(row=4, column=0, columnspan=3)
opt4 = Button(frame, text="4. Buy product", padx=5, pady=5, command=buy_product_menu)
opt4.grid(row=5, column=0, columnspan=3)
opt5 = Button(frame, text="5. Check current plan", padx=5, pady=5, command=current_plan_menu)
opt5.grid(row=6, column=0, columnspan=3)


# Creating and displaying a "Sign out" button
button = Button(menu, text="Sign out", command=log_out)
button.pack()

menu.mainloop()