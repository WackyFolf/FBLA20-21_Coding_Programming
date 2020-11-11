import tkinter
from tkinter import *
import sys
from reader import reader
from functools import partial

reader = reader("ques", "1")
root = Tk()
root.title('UI Testing')
frame = LabelFrame(root, padx=5, pady=5, text="Start a Quiz")
frame.pack(padx=10, pady=10, side = LEFT)
frame2 = LabelFrame(root, padx=5, pady=5, text="End This Program")
frame2.pack(padx=10, pady=10, side = RIGHT)

def exitProgram():
    sys.exit() 
def obtainInfo(want, num):
    label.config(text = (reader.read(want, num)))
    print(reader.read("ques", "2"))
b = Button(frame, text="Question 1", command=partial(obtainInfo, "ques", "1"))
b.grid(row=1, column=0)
b2 = Button(frame, text="Question 2", command=partial(obtainInfo, "ques", "2"))
b2.grid(row=1, column=1)
b3 = Button(frame, text="Question 3", command=partial(obtainInfo, "ques", "3"))
b3.grid(row=1, column=2)
b3 = Button(frame2, text="Exit", command=exitProgram)
b3.grid(row=0, column=0)
label = Label(frame, text="Click a button for a question.")
label.grid(row=0,column=0)
root.mainloop()