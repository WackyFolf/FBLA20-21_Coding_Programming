import tkinter
from tkinter import *
from reader import reader

class quizUI:
    def __init__(self, quiz):
        self.quiz = quiz

    def openQuiz(self, quiz):
        root = Tk()
        root.title('Quiz')
        root.mainloop()