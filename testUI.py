import tkinter
from tkinter import *
import sys

root = Tk()
def buttonAction():
    sys.exit()
    print("Button pressed")
label1 = Label(root, text="How are you")
button = Button(root, text="Exit", padx=50, command=buttonAction).grid(row=1,column=1)
label2 = Label(root, text="Hello world").grid(row=2,column=2)

label1.grid(row=0,column=0)

root.mainloop()