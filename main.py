"""
Quizify
SPUD Hackathon
Aaron Grider, Joe Jazdzewski, Isaac Wang
"""

#!/usr/bin/env python3

import sys
from tkinter import *
from tkinter.filedialog import askopenfilename

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200

def read_textfile(file_name):

    file = open(file_name,'r')

    for word in file.read().split():
        print(word + ":")

def present_definitions():
    print("Present definition")

if __name__ == "__main__":

    # Draw initial UI
    root = Tk()
    root.wm_title("Test")
    root.geometry("800x600")

    # Add quit button
    quit = Button(root, text="Quit", command=root.quit, d)
    quit.pack()

    root.withdraw() # Hide main window

    # Prompt for file
    root.filename = askopenfilename(title="Choose a text file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

    # Check to see if file selected
    if root.filename:
        open_message = root.filename + " opened!"
        w = Label(root, text=open_message)
        w.pack()
    else:
        sys.exit()

    root.deiconify() # Show main window

    root.mainloop()