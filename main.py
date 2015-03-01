"""
Quizify
SPUD Hackathon
Aaron Grider, Joe Jazdzewski, Isaac Wang
"""

#!/usr/bin/env python3


import Parser
import Quizlet
import Word
import sys

from tkinter import *
from tkinter.filedialog import askopenfilename

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200

parser = Parser.Parser()
quizlet = Quizlet.Quizlet('695d75d41c43e243bbee2b8896a7b99bc9fefe4c')

def read_textfile(file_name):

    file = open(file_name,'r')

    for word in file.read().split():
        print("Reading word: " + word)
        parser.add_word(word, get_definition(word))

def get_definition(word):
    print("Getting definition")
    definition = quizlet.query_definition(word)
    return definition

if __name__ == "__main__":

    # Draw initial UI
    root = Tk()
    root.wm_title("Test")
    root.geometry("800x600")

    # Add quit button
    quit = Button(root, text="Quit", command=root.quit)
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

    # Call required methods
    read_textfile(root.filename)

    print("Flash cards sucessfully created")
    for item in Parser.Parser.get_list(parser):
        print(item.name + " Count(", item.frequency, "): ", item.definition)
        quizlet.add_flashcard(item)

    root.mainloop()
