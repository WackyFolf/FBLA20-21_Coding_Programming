# Copyright (c) 2020 Evan Sonin
import tkinter
from tkinter import Button, Message, Label, Entry

window = tkinter.Tk() # Create new Tkinter window
window.title("Testing Program") # Set the title of the window
def setLabel(): # Create new command for the button to execute
    newText = entry.get() # Get text from text box
    label["text"] = newText
hiButton = Button(window, text="Hi", command = setLabel) # Create button with the text "text" in the window "window" that executes printInConsole.
label = Label(window, text="The server is running but no one is allowed on, \n so if you see that it has an unusually low amount of people, \nit's whitelisted still.") # Chunk of text.
entry = Entry()
label.pack() # Add text to window
hiButton.pack() # Add button to window
entry.pack()
window.mainloop() # Open window