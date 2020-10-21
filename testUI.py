import tkinter
from tkinter import *
import sys

root = Tk()
root.title('UI Testing')
frame = LabelFrame(root, padx=5, pady=5, text="Start a Quiz")
frame.pack(padx=10, pady=10, side = LEFT)
frame2 = LabelFrame(root, padx=5, pady=5, text="End This Program")
frame2.pack(padx=10, pady=10, side = RIGHT)

def exitProgram():
    sys.exit() 
b = Button(frame, text="Button")
b.grid(row=1, column=0)
b2 = Button(frame, text="Button")
b2.grid(row=1, column=1)
b3 = Button(frame2, text="Exit", command=exitProgram)
b3.grid(row=0, column=0)
label = Label(frame, text="I am a label").grid(row=0,column=0)
root.mainloop()