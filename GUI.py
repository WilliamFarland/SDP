# SDP Front End
# 9/25/2021
# William Farland

from tkinter import *
# from tkinter.ttk import *
import sys
from PIL import ImageTk, Image


def menuOptions_1_logic(flag):
    if flag == "Exit":
        return 0


def placeNote(noteType, x, y):
    noteType = "Note"
    note = Image.open(noteType + '.png')  # PIL solution
    note_width, note_height = note.size
    note = note.resize((int(note_width * 0.5), int(note_height * 0.5)))
    note = ImageTk.PhotoImage(note)
    canvas.create_image(x, y, anchor=NW, image=note)
   # canvas.create_image(0, 0, anchor=NW, image=note)


# ---------- Important Variables ----------
# Monitor screen dimensions
height = 1080
width = 1920

# ---------- Part 1: Widget Creation ----------

# Main Window Creation
global root
root = Tk()  # Create initial root widget
root.title('SDP - Team 22')  # Name root widget
root.attributes('-fullscreen', True)  # Display in full screen
root.configure(bg='#FFFFFF')
# root.geometry("400x400")  # Can use this if we need to debug in smaller window
# root.iconbitmap()  # Add icon file later

# Canvas for Image creation

canvas = Canvas(root, width=width, height=height)  # Create canvas inside root widget
canvas.configure(bg='#FFFFFF')

# Drop Down Menu Creation
menuOptions_1 = ["Exit", "Save"]
clicked = StringVar()
clicked.set("File")
dropMenu_1 = OptionMenu(root, clicked, *menuOptions_1)

# Image selection
img = Image.open("SheetMusic.png")  # PIL solution
img = img.resize((int(width * 0.8), int(height * 0.8)))
img = ImageTk.PhotoImage(img)

# Note Testing
noteType = "Note"
x, y = 0, 50
note = Image.open(noteType + '.png')  # PIL solution
note_width, note_height = note.size
note = note.resize((int(note_width * 0.5), int(note_height * 0.5)))
note = ImageTk.PhotoImage(note)


# ---------- Part 2: Place widgets ----------
dropMenu_1.grid(column=0, row=0)
canvas.grid(column=0, row=1)  # Place Canvas using geometry manager
canvas.create_image(0, 0, anchor=NW, image=img)
#canvas.create_image(0, 0, anchor=NW, image=note)
canvas.create_image(0, 100, anchor=NW, image=note)
placeNote('test', 0, 100)
placeNote('test', 0, 0)
# ---------- Part 3: Infinite Loop for responsive GUI ----------
while 1:
    root.update()
    output = menuOptions_1_logic(clicked.get())
    if output == 0:
        sys.exit()
