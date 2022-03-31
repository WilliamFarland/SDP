from guiDependencies_GUI import *
from sheetMusic_GUI import *

import csv


def checkError(correctNote):
    value = False
    f = open('Output.csv', 'r')
    rowList = []
    reader = csv.reader(f, delimiter=",")
    for rows in reader:
        if abs(float(rows[1]) - time.time()) < 5:
            rowList.append(rows)
    f.close()

    for notes in rowList:
        if notes[3] == correctNote:
            value = True
        else:
            value = False

    return value


def findBatch(batchNum, noteList):
    noteinBatch = []
    for notes in noteList:
        if notes.batch == batchNum:
            noteinBatch.append(notes)
    return noteinBatch


def changeColor(noteNum, color, window):
    for notes in window.sheetMusic.noteList:
        noteName = note[noteNum.noteNum][2]
        if notes.pos == 5 and notes.name == noteName:
            notes.color = color


class defaultWindow:
    # GUI Setup Commands
    def __init__(self, name):
        self.name = name
        self.play = False
        self.dialog = None
        self.keyboard = None
        self.logo = None
        self.restartProgramFlag = 0
        self.mainCanvas = Canvas(root, width=width, height=height, highlightthickness=1,
                                 highlightbackground="black")

        self.dropMenu_1 = DropMenu("Menu 1", "Option Menu",
                                   ["File", "Exit", "Save", "Choose Song File"])
        self.dropMenu_2 = DropMenu("Menu 2", "Play/Pause",
                                   ["Play", "Pause"])
        self.dropMenu_3 = DropMenu("Menu 3", "Show/Hide", ["Show", "Hide"])

        self.current_tempo=tkinter.DoubleVar
        self.slider = tkinter.Scale(root, from_=1, to=10, orient='horizontal', variable=self.current_tempo)

        self.restartButton = Button(root, text='\u21BA', command = lambda: restartProgram(self))
        restartButtonLabel = Label(root, text="Restart", font=myFont_large)
        restartButtonLabel.grid(row=1, column=5)

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
        instr = tkinter.Label(self.dialog, text=instruction, font=myFont)
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

        self.sheetMusic.innerCanvas.create_rectangle(54, 20, 87, 450, fill='white', outline='', tag='showhidekeyboard')
        self.sheetMusic.innerCanvas.create_text(55, 20, anchor=NW, text="A", tag='showhidekeyboard', font=myFont_large)
        self.sheetMusic.innerCanvas.create_text(70, 30, anchor=NW, text="G", tag='showhidekeyboard', fill='black',
                                                font=myFont_large)
        self.sheetMusic.innerCanvas.create_text(55, 40, anchor=NW, text="F", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 55, anchor=NW, text="E", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 70, anchor=NW, text="D", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 83, anchor=NW, text="C", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 98, anchor=NW, text="B", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 110, anchor=NW, text="A", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 125, anchor=NW, text="G", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 139, anchor=NW, text="F", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 155, anchor=NW, text="E", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 164, anchor=NW, text="D", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 174, anchor=NW, text="C", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')

        self.sheetMusic.innerCanvas.create_text(55, 290, anchor=NW, text="C", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 300, anchor=NW, text="B", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 308, anchor=NW, text="A", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 320, anchor=NW, text="G", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 335, anchor=NW, text="F", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 348, anchor=NW, text="E", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 365, anchor=NW, text="D", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 377, anchor=NW, text="C", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 392, anchor=NW, text="B", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 405, anchor=NW, text="A", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 422, anchor=NW, text="G", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(70, 430, anchor=NW, text="F", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')
        self.sheetMusic.innerCanvas.create_text(55, 440, anchor=NW, text="E", tag='showhidekeyboard',
                                                font=myFont_large, fill='black')

    def updateWindow(self):
        root.update()
        self.dropMenu_1.checkValue()
        self.dropMenu_2.checkValue()
        self.dropMenu_3.checkValue()

        if self.dropMenu_1.checkValue() == "Save":
            return 'Save'

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
        self.dialog.grid(row=1, column=5, columnspan=25, rowspan=5, padx=10, pady=10)
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

        self.restartButton.grid(row=2, column=5)
