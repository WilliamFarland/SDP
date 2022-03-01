# SDP Front End
# 9/25/2021
# William Farland
from GUI_Functions import *
from MUSIC_Logic import *
import time
import tkinter
from tkinter import *
from PIL import ImageTk, Image

control = False
imagePath = 'images/'
noteHeight = dict()
noteHeight['c4'] = 175
noteHeight['d4'] = 165
noteHeight['e4'] = 157
noteHeight['f4'] = 143
noteHeight['g4'] = 130
noteHeight['a5'] = 115
noteHeight['b5'] = 100
noteHeight['c5'] = 85
noteHeight['d5'] = 70
noteHeight['e5'] = 55
noteHeight['f5'] = 40
noteHeight['g5'] = 30
noteHeight['a6'] = 15


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

class Note:
    def __init__(self, name, noteType):
        self.name = name
        self.noteType = noteType


class sheetmusicGraphics:
    def __init__(self, name, mainCanvas, root):
        self.name = name
        self.innerCanvas = Canvas(mainCanvas, width=width * 0.8, height=height * 0.45, highlightthickness=1,
                                  highlightbackground="black")
        img = Image.open(imagePath+"SheetMusic_crop5.png")  # PIL solution
        img = img.resize((int(width * 0.8), int(height * 0.45)))
        img = ImageTk.PhotoImage(img)
        self.innerCanvas.img = img
        self.innerCanvas.create_image(0, 0, anchor=NW, image=img)
        self.rectLeftCord = []
        self.rectRightCord = []
        self.midCord = []
        self.root = root
        self.drawBorders()
        self.noteList = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def drawNotes(self):
        for i in range(10):
            note = self.noteList[i]
            if type(note) == int:
                continue
            y = noteHeight[note.name]
            noteType = note.noteType
            pos = i
            x = self.midCord[pos - 1]
            if note.name == "c4":
                self.innerCanvas.create_line(x-20, 185, x+40, 185, width=3)
            if note.name == "a6":
                self.innerCanvas.create_line(x - 20, 25, x + 40, 25, width=3)
            if noteType == "Quarter":
                self.drawQuarterNote(pos, y)
            if noteType == "Half":
                self.drawHalfNote(pos, y)
            if noteType == "Eighth":
                self.drawEighthNote(pos, y)
            if noteType == "Whole":
                self.drawWholeNote(pos, y)

    def shiftNoteData(self):
        for i in reversed(range(10)):
            self.noteList[i] = self.noteList[i-1]
        self.deleteNotes()

    def createNoteData(self, note, pos, noteType):
        newNote = Note(note, noteType)
        self.noteList.insert(pos, newNote)

    def drawBorders(self):
        left = 50
        right = 1500
        size = (right - left) / 9
        leftStart = left
        rightStart = leftStart + size
        for i in range(9):
            self.innerCanvas.create_rectangle(leftStart + i * size, 470, rightStart + i * size, 480, fill="grey")
            self.rectLeftCord.append(leftStart + i * size)
            self.rectRightCord.append(rightStart + i * size)
            self.midCord.append((self.rectLeftCord[i]+self.rectRightCord[i])/2)

        self.innerCanvas.create_rectangle(self.rectLeftCord[4], 0, self.rectRightCord[4], 480, fill='')

    def drawQuarterNote(self, pos, y):
        x = self.midCord[pos-1]
        oval = self.innerCanvas.create_oval(x, y, x + 22, y + 20, fill='black', tags='notes')
        line = self.innerCanvas.create_line(x + 20, y + 10, x + 20, y - 30, width=2.5, tags='notes')

    def drawHalfNote(self, pos, y):
        x = self.midCord[pos - 1]
        oval = self.innerCanvas.create_oval(x, y, x + 22, y + 20, fill='', width=2.5 ,tags='notes')
        line = self.innerCanvas.create_line(x + 20, y + 10, x + 20, y - 30, width=2.5, tags='notes')

    def drawEighthNote(self, pos, y):
        x = self.midCord[pos - 1]
        oval = self.innerCanvas.create_oval(x, y, x + 22, y + 20, fill='black', width=2.5, tags='notes')
        line = self.innerCanvas.create_line(x + 20, y + 10, x + 20, y - 30, width=2.5, tags='notes')
        line = self.innerCanvas.create_line(x + 20, y - 30, x + 34, y - 12, width=2.5,tags='notes')

    def drawWholeNote(self, pos, y):
        x = self.midCord[pos - 1]
        oval = self.innerCanvas.create_oval(x-5, y, x + 30, y + 25, fill='', width=4.5, tags='notes')

    def deleteNotes(self):
        self.innerCanvas.delete("notes")

    def create_rectangle_transparent(self, x1, y1, x2, y2, **kwargs):
        images = []
        if 'alpha' in kwargs:
            alpha = int(kwargs.pop('alpha') * 255)
            fill = kwargs.pop('fill')
            fill = self.root.winfo_rgb(fill) + (alpha,)
            image = Image.new('RGBA', (x2 - x1, y2 - y1), fill)
            images.append(ImageTk.PhotoImage(image))
            self.innerCanvas.create_image(x1, y1, image=images[-1], anchor='nw')
    # self.innerCanvas.create_rectangle(x1, y1, x2, y2, **kwargs)


class mainWindow:
    # GUI Setup Commands
    def __init__(self, name):
        self.name = name

        self.play = False

        self.dialog = None  # initialized later
        self.keyboard = None  # initialized later
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
        self.sheetMusic = sheetmusicGraphics("Sheet Music 1", self.mainCanvas, self.root)

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


def main():
    window = mainWindow("Window")
    window.mainCanvas.grid(row=10, column=0, columnspan=40, rowspan=50)
    window.mainCanvas.configure(background="white")
    window.dialog.grid(row=1, column=3, columnspan=30, rowspan=5, padx=10, pady=10)
    window.keyboard.place(x=52, y=10)
    window.logo.place(x=1400, y=10)
    allura = font.Font(family='Roman', size=10, weight='bold')
    label = tkinter.Label(window.root, text="Team 22", font=allura)
    label1 = tkinter.Label(window.root, text="SDP", font=allura)
    label1.place(x=1360, y=15)
    label.place(x=1350, y=30)
    window.mainCanvas.create_rectangle(0, 0, 1920, 5, fill="grey")
    window.sheetMusic.innerCanvas.place(x=0, y=300)

    # Place dropmenu
    window.dropMenu_1.dropMenuLabel.grid(row=1, column=0, padx=5)
    window.dropMenu_1.dropMenuObject.grid(row=2, column=0, padx=0, pady=5, rowspan=3)
    window.dropMenu_1.dropMenuObject.config(width=7)

    window.dropMenu_2.dropMenuLabel.grid(row=1, column=1, padx=5)
    window.dropMenu_2.dropMenuObject.grid(row=2, column=1, padx=0, rowspan=3)

    window.dropMenu_3.dropMenuLabel.grid(row=1, column=3, padx=5)
    window.dropMenu_3.dropMenuObject.grid(row=2, column=3, padx=0, rowspan=3)
    # Place slider
    window.slider.sliderLabel.grid(row=1, column=4, padx=10)
    window.slider.sliderObject.grid(row=2, column=4, padx=10)

    # An initial loop to pause program until a song is selected and the play button is pressed
    window.outputDialog("Please choose a song to begin the program")

    window.updateWindow()
    ##
    # Test area for GUI

    '''
    for pos in range(9):
        window.sheetMusic.shiftNoteData()
        window.sheetMusic.drawNotes()
        window.updateWindow()
        #window.hideValues()
        time.sleep(1)
    '''
    window.sheetMusic.createNoteData("c4", 2, "Whole")
    window.sheetMusic.createNoteData("d4", 1, "Quarter")
    window.sheetMusic.createNoteData("e4", 1, "Quarter")
    window.sheetMusic.createNoteData("f4", 1, "Quarter")
    window.sheetMusic.createNoteData("g4", 1, "Quarter")
    window.sheetMusic.createNoteData("a5", 1, "Quarter")
    window.sheetMusic.createNoteData("b5", 1, "Quarter")
    window.sheetMusic.createNoteData("c5", 1, "Quarter")
    window.sheetMusic.createNoteData("d5", 1, "Quarter")
    window.sheetMusic.createNoteData("e5", 1, "Quarter")
    window.sheetMusic.createNoteData("f5", 1, "Quarter")
    window.sheetMusic.createNoteData("a6", 1, "Whole")
    window.sheetMusic.createNoteData("c4", 1, "Quarter")
    window.sheetMusic.drawNotes()

    while True:
        condition = window.dropMenu_1.path
        if condition:
            break
        window.updateWindow()
    window.outputDialog("Choose play option to begin song")
    while True:
        playPause = window.dropMenu_2.path
        if playPause:
            break
        window.updateWindow()

    timer = 2  # count down
    while timer:
        window.outputDialog(f"Song Starting in {timer} seconds")
        window.updateWindow()
        time.sleep(1)
        timer = timer - 1
    window.outputDialog("Playing...")

    # Extract the data, and timing requirements from the user's chosen song
    data, ticks_per_sec = readSong(window.dropMenu_1.path)

    i = 0  # i is a count variable for iterating through the data matrix
    tempo_modifier = 1  # a variable that can be adjusted to speed/slow a song
    tend = time.time() + int(data[len(data) - 1][' 0']) / ticks_per_sec  # calculates the time at which song is over
    tstart = time.time()  # calculates the start time

    # This is the main logic loop of the program its setup to loop until the end of the song has been reached
    # this is relative to the timing specified in tics of the MIDI file
    while tstart < tend:
        playPause = window.dropMenu_2.path
        window.outputDialog("Playing...")

        while playPause is False:
            playPause = window.dropMenu_2.path
            window.outputDialog("Paused...")
            window.updateWindow()

        # If statement checks to see if the time of the next note has been reached
        if time.time() > (int(data[i][' 0']) / ticks_per_sec + tstart):
            # from the data, we can extract the proper note, as well as if the instruction is an on or off signal
            on_off, noteNum = iterateSong(data, i)
            # future color option for when we develop color logic
            color = 'red'

            # actually turns on/off the specified note, this is on GUI side only, will need a function for hardware
            size = width * 0.75, height * 0.25

            placeNote(window.keyboard, noteNum, color, on_off, size)

            # increment data to next index
            i = i + 1

            # make sure that each time we loop, the GUI is responsive, with a checkUpdate
            window.updateWindow()

        # still need to make sure GUI is responsive, may be able to eliminate
        window.updateWindow()


if __name__ == "__main__":
    main()
