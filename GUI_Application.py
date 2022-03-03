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


class Slider:
    def __init__(self, root, myFont_large, name, label, min, max):
        self.root = root
        self.myFont_large = myFont_large
        self.name = name
        self.sliderLabel = tkinter.Label(self.root, text=label, font=myFont_large)
        self.sliderObject = Scale(self.root, from_=min, to=max, orient=HORIZONTAL, tickinterval=0.25)


class DropMenu:
    def __init__(self, root, myFont_large, name, label, menuOptions):
        self.root = root
        self.myFont_large = myFont_large
        self.name = name
        self.path = False
        self.show = True
        self.prevShow = True
        self.menuOptions = menuOptions
        self.clicked = StringVar()
        if self.name == "Menu 1":
            self.clicked.set("File")
        else:
            self.clicked.set("Play/Pause")
        # self.clicked.set("File")
        self.dropMenuObject = OptionMenu(self.root, self.clicked, *self.menuOptions)
        self.dropMenuLabel = tkinter.Label(self.root, text=label, font=self.myFont_large)

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

        self.root = Tk()  # Create initial root widget
        self.root.title('SDP - Team 22')  # Name root widget
        self.root.attributes('-fullscreen', True)  # Display in full screen
        # self.root.configure(background = 'white')
        self.mainCanvas = Canvas(self.root, width=width, height=height, highlightthickness=1,
                                 highlightbackground="black")

        # Create a common font accross the different GUI elements
        self.myFont = font.Font(family='San Francisco', size=10, weight='bold')
        self.myFont_large = font.Font(family='San Francisco', size=15, weight='bold')

        self.dropmenu_lbl = tkinter.Label(self.root, text="Menu Options", font=self.myFont_large)
        self.pause_btn_lbl = tkinter.Label(self.root, text="Pause Song", font=self.myFont_large)
        self.play_btn_lbl = tkinter.Label(self.root, text="Play Song", font=self.myFont_large)
        self.slider_lbl = tkinter.Label(self.root, text="Tempo Control", font=self.myFont_large)

        self.slider = Slider(self.root, self.myFont_large, "tempo adjustment", "Tempo Adjustment", 1, 10)
        self.dropMenu_1 = DropMenu(self.root, self.myFont_large, "Menu 1", "Option Menu",
                                   ["File", "Exit", "Save", "Choose Song File"])

        self.dropMenu_2 = DropMenu(self.root, self.myFont_large, "Menu 2", "Play/Pause",
                                   ["Play", "Pause"])
        self.dropMenu_3 = DropMenu(self.root, self.myFont_large, "Menu 3", "Show/Hide", ["Show", "Hide"])

        # self.pauseButton = Btn(self.root, "Pause", "Pause Button", '\u23F8', self.myFont, self.myFont_large)
        # self.playButton = Btn(self.root, "Play", "Play Button", '\u23F5', self.myFont, self.myFont_large)

        self.configureKeyboard()
        self.configureDialog()
        self.configureLogo()
        self.sheetMusic = SheetMusicGraphics("Sheet Music 1", self.mainCanvas, self.root)
        self.placeObjects()

    def configureKeyboard(self):
        # Canvas for Image creation
        w = Canvas(self.mainCanvas, width=width * 0.75, height=height * 0.25)  # Create canvas inside root widget
        w.configure(bg='#FFFFFF')
        # Background Image
        img = Image.open(imagePath+"keyBoardModel.png")  # PIL solution
        img = img.resize((int(width * 0.75), int(height * 0.25)))
        img = ImageTk.PhotoImage(img)
        self.root.img = img
        w.create_image(0, 0, anchor=NW, image=img)
        w.update()
        self.keyboard = w

    def configureLogo(self):
        # Canvas for Image creation
        w = Canvas(self.root, width=width * 0.05, height=height * 0.05)  # Create canvas inside root widget
        w.configure(bg='#FFFFFF')
        # Background Image
        img2 = Image.open(imagePath+"16th.png")  # PIL solution
        img2 = img2.resize((int(width * 0.05), int(height * 0.05)))
        img2 = ImageTk.PhotoImage(img2)
        self.root.img2 = img2
        w.create_image(0, 0, anchor=NW, image=img2)
        w.update()
        self.logo = w

    def configureDialog(self):
        # Create another canvas for dialog between user and program
        dialog = Frame(self.root, width=width * 0.5, height=height * 0.24)
        # dialog.configure(bg="white", bd=5)
        self.dialog = dialog

    def outputDialog(self, instruction):
        self.clearDialog()
        instrHeader = tkinter.Label(self.dialog, text="DEBUG: ", font=self.myFont_large)
        instrHeader.pack(side=LEFT)
        # Create an initial start instruction before a song is selected
        instr = tkinter.Label(self.dialog, text=instruction, font=self.myFont_large)
        instr.pack(side=LEFT)

    def clearDialog(self):
        for widgets in self.dialog.winfo_children():
            widgets.destroy()

    def hideValues(self):
        numKeys = 36
        shift = (width*0.75) / numKeys + 0.5
        shift = shift + 0.005
        for noteNum in range(1, len(note)+1):
            if note[noteNum][0] == 'r':
                coords = note[noteNum][1] * shift -37.6, 260, note[noteNum][1] * shift + 30 - 33, 205
                self.keyboard.create_rectangle(coords, outline='white', fill='white', tag='showhide')

    def showValues(self):
        self.keyboard.delete("showhide")

    def updateWindow(self):
        self.root.update()
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
        self.keyboard.place(x=52, y=10)
        self.logo.place(x=1400, y=10)
        allura = font.Font(family='Roman', size=10, weight='bold')
        label = tkinter.Label(self.root, text="Team 22", font=allura)
        label1 = tkinter.Label(self.root, text="SDP", font=allura)
        label1.place(x=1360, y=15)
        label.place(x=1350, y=30)
        self.mainCanvas.create_rectangle(0, 0, 1920, 5, fill="grey")
        self.sheetMusic.innerCanvas.place(x=0, y=300)

        # Place dropmenu
        self.dropMenu_1.dropMenuLabel.grid(row=1, column=0, padx=5)
        self.dropMenu_1.dropMenuObject.grid(row=2, column=0, padx=0, pady=5, rowspan=3)
        self.dropMenu_1.dropMenuObject.config(width=7)

        self.dropMenu_2.dropMenuLabel.grid(row=1, column=1, padx=5)
        self.dropMenu_2.dropMenuObject.grid(row=2, column=1, padx=0, rowspan=3)

        self.dropMenu_3.dropMenuLabel.grid(row=1, column=3, padx=5)
        self.dropMenu_3.dropMenuObject.grid(row=2, column=3, padx=0, rowspan=3)
        # Place slider
        self.slider.sliderLabel.grid(row=1, column=4, padx=10)
        self.slider.sliderObject.grid(row=2, column=4, padx=10)


class Btn(mainWindow):
    def __init__(self, root, name, label, btnLabel, myFont, myFont_large):
        self.root = root
        self.name = name
        self.label = tkinter.Label(self.root, text=label, font=myFont_large)
        self.buttonObject = Button(self.root, text=btnLabel, bd='5', command=self.action, font=myFont)

    def action(self):
        if self.name == "Play":
            mainWindow.play = True
            print("Playing...")
        else:
            mainWindow.play = False
            print("Pausing...")

