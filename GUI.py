# SDP Front End
# 9/25/2021
# William Farland

from tkinter import *
# from tkinter.ttk import *
import sys
from PIL import ImageTk, Image

def menuOptions_1_logic(input):
    if input == "Exit":
        return 0


# ---------- Part 1: Widget Creation ----------

# Main Window Creation
root = Tk()  # Create initial root widget
root.title('SDP - Team 22')  # Name root widget
root.attributes('-fullscreen', True)  # Display in full screen
# root.geometry("400x400")  # Can use this if we need to debug in smaller window
# root.iconbitmap()  # Add icon file later

# Canvas for Image creation
canvas = Canvas(root, width=2000, height=1200)  # Create canvas inside root widget

# Drop Down Menu Creation
menuOptions_1 = ["Exit", "Save"]
clicked = StringVar()
clicked.set("File")
dropMenu_1 = OptionMenu(root, clicked, *menuOptions_1)

# Image selection
img = Image.open("SheetMusic.png")  # PIL solution
img = img.resize((3000, 1000))
img = ImageTk.PhotoImage(img)
# ---------- Part 2: Place widgets ----------
dropMenu_1.grid(column=0, row=0)
canvas.grid(column=0, row=1)  # Place Canvas using geometry manager
canvas.create_image(0, 0, anchor=NW, image=img)

# ---------- Part 3: Infinite Loop for responsive GUI ----------
while 1:
    root.update()
    output = menuOptions_1_logic(clicked.get())
    if output == 0:
        sys.exit()
