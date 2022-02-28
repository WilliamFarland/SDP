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


def controlMethod():
    play = True
    print("Play button was pressed!...")
    return play


def test():
    return


startstop = False  # Configure a pause/play variable for later use


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
        self.menuOptions = menuOptions
        self.clicked = StringVar()
        if self.name == "Menu 1":
            self.clicked.set("File")
        else:
            self.clicked.set("Play/Pause")
        #self.clicked.set("File")
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
            #self.clicked.set("Play/Pause")
            self.path = False
            #print("Pause")
        if flag == "Play":
            self.path = True
            #self.clicked.set("Play/Pause")
            #print("Play")


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
        self.mainCanvas = Canvas(self.root, width=width, height=height, highlightthickness=1, highlightbackground = "black")

        # Create a common font accross the different GUI elements
        self.myFont = font.Font(family='San Francisco', size=10, weight='bold')
        self.myFont_large = font.Font(family='San Francisco', size=15, weight='bold')

        self.slider = Slider(self.root, self.myFont_large, "tempo adjustment", "Tempo Adjustment", 1, 10)
        self.dropMenu_1 = DropMenu(self.root, self.myFont_large, "Menu 1", "Option Menu",
                                   ["File", "Exit", "Save", "Choose Song File"])

        self.dropMenu_2 = DropMenu(self.root, self.myFont_large, "Menu 2", "Play/Pause",
                                   ["Play", "Pause"])

        #self.pauseButton = Btn(self.root, "Pause", "Pause Button", '\u23F8', self.myFont, self.myFont_large)
        #self.playButton = Btn(self.root, "Play", "Play Button", '\u23F5', self.myFont, self.myFont_large)

        self.configureKeyboard()
        self.configureDialog()
        self.configureLogo()

    def configureKeyboard(self):
        # Canvas for Image creation
        w = Canvas(self.mainCanvas, width=width * 0.75, height=height * 0.25)  # Create canvas inside root widget
        w.configure(bg='#FFFFFF')
        # Background Image
        img = Image.open("keyBoardModel.png")  # PIL solution
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
        img2 = Image.open("16th.png")  # PIL solution
        img2 = img2.resize((int(width * 0.05), int(height * 0.05)))
        img2 = ImageTk.PhotoImage(img2)
        self.root.img2 = img2
        w.create_image(0, 0, anchor=NW, image=img2)
        w.update()
        self.logo = w

    def configureDialog(self):
        # Create another canvas for dialog between user and program
        dialog = Frame(self.root, width=width * 0.5, height=height * 0.24)
        #dialog.configure(bg="white", bd=5)
        self.dialog = dialog

    def outputDialog(self, instruction):
        self.clearDialog()
        instrHeader = tkinter.Label(self.dialog, text="DEBUG: ", font=self.myFont_large)
        instrHeader.pack(side = LEFT)
        # Create an initial start instruction before a song is selected
        instr = tkinter.Label(self.dialog, text=instruction, font=self.myFont_large)
        instr.pack(side = LEFT)

    def clearDialog(self):
        for widgets in self.dialog.winfo_children():
            widgets.destroy()

    def updateWindow(self):
        self.root.update()
        self.dropMenu_1.checkValue()
        self.dropMenu_2.checkValue()


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
    window.mainCanvas.configure(background= "white")
    window.dialog.grid(row=1, column=1, columnspan=30, rowspan=5, padx=10, pady=10)
    window.keyboard.place(x=52, y=10)
    window.logo.place(x=1400, y=10)
    allura = font.Font(family='Roman', size=10, weight='bold')
    label = tkinter.Label(window.root, text="Team 22", font=allura)
    label1 = tkinter.Label(window.root, text="SDP", font=allura)
    label1.place(x=1360, y=15)
    label.place(x=1350, y=30)
    window.mainCanvas.create_rectangle(0, 0, 1920, 5, fill="grey")

    # Place dropmenu
    window.dropMenu_1.dropMenuLabel.grid(row=1, column=0, padx=5)
    window.dropMenu_1.dropMenuObject.grid(row=2, column=0, padx=0, pady=5, rowspan=3)
    window.dropMenu_1.dropMenuObject.config(width=7)

    window.dropMenu_2.dropMenuLabel.grid(row=1, column=1, padx=5)
    window.dropMenu_2.dropMenuObject.grid(row=2, column=1, padx=0, rowspan=3)

    # Place slider
    window.slider.sliderLabel.grid(row=1, column=3, padx=10)
    window.slider.sliderObject.grid(row=2, column=3, padx=10)

    # Create header for the instruction dialog box

    # An initial loop to pause program until a song is selected and the play button is pressed
    window.outputDialog("Please choose a song to begin the program")
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
            size = width*0.75, height*0.25

            placeNote(window.keyboard, noteNum, color, on_off, size)

            # increment data to next index
            i = i + 1

            # make sure that each time we loop, the GUI is responsive, with a checkUpdate
            window.updateWindow()

        # still need to make sure GUI is responsive, may be able to eliminate
        window.updateWindow()


if __name__ == "__main__":
    main()
