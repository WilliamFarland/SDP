# SDP Front End
# 9/25/2021
# William Farland
from buttonLogic import *
from tkinter import *
#from tkinter.ttk import *
import sys

# Part 1: Main Window Creation
root = Tk()
root.title('SDP - Team 22')
# root.iconbitmap()
# root.attributes('-fullscreen', True)
root.geometry("400x400")

# Add some pizaz to the styling...
#style = Style()
#style.configure('TButton', font =
#               ('calibri', 10, 'bold', 'underline'),
#                foreground = 'red')


menuOptions_1 = [
    "Exit", "Save"
]
clicked = StringVar()
clicked.set("File")
dropMenu_1 = OptionMenu(root, clicked, *menuOptions_1)
dropMenu_1.grid(column=0, row=0)
# button = Button(root, text="OK", command=menuOptions_1_logic)
# button.pack()


while 1:
    root.update()
    output = menuOptions_1_logic(clicked.get())
    if output == 0:
        sys.exit()
