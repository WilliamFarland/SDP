# GUI for the 2nd mode of project
# 3/29/22

from GUI_Functions import *
from GUI_SheetMusic import SheetMusicGraphics
import tkinter
from tkinter import *
from tkinter import font, filedialog
from PIL import ImageTk, Image
import sys

control = False
imagePath = 'images/'

width = 1920
height = 1080

root = Tk()  # Create initial root widget
root.title('SDP - Team 22')  # Name root widget
root.geometry("1536x864")

myFont = font.Font(family='San Francisco', size=10, weight='bold')
myFont_large = font.Font(family='San Francisco', size=15, weight='bold')


class DropMenu:
    def __init__(self, name, label, menuOptions):
        self.name = name
        self.path = False
        self.show = True
        self.prevShow = True
        self.menuOptions = menuOptions
        self.clicked = StringVar()
        if self.name == "Menu 1":
            self.clicked.set("File")
        if self.name == "Menu 2":
            self.clicked.set("Play/Pause")
        if self.name == "Menu 3":
            self.clicked.set("Show/Hide")
        if self.name == "Menu 10":
            self.clicked.set("Mode Selection")
        # self.clicked.set("File")
        self.dropMenuObject = OptionMenu(root, self.clicked, *self.menuOptions)
        self.dropMenuLabel = tkinter.Label(text=label, font=myFont_large)

    def checkValue(self):
        flag = self.clicked.get()
        if flag == "Exit":
            sys.exit()
        if flag == "Choose Song File":
            file_path = filedialog.askopenfilename()
            self.clicked.set("File")
            self.path = file_path
        if flag == "Pause":
            # self.clicked.set("Play/Pause")
            self.path = False
            # print("Pause")
        if flag == "Play":
            self.path = True
            # self.clicked.set("Play/Pause")
            # print("Play")
        if flag == "Show":
            self.show = True
        if flag == "Hide":
            self.show = False


class mainWindow:
    # GUI Setup Commands
    def __init__(self, name):
        self.name = name
        self.play = False
        self.dialog = None
        self.keyboard = None
        self.logo = None
        self.mainCanvas = Canvas(root, width=width, height=height, highlightthickness=1,
                                 highlightbackground="black")

        self.dropMenu_1 = DropMenu("Menu 1", "Option Menu",
                                   ["File", "Exit", "Save", "Choose Song File"])
        self.dropMenu_2 = DropMenu("Menu 2", "Play/Pause",
                                   ["Play", "Pause"])
        self.dropMenu_3 = DropMenu("Menu 3", "Show/Hide", ["Show", "Hide"])

        self.current_tempo=tkinter.DoubleVar
        self.slider = tkinter.Scale(root, from_=1, to=10, orient='horizontal', variable=self.current_tempo)

        self.configureKeyboard()
        self.configureDialog()
        self.configureLogo()
        self.sheetMusic = SheetMusicGraphics("Sheet Music 1", self.mainCanvas, root)
        self.placeObjects()
        self.showValues()

    def configureKeyboard(self):
        # Canvas for Image creation
        w = Canvas(self.mainCanvas, width=width * 0.8, height=height * 0.3)  # Create canvas inside root widget
        w.configure(bg='#FFFFFF')
        # Background Image
        img = Image.open(imagePath + "keyBoardModel.png")  # PIL solution
        img = img.resize((int(width * 0.8), int(height * 0.27)))
        img = ImageTk.PhotoImage(img)
        root.img = img
        w.create_image(0, 0, anchor=NW, image=img)
        w.update()
        self.keyboard = w

    def configureLogo(self):
        # Canvas for Image creation
        w = Canvas(root, width=width * 0.05, height=height * 0.05)  # Create canvas inside root widget
        w.configure(bg='#FFFFFF')
        # Background Image
        img2 = Image.open(imagePath + "SDP_Logo_Grey_Small.png")  # PIL solution
        img2 = img2.resize((int(width * 0.05), int(height * 0.07)))
        img2 = ImageTk.PhotoImage(img2)
        root.img2 = img2
        w.create_image(0, 0, anchor=NW, image=img2)
        w.update()
        self.logo = w

    def configureDialog(self):
        # Create another canvas for dialog between user and program
        dialog = Frame(root, width=width * 0.5, height=height * 0.24)
        # dialog.configure(bg="white")
        # dialog.configure(highlightbackground="r", highlightcolor="red")
        self.dialog = dialog

    def outputDialog(self, instruction):
        self.clearDialog()
        instrHeader = tkinter.Label(self.dialog, text="Console: ", font=myFont_large)
        instrHeader.grid(row=0, column=0)
        # Create an initial start instruction before a song is selected
        instr = tkinter.Label(self.dialog, text=instruction, font=myFont_large)
        instr.grid(row=1, column=0)

    def clearDialog(self):
        for widgets in self.dialog.winfo_children():
            widgets.destroy()

    def hideValues(self):
        self.sheetMusic.innerCanvas.delete('showhidekeyboard')
        numKeys = 36
        shift = (width * 0.8) / numKeys + 0.5
        shift = shift + .05
        coords = 0, 200, 41, 280
        self.keyboard.create_rectangle(coords, outline='white', fill='white', tag='showhide')
        for noteNum in range(1, len(note) + 1):
            if note[noteNum][0] == 'r':
                coords = note[noteNum][1] * shift + 3 - .05, 280, note[noteNum][1] * shift + 41, 215
                self.keyboard.create_rectangle(coords, outline='white', fill='white', tag='showhide')

    def showValues(self):
        self.keyboard.delete("showhide")



    def updateWindow(self):
        root.update()
        self.dropMenu_1.checkValue()
        self.dropMenu_2.checkValue()
        self.dropMenu_3.checkValue()

        # insert stupid code here to toggle the on / off instead of wasting on off time every iteration
        # if this isnt here the code does lag
        if self.dropMenu_3.prevShow is True and self.dropMenu_3.show is False:
            self.hideValues()
            self.dropMenu_3.prevShow = False
        elif self.dropMenu_3.prevShow is False and self.dropMenu_3.show is True:
            self.showValues()
            self.dropMenu_3.prevShow = True

    def placeObjects(self):
        self.mainCanvas.grid(row=10, column=0, columnspan=40, rowspan=50)
        self.mainCanvas.configure(background="white")
        self.dialog.grid(row=1, column=3, columnspan=30, rowspan=5, padx=10, pady=10)
        self.keyboard.place(x=1, y=7)
        self.logo.place(x=1440, y=5)
        # rectangle borders
        self.sheetMusic.innerCanvas.create_rectangle(0, 0, 1920, 5, fill="grey")
        self.sheetMusic.innerCanvas.place(x=0, y=300)
        self.mainCanvas.create_rectangle(0, 0, 1920, 5, fill="grey")
        # Place dropmenu
        self.dropMenu_1.dropMenuLabel.grid(row=1, column=0, padx=5)
        self.dropMenu_1.dropMenuObject.grid(row=2, column=0, padx=0, pady=5, rowspan=3)
        self.dropMenu_1.dropMenuObject.config(width=7)

        self.dropMenu_2.dropMenuLabel.grid(row=1, column=1, padx=5)
        self.dropMenu_2.dropMenuObject.grid(row=2, column=1, padx=0, rowspan=3)

        self.dropMenu_3.dropMenuLabel.grid(row=1, column=3, padx=5)
        self.dropMenu_3.dropMenuObject.grid(row=2, column=3, padx=0, rowspan=3)

        sliderLabel = Label(root, text="Tempo Adjustment", font=myFont_large)
        sliderLabel.grid(row=1, column=4)
        self.slider.grid(row=2, column=4)

