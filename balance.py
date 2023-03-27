class balance:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
    def display(self):
        print("\n Net Available Balance=",self.balance)


#run the program
s = balance()
s.deposit()
s.withdraw()
s.display()


# # """ Here is the explanation for the code above:
# 1. The class is named "balance" and is defined with the __init__ method
# 2. This method has the balance attribute of the class set to 0
# 3. The deposit method is defined with the amount inputted by the user
# 4. The balance is added to the amount and printed
# 5. The withdraw method is defined with the amount inputted by the user
# 6. The balance is subtracted from the amount and printed if the balance is greater or equal to the amount
# 7. The display method is defined with the balance printed """

