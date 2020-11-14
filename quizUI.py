import tkinter
import random
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
        actualQuiz = optionDict[quiz]
        root.title(quiz + " Quiz")
        numOfQuesions = reader.numberquesions(actualQuiz)
        labelText = ''
        q = []
        y = 0
        questionDict = reader.getFile(actualQuiz)
        for x in range(1, numOfQuesions + 1):
            q.append(x)
        random.shuffle(q)
        for x in range(0, numOfQuesions):
           labelText = labelText + questionDict[(str(q[x]))]['ques'] + " \\ " + questionDict[(str(q[x]))]['ans'] + "\n"
           y = y + 1
        label = Label(root, text=labelText, justify="left", wraplength=(800)).pack()
        root.mainloop()