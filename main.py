# Copyright (c) 2020 Evan Sonin
import tkinter
from tkinter import Button, Message

window = tkinter.Tk() # Create new Tkinter window
window.title("Testing Program") # Set the title of the window
def printInConsole(): # Create new command for the button to execute
    print ("Hello there")
hiButton = tkinter.Button (window, text="Hi", command = printInConsole) # Create button with the text "text" in the window "window" that executes printInConsole.
label = Message(window, text="The server is running but no one is allowed on, so if you see that it has an unusually low amount of people, it's whitelisted still. ") # Chunk of text.
hiButton.pack() # Add button to window
label.pack() # Add text to window
window.mainloop() # Open window