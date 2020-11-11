import tkinter
from tkinter import *
import sys
from reader import reader
from functools import partial
from quizUI import quizUI

reader = reader("ques", "1", "test")
quizUI = quizUI('quiz')
root = Tk()
root.title('Quiz Program')

variable=StringVar(root)
variable.set("Question") # Sets default value

frame = LabelFrame(root, padx=5, pady=5, text="Start a Quiz")
frame.pack(padx=10, pady=10, side = LEFT)
frame2 = LabelFrame(root, padx=5, pady=5, text="End This Program")
frame2.pack(padx=10, pady=10, side = RIGHT)

def exitProgram():
    quizUI.openQuiz("quiz")
    sys.exit() 
def obtainInfo(num):
    want = optionDict.get(variable.get()) # Define want as the dictionary definition for the current variable of the dropdown
    label.config(text = (reader.read(want, num, "computerapps")))
options = OptionMenu(frame, variable, "Question", "Answer", "Alternate 1", "Alternate 2", "Alternate 3")
optionDict = {
    "Question": "ques",
    "Answer": "ans",
    "Alternate 1": "alt1",
    "Alternate 2": "alt2",
    "Alternate 3": "alt3"
}
options.grid(row=2,column=0)
b = Button(frame, text="Question 1", command=partial(obtainInfo, "1"))
b.grid(row=1, column=0)
b2 = Button(frame, text="Question 2", command=partial(obtainInfo, "2"))
b2.grid(row=1, column=1)
b3 = Button(frame, text="Question 3", command=partial(obtainInfo, "3"))
b3.grid(row=1, column=2)
b3 = Button(frame2, text="Exit", command=exitProgram)
b3.grid(row=0, column=0)
label = Label(frame, text="Click a button for a question.")
label.grid(row=0,column=0)
root.mainloop()