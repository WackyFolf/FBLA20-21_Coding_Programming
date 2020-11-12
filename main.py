import tkinter
from tkinter import *
import sys
from reader import reader
from functools import partial
from quizUI import quizUI

reader = reader("ques", "1", "test") # Set variables for reader
quizUI = quizUI('quiz') # Create quizUI object
root = Tk() # Create main window
root.title('Quiz Program') # Name main window


licenseOpen = False # Used to make sure the license window cannot be opened more than once- currently closed

quizOptions = [
    "Test Quiz",
    "Computer Applications"
]
variable=StringVar(root) # I don't really know what this does, but it works
variable.set(quizOptions[0]) # Sets default value for dropdown

frame = LabelFrame(root, padx=5, pady=5, text="Start a Quiz")
frame.pack(padx=10, pady=10, side = LEFT)
frame2 = LabelFrame(root, padx=5, pady=5, text="Other")
frame2.pack(padx=10, pady=10, side = RIGHT)

def exitProgram():
    sys.exit()  # Exit button completely ends script including all child windows
def uselessDef():
    pass # Do nothing and be useless as the name suggests
def declareLicenseClosed():
    global licenseOpen
    licenseOpen = False # This funcion is here because buttons are stupid, define the license window as closed when it is closed
def license():
    global licenseOpen
    with open ("LICENSE", "r") as licenseFile:
        licenseText = licenseFile.read() # Open LICENSE file and set variable to its contents
    if licenseOpen == True:
        pass # If the license window is already open, don't do anything if the button is pressed
    else:
        licenseOpen = True # Set the license window to open so it can't be opened until closed again
        licenseWindow = Tk() # Create license window
        licenseWindow.resizable(width=False, height=False) # Disable resizing of the license window
        licenseWindow.iconbitmap('icons/license.ico') # Add nifty icon to the license window
        licenseWindow.protocol("WM_DELETE_WINDOW", uselessDef) # Assign the close button of the window to do absolutely nothing when pressed
        licenseWindow.title('MIT License © 2020 Evan Sonin')
        labelLicense = Label(licenseWindow, text=licenseText, padx=10, pady=10, relief="ridge", justify='center').pack()
        exitButton = Button(licenseWindow, text="Close", command=lambda:[declareLicenseClosed(),licenseWindow.destroy()]).pack(anchor=CENTER, pady=10) # The button calls the function to define the window as closed, then closes it
        licenseWindow.mainloop()
options = OptionMenu(frame, variable, *quizOptions)  
options.grid(row=1,column=0)      
def openQuiz(quiz):
    quizUI.openQuiz(quiz)
    print(variable.get())


b = Button(frame, text="Begin Quiz", command=partial(openQuiz,variable.get()))
b.grid(row=2, column=0)
b3 = Button(frame2, text="Exit", command=exitProgram)
b3.grid(row=0, column=1, padx=10, pady=10)
b3 = Button(frame2, text="License", command=license)
b3.grid(row=0, column=0, padx=10, pady=10)
label = Label(frame, text="Select a quiz, then open it.")
label.grid(row=0,column=0)
root.mainloop()