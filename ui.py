# Copyright (c) 2020 Evan 
import tkinter
from tkinter import *
from reader import reader

reader = reader("alt1")
root = tkinter.Tk() # Create new Tkinter window
root.title("Testing Program") # Set the title of the window
def setLabel(): # Create new command for the button to execute
    want = entry.get() # Get want from text box
    newText = reader.read(want) # Obtain from JSON file via reader
    label["text"] = newText
frame = Frame(relief = SUNKEN, master=root)
frame2 = Frame(master=root, height=50)
hiButton = Button(root, text="Hi", command = setLabel) # Create button with the text "text" in the window "window" that executes printInConsole.
label = Label(text="The server is running but no one is allowed on, \n so if you see that it has an unusually low amount of people, \nit's whitelisted still.", master=frame, relief=RIDGE) # Chunk of text.
entry = Entry(master = frame2)
frame.pack(side=tkinter.TOP)
frame2.pack(side=tkinter.LEFT)
label.pack() # Add text to window
hiButton.pack(side=tkinter.LEFT) # Add button to window
entry.pack()
root.mainloop() # Open window
