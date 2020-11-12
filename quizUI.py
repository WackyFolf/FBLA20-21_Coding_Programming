import tkinter
from tkinter import *
from reader import reader
reader = reader("ques", "1", "test")
optionDict = {
    "Test Quiz": "test",
    "Computer Applications": "computerapps",
    "Alternate 1": "alt1",
    "Alternate 2": "alt2",
    "Alternate 3": "alt3"
}
class quizUI:
    def __init__(self, quiz):
        self.quiz = quiz

    def openQuiz(self, quiz):
        root = Tk()
        quiz = optionDict[quiz]
        root.title(quiz)
        numOfQuesions = reader.numberquesions(quiz)
        labelText = ''
        q = 1
        for x in range(0, numOfQuesions):
            labelText = labelText + ' ' + reader.read("ques", str(q), quiz)
            q = q + 1
        label = Label(root, text=labelText).pack()
        print(quiz)
        root.mainloop()