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
    else:
        messagebox.showerror("B.A.T.E","Invalid input! Please try again")
        money.delete(0, END)


# Function for users to select products
def select_product():
    return


# Function for users to purchase products and subtract their balance
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

    text = Label(frame, text="-Please enter the amount you'd like to deposit!-", font=("Helvetica",10,"italic"), pady=2)
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

    Title = Label(frame, text="---CURRENT BALANCE---", font=("Bodoni",17,"bold"))
    Title.grid(row=0, column=0, columnspan=3)

    text = Label(frame, text="-Please check if your balance number is correct!-", font=("Helvetica",10,"italic"))
    text.grid(row=1, column=0, columnspan=3)

    text2 = Label(frame, text="Current user: ", font=("Helvetica",11,"bold"), padx=1)
    text2.grid(row=2, column=0)

    text3 = Label(frame, text="Current balance: ", font=("Helvetica",11,"bold"), padx=5)
    text3.grid(row=3, column=0)

    money_text = Label(frame, text=str(balance) + " VND", font=("Helvetica",10,"italic"))
    money_text.grid(row=3, column=1, columnspan=2)

    back_button = Button(top, text="Return", command=top.destroy)
    back_button.pack()


# Function for the forward button
def forward(image_number): #, text_number):
    global my_display
    # global my_display_text
    global forward_button
    global backward_button

    # Clear the screen and display the next image
    my_display.grid_forget()
    # my_display_text.grid_forget()
    my_display = Label(frame1, image=product_list[image_number-1])
    # my_display_text = Label(frame1, text=product_text_list[text_number-1], font=("Helvetica",11,"italic"))
    forward_button = Button(frame1, text=">>", font=("Helvetica",11,"bold"), padx=10, pady=3, command= lambda: forward(image_number+1))#, text_number+1))
    backward_button = Button(frame1, text="<<", font=("Helvetica",11,"bold"), padx=10, pady=3, command= lambda: backward(image_number-1))#, text_number-1))
    
    my_display.grid(row=2, column=0, columnspan=3)
    forward_button.grid(row=4, column=2)
    backward_button.grid(row=4, column=0)

    # Disable the forward button when the last image is displayed
    if image_number == 4:
        forward_button = Button(frame1, text=">>", font=("Helvetica",11,"bold"), padx=10, pady=3, state=DISABLED)
        forward_button.grid(row=4, column=2)
       

# Function for the backward button
def backward(image_number): #, text_number):
    global my_display
    # global my_display_text
    global forward_button
    global backward_button

    # Clear the screen and display the previous image
    my_display.grid_forget()
    # my_display_text.grid_forget()
    my_display = Label(frame1, image=product_list[image_number-1])
    #my_display_text = Label(frame1, text=product_text_list[text_number-1], font=("Helvetica",11,"italic"))
    forward_button = Button(frame1, text=">>", font=("Helvetica",11,"bold"), padx=10, pady=3, command= lambda: forward(image_number+1))#,text_number+1))
    backward_button = Button(frame1, text="<<", font=("Helvetica",11,"bold"), padx=10, pady=3, command= lambda: backward(image_number-1))#, text_number-1))
    
    my_display.grid(row=2, column=0, columnspan=3)
    forward_button.grid(row=4, column=2)
    backward_button.grid(row=4, column=0)

    # Disable the backward button when the first image is displayed
    if image_number == 1:
        backward_button = Button(frame1, text="<<", font=("Helvetica",11,"bold"), padx=10, pady=3, state=DISABLED)
        backward_button.grid(row=4, column=0)


# Displaying the main product menu
def check_product_menu():
    top = Toplevel()
    top.title("B.A.T.E")
    top.geometry("350x210")
    top.resizable(0,0)

    frame = LabelFrame(top, padx=20, pady=20)
    frame.pack(padx=10, pady=10)

    label = Label(frame, text="---PRODUCT MENU---", font=("Bodoni",20,"bold"))
    label.grid(row=0, column=0, columnspan=3)

    text = Label(frame, text="-What product would you like to see?-", font=("Helvetica",12,"italic"), pady=3)
    text.grid(row=1, column=0, columnspan=3)

    internet_data_button = Button(frame, text="Data package", font=("Helvetica",11,"bold"), pady=5, command=internet_data)
    internet_data_button.grid(row=2, column=0)
    
    web_service_button = Button(frame, text="Web service", font=("Helvetica",11,"bold"), pady=5, command=web_service)
    web_service_button.grid(row=2, column=2)

    back_button = Button(top, text="Return", command=top.destroy)
    back_button.pack()


# Creating and displaying the internet data package menu
def internet_data():
    top = Toplevel()
    top.title("B.A.T.E")
    top.geometry("605x320")
    top.resizable(0,0)

    global frame1
    frame1 = LabelFrame(top, padx=20, pady=20)
    frame1.pack(padx=10, pady=10)

    label = Label(frame1, text="---DATA PACKAGE---", font=("Bodoni",20,"bold"), pady=2)
    label.grid(row=0, column=0, columnspan=3)

    text = Label(frame1, text="-If you want to purchase, return to the main menu and select 'Buy product'!-", font=("Helvetica",12,"italic"), padx=2)
    text.grid(row=1, column=0, columnspan=3)

            # Creating the images for the products
    bronze = ImageTk.PhotoImage(Image.open("D:\Studying\Adv.Python\GUI\Basics\Images/bronze.png"))
    silver = ImageTk.PhotoImage(Image.open("D:\Studying\Adv.Python\GUI\Basics\Images\silver.png"))
    gold = ImageTk.PhotoImage(Image.open("D:\Studying\Adv.Python\GUI\Basics\Images/gold.png"))
    diamond = ImageTk.PhotoImage(Image.open("D:\Studying\Adv.Python\GUI\Basics\Images/diamond.png"))
            
            # Creating the descriptions for the products
            # bronze_text = Label(frame, text="-Bronze: 50,000VND, 5GB/month-", font=("Helvetica",11,"italic"), padx=5, pady=2)
            # silver_text = Label(frame, text="-Silver: 100,000VND, 10GB/month-", font=("Helvetica",11,"italic"), padx=5, pady=2)
            # gold_text = Label(frame, text="-Gold: 150,000VND, 15GB/month-", font=("Helvetica",11,"italic"), padx=5, pady=2)
            # diamond_text = Label(frame, text="-Diamond: 200,000VND, 20GB/month-", font=("Helvetica",11,"italic"), padx=5, pady=2)
            
            # Create a list of descriptions
            # global product_text_list
            # product_text_list = [bronze_text, silver_text, gold_text, diamond_text]
            # Display the first description and the rest of the descriptions
            # global my_display_text
            # my_display_text = Label(frame, text=bronze_text, font=("Helvetica",11,"italic"), pady=5)
            # my_display_text.grid(row=3, column=0, columnspan=3)

            # Create a list of images
    global product_list
    product_list = [bronze, silver, gold, diamond]

            # Display the first image and the rest of the images
    global my_display
    my_display = Label(frame1, image=bronze, pady=5)
    my_display.grid(row=2, column=0, columnspan=3)

            # Create the forward and backward buttons
    forward_button = Button(frame1, text=">>", font=("Helvetica",11,"bold"), padx=10, pady=3, command= lambda: forward(2))#, 2))
    forward_button.grid(row=4, column=2)

    backward_button = Button(frame1, text="<<", font=("Helvetica",11,"bold"), padx=10, pady=3, command=backward, state=DISABLED)
    backward_button.grid(row=4, column=0)

    back_button = Button(top, text="Return", command=top.destroy)
    back_button.pack()


# Creating and displaying the web service menu
def web_service():
    top = Toplevel()
    top.title("B.A.T.E")
    top.geometry("605x320")
    top.resizable(0,0)

    frame = LabelFrame(top, padx=20, pady=20)
    frame.pack(padx=10, pady=10)
    
    label = Label(frame, text="---WEB SERVICE---", font=("Bodoni",20,"bold"), pady=2)
    label.grid(row=0, column=0, columnspan=3)

    text = Label(frame, text="-If you want to purchase, return to the main menu and select 'Buy product'!-", font=("Helvetica",12,"italic"), padx=2)
    text.grid(row=1, column=0, columnspan=3)

    # Creating and displaying the service packages
    title1 = Label(frame, text="---Service Package---", font=("Helvetica",13,"bold"), pady=2)
    title1.grid(row=2, column=0)

    pack1 = Label(frame, text="Basic: 200,000 VND/year", font=("Helvetica",10,"italic"), padx=5, pady=2)
    pack2 = Label(frame, text="Advanced: 350,000 VND/2 years", font=("Helvetica",10,"italic"), padx=5, pady=2)
    pack3 = Label(frame, text="High End: 500,000 VND/3 years", font=("Helvetica",10,"italic"), padx=5, pady=2)
    pack4 = Label(frame, text="VIP: 800,000 VND/5 years", font=("Helvetica",10,"italic"), padx=5, pady=2)
    pack5 = Label(frame, text="VIP+: 1,850,000 VND/10 years", font=("Helvetica",10,"italic"), padx=5, pady=2)

    # Creating and displaying the VPN packages
    title2 = Label(frame, text="---VPN Package---", font=("Helvetica",13,"bold"), pady=2)
    title2.grid(row=2, column=2)

    vpn1 = Label(frame, text="Basic: 100,000 VND/year", font=("Helvetica",10,"italic"), padx=5, pady=2)
    vpn2 = Label(frame, text="Advanced: 150,000 VND/2 years", font=("Helvetica",10,"italic"), padx=5, pady=2)
    vpn3 = Label(frame, text="High End: 200,000 VND/3 years", font=("Helvetica",10,"italic"), padx=5, pady=2)
    vpn4 = Label(frame, text="VIP: 300,000 VND/5 years", font=("Helvetica",10,"italic"), padx=5, pady=2)
    vpn5 = Label(frame, text="VIP+: 500,000 VND/10 years", font=("Helvetica",10,"italic"), padx=5, pady=2)

    pack1.grid(row=3, column=0)
    pack2.grid(row=4, column=0)
    pack3.grid(row=5, column=0)
    pack4.grid(row=6, column=0)
    pack5.grid(row=7, column=0)

    vpn1.grid(row=3, column=2)
    vpn2.grid(row=4, column=2)
    vpn3.grid(row=5, column=2)
    vpn4.grid(row=6, column=2)
    vpn5.grid(row=7, column=2)

    back_button = Button(top, text="Return", command=top.destroy)
    back_button.pack()


# Function for the purchasing GUI
def buy_product_menu():
    top = Toplevel()
    top.title("B.A.T.E")
    top.geometry("950x640")
    top.resizable(0,0)

    frame = LabelFrame(top, padx=20, pady=20)
    frame.pack(padx=10, pady=10)

    label = Label(frame, text="---PURCHASING MENU---", font=("Bodoni",20,"bold"), padx=8, pady=2)
    label.grid(row=0, column=0)

    text = Label(frame, text="-Select the items you want to purchase!-", font=("Helvetica",13,"italic"), padx=2)
    text.grid(row=1, column=0)

    title3 = Frame(frame, width=650, height=600)
    title3.grid(row=2, column=0, columnspan=3)

    # Data packages
    title0 = Label(title3, text="1. Data Packages", font=("Helvetica",12,"bold"), pady=2, padx=5)
    item1 = Label(title3, text="Bronze: 50,000 VND, 5GB/month", font=("Helvetica",11,"italic"), pady=2, padx=5)
    item2 = Label(title3, text="Silver: 100,000 VND, 10GB/month", font=("Helvetica",11,"italic"), pady=2, padx=5)
    item3 = Label(title3, text="Gold: 150,000 VND, 15GB/month", font=("Helvetica",11,"italic"), pady=2, padx=5)
    item4 = Label(title3, text="Platinum: 200,000 VND, 20GB/month", font=("Helvetica",11,"italic"), pady=2, padx=5)
    # Service packages
    title1 = Label(title3, text="2. Service Packages", font=("Helvetica",12,"bold"), pady=2, padx=5)
    item5 = Label(title3, text="Basic: 200,000 VND/year", font=("Helvetica",11,"italic"), pady=2, padx=5)
    item6 = Label(title3, text="Advanced: 350,000 VND/2 years", font=("Helvetica",11,"italic"), pady=2, padx=5)
    item7 = Label(title3, text="High End: 500,000 VND/3 years", font=("Helvetica",11,"italic"), pady=2, padx=5)
    item8 = Label(title3, text="VIP: 800,000 VND/5 years", font=("Helvetica",11,"italic"), pady=2, padx=5)
    item9 = Label(title3, text="VIP+: 1,850,000 VND/10 years", font=("Helvetica",11,"italic"), pady=2, padx=5)
    # VPN packages
    title2 = Label(title3, text="3. VPN Packages", font=("Helvetica",12,"bold"), pady=2, padx=5)
    item10 = Label(title3, text="Basic: 100,000 VND/year", font=("Helvetica",11,"italic"), pady=2, padx=5)
    item11 = Label(title3, text="Advanced: 150,000 VND/2 years", font=("Helvetica",11,"italic"), pady=2, padx=5)
    item12 = Label(title3, text="High End: 200,000 VND/3 years", font=("Helvetica",11,"italic"), pady=2, padx=5)
    item13 = Label(title3, text="VIP: 300,000 VND/5 years", font=("Helvetica",11,"italic"), pady=2, padx=5)
    item14 = Label(title3, text="VIP+: 500,000 VND/10 years", font=("Helvetica",11,"italic"), pady=2, padx=5)

    # Displaying the data packages
    title0.grid(row=0, column=0)
    item1.grid(row=1, column=0)
    item2.grid(row=2, column=0)
    item3.grid(row=3, column=0)
    item4.grid(row=4, column=0)
    # Displaying the service packages
    title1.grid(row=5, column=0)
    item5.grid(row=6, column=0)
    item6.grid(row=7, column=0)
    item7.grid(row=8, column=0)
    item8.grid(row=9, column=0)
    item9.grid(row=10, column=0)
    # Displaying the VPN packages
    title2.grid(row=11, column=0)
    item10.grid(row=12, column=0)
    item11.grid(row=13, column=0)
    item12.grid(row=14, column=0)
    item13.grid(row=15, column=0)
    item14.grid(row=16, column=0)

    # Buttons for purchasing
    buy_button1 = Button(title3, text="Buy", padx= 5, pady=2, command=select_product).grid(row=1, column=1)
    buy_button2 = Button(title3, text="Buy", padx= 5, pady=2,command=select_product).grid(row=2, column=1)
    buy_button3 = Button(title3, text="Buy", padx= 5, pady=2,command=select_product).grid(row=3, column=1)
    buy_button4 = Button(title3, text="Buy", padx= 5, pady=2,command=select_product).grid(row=4, column=1)
    buy_button5 = Button(title3, text="Buy", padx= 5, pady=2,command=select_product).grid(row=6, column=1)
    buy_button6 = Button(title3, text="Buy", padx= 5, pady=2,command=select_product).grid(row=7, column=1)
    buy_button7 = Button(title3, text="Buy", padx= 5, pady=2,command=select_product).grid(row=8, column=1)
    buy_button8 = Button(title3, text="Buy", padx= 5, pady=2,command=select_product).grid(row=9, column=1)
    buy_button9 = Button(title3, text="Buy", padx= 5, pady=2,command=select_product).grid(row=10, column=1)
    buy_button10 = Button(title3, text="Buy", padx= 5, pady=2,command=select_product).grid(row=12, column=1)
    buy_button11 = Button(title3, text="Buy", padx= 5, pady=2,command=select_product).grid(row=13, column=1)
    buy_button12 = Button(title3, text="Buy", padx= 5, pady=2,command=select_product).grid(row=14, column=1)
    buy_button13 = Button(title3, text="Buy", padx= 5, pady=2,command=select_product).grid(row=15, column=1)
    buy_button14 = Button(title3, text="Buy", padx= 5, pady=2,command=select_product).grid(row=16, column=1)


    # Displaying the frame for transaction
    title5 = Frame(frame, width=350, height=300)
    title5.grid(row=2, column=3, columnspan=2)

    text = Label(title5, text="-Transaction-", font=("Helvetica",12,"bold"), padx=5)
    text.grid(row=0, column=0, columnspan=2)

    # Displaying the total price
    total = Label(title5, text="Total price: ", font=("Helvetica",12,"bold"), padx=5)
    total.grid(row=1, column=0)

    # Displaying the current balance
    blnce = Label(title5, text="Current balance: ", font=("Helvetica",12,"bold"), padx=5)
    blnce.grid(row=2, column=0)
    current_balance = Label(title5, text=str(balance) + " VND", font=("Helvetica",11,"italic"), padx=5)
    current_balance.grid(row=2, column=1, columnspan=2)

    # Displaying the purchase button
    purchase = Button(title5, text="Purchase", font=("Helvetica",15,"bold"), padx=10, pady=5, command=buy_product)
    purchase.grid(row=3, column=0, columnspan=3)

    back_button = Button(top, text="Return", command=top.destroy)
    back_button.pack()


# Function for the current plan GUI
def current_plan_menu():
    top = Toplevel()
    top.title("B.A.T.E")
    top.geometry("350x210")
    top.resizable(0,0)

    frame = LabelFrame(top, padx=20, pady=20)
    frame.pack(padx=10, pady=10)

    Title = Label(frame, text="---CURRENT PLAN---", font=("Bodoni",17,"bold"), padx=3, pady=2)
    Title.grid(row=0, column=0, columnspan=3)

    text = Label(frame, text="-Please check if your plan is correct!-", font=("Helvetica",12,"italic"), padx=2)
    text.grid(row=1, column=0, columnspan=2)

    text2 = Label(frame, text="Current user: ", font=("Helvetica",11,"bold"), padx=1)
    text2.grid(row=2, column=0)

    text3 = Label(frame, text="Current plan: ", font=("Helvetica",11,"bold"), padx=5)
    text3.grid(row=3, column=0)

    money_text = Label(frame)
    money_text.grid(row=3, column=1, columnspan=2)

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