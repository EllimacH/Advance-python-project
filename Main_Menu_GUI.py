import tkinter
from tkinter import *

root = Tk()
root.geometry("1280x720")
root.title('Welcome')

def logout():
    root.destroy()
    import Login_System_GUI

frame = LabelFrame(root, text="Welcome to the B.A.T.E. System", padx=400, pady=400)
frame.pack(padx=50, pady=50)

button = Button(frame, text="Logout", command=logout)
button.grid(row = 0, column = 0)

root.mainloop()