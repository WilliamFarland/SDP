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
        #self.root.configure(background='white')
        # self.root.configure(background = 'white')
        self.mainCanvas = Canvas(self.root, width=width, height=height, highlightthickness=1,
                                 highlightbackground="black")

        # Create a common font accross the different GUI elements
        self.myFont = font.Font(family='San Francisco', size=10, weight='bold')
        self.myFont_large = font.Font(family='San Francisco', size=15, weight='bold')

        #self.dropmenu_lbl = tkinter.Label(self.root, text="Menu Options", font=self.myFont_large, bg='white')
        #self.pause_btn_lbl = tkinter.Label(self.root, text="Pause Song", font=self.myFont_large)
        #self.play_btn_lbl = tkinter.Label(self.root, text="Play Song", font=self.myFont_large)
        #self.slider_lbl = tkinter.Label(self.root, text="Tempo Control", font=self.myFont_large, bg='white')

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
        self.showValues()

    def configureKeyboard(self):
        # Canvas for Image creation
        w = Canvas(self.mainCanvas, width=width * 0.8, height=height * 0.3)  # Create canvas inside root widget
        w.configure(bg='#FFFFFF')
        # Background Image
        img = Image.open(imagePath+"keyBoardModel.png")  # PIL solution
        img = img.resize((int(width * 0.8), int(height * 0.27)))
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
        img2 = Image.open(imagePath+"SDP_Logo_Grey_Small.png")  # PIL solution
        img2 = img2.resize((int(width * 0.05), int(height * 0.07)))
        img2 = ImageTk.PhotoImage(img2)
        self.root.img2 = img2
        w.create_image(0, 0, anchor=NW, image=img2)
        w.update()
        self.logo = w

    def configureDialog(self):
        # Create another canvas for dialog between user and program
        dialog = Frame(self.root, width=width * 0.5, height=height * 0.24)
       # dialog.configure(bg="white")
       # dialog.configure(highlightbackground="r", highlightcolor="red")
        self.dialog = dialog

    def outputDialog(self, instruction):
        self.clearDialog()
        instrHeader = tkinter.Label(self.dialog, text="Console: ", font=self.myFont_large)
        instrHeader.grid(row=0, column=0)
        # Create an initial start instruction before a song is selected
        instr = tkinter.Label(self.dialog, text=instruction, font=self.myFont_large)
        instr.grid(row=1, column=0)

    def clearDialog(self):
        for widgets in self.dialog.winfo_children():
            widgets.destroy()

    def hideValues(self):
        self.sheetMusic.innerCanvas.delete('showhidekeyboard')
        numKeys = 36
        shift = (width*0.8) / numKeys + 0.5
        shift = shift+.05
        coords = 0,200,41,280
        self.keyboard.create_rectangle(coords, outline='white', fill='white', tag='showhide')
        for noteNum in range(1, len(note)+1):
            if note[noteNum][0] == 'r':
                coords = note[noteNum][1] * shift+3-.05, 280, note[noteNum][1] * shift+41, 215
                self.keyboard.create_rectangle(coords, outline='white', fill='white', tag='showhide')

    def showValues(self):
        self.keyboard.delete("showhide")



        self.sheetMusic.innerCanvas.create_rectangle(54, 20, 87, 450, fill='white', outline='', tag='showhidekeyboard')
        self.sheetMusic.innerCanvas.create_text(55, 20, anchor = NW, text="A", tag='showhidekeyboard', font=self.myFont_large)
        self.sheetMusic.innerCanvas.create_text(70, 30, anchor=NW, text="G", tag='showhidekeyboard', fill='black',
                                                font=self.myFont_large)
        self.sheetMusic.innerCanvas.create_text(55, 40, anchor=NW, text="F", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 55, anchor=NW, text="E", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 70, anchor=NW, text="D", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 83, anchor=NW, text="C", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 98, anchor=NW, text="B", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 110, anchor=NW, text="A", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 125, anchor=NW, text="G", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 139, anchor=NW, text="F", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 155, anchor=NW, text="E", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 164, anchor=NW, text="D", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 174, anchor=NW, text="C", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')

        self.sheetMusic.innerCanvas.create_text(55, 290, anchor=NW, text="C", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 300, anchor=NW, text="B", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 308, anchor=NW, text="A", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 320, anchor=NW, text="G", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 335, anchor=NW, text="F", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 348, anchor=NW, text="E", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 365, anchor=NW, text="D", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 377, anchor=NW, text="C", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 392, anchor=NW, text="B", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 405, anchor=NW, text="A", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 422, anchor=NW, text="G", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 430, anchor=NW, text="F", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 440, anchor=NW, text="E", tag='showhidekeyboard',
                                                font=self.myFont_large, fill='black')

        #for i in range(5):
           # self.sheetMusic.innerCanvas.create_rectangle(40, 51 + i * 29, 100, 53 + i * 29, fill='black', outline='black',
                                              #           tag='showhidekeyboard')

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
        self.keyboard.place(x=1, y=7)
        self.logo.place(x=1440, y=5)
        allura = font.Font(family='Roman', size=10, weight='bold')
        #label = tkinter.Label(self.root, text="Team 22", font=allura)
        #label1 = tkinter.Label(self.root, text="SDP", font=allura)
       # label1.place(x=1360, y=15)
        #label.place(x=1350, y=30)
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
        # Place slider
        self.slider.sliderLabel.grid(row=1, column=4, padx=10)
        self.slider.sliderObject.grid(row=2, column=4, padx=10)


class Btn(mainWindow):
    def __init__(self, root, name, label, btnLabel, myFont, myFont_large):
        self.root = root
        self.name = name
        self.label = tkinter.Label(self.root, text=label, font=myFont_large, bd='white')
        self.buttonObject = Button(self.root, text=btnLabel, bd='5', command=self.action, font=myFont)

    def action(self):
        if self.name == "Play":
            mainWindow.play = True
            print("Playing...")
        else:
            mainWindow.play = False
            print("Pausing...")

