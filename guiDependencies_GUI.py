import tkinter
from tkinter import *
from tkinter import font, filedialog
from PIL import ImageTk, Image
import sys
import os
import random
import time

# ---------- Important Variables ----------

beaglePluggedin = 0
restartProgramFlag = 0

# Monitor screen dimensions
width = 1920
height = 1080

size = width * 0.8, height * 0.45


control = False
imagePath = 'images/'

root = Tk()  # Create initial root widget
root.title('SDP - Team 22')  # Name root widget
root.geometry("1536x864")

myFont = font.Font(family='San Francisco', size=10, weight='bold')
myFont_large = font.Font(family='San Francisco', size=15, weight='bold')

note = dict()
note[1] = 'r', 1, 'c1'
note[2] = 's', 1, ''
note[3] = 'r', 2, 'd1'
note[4] = 's', 2, ''
note[5] = 'r', 3, 'e1'
note[6] = 'r', 4, 'f1'
note[7] = 's', 4, ''
note[8] = 'r', 5, 'g1'
note[9] = 's', 5, ''
note[10] = 'r', 6, 'a2'
note[11] = 's', 6, ''
note[12] = 'r', 7, 'b2'
note[13] = 'r', 8, 'c2'
note[14] = 's', 8, ''
note[15] = 'r', 9, 'd2'
note[16] = 's', 9, ''
note[17] = 'r', 10, 'e2'
note[18] = 'r', 11, 'f2'
note[19] = 's', 11, ''
note[20] = 'r', 12, 'g2'
note[21] = 's', 12, ''
note[22] = 'r', 13, 'a3'
note[23] = 's', 13, ''
note[24] = 'r', 14, 'b3'
note[25] = 'r', 15, 'c3'
note[26] = 's', 15, ''
note[27] = 'r', 16, 'd3'
note[28] = 's', 16, ''
note[29] = 'r', 17, 'e3'
note[30] = 'r', 18, 'f3'
note[31] = 's', 18, ''
note[32] = 'r', 19, 'g3'
note[33] = 's', 19, ''
note[34] = 'r', 20, 'a4'
note[35] = 's', 20, ''
note[36] = 'r', 21, 'b4'
note[37] = 'r', 22, 'c4'
note[38] = 's', 22, ''
note[39] = 'r', 23, 'd4'
note[40] = 's', 23, ''
note[41] = 'r', 24, 'e4'
note[42] = 'r', 25, 'f4'
note[43] = 's', 25, ''
note[44] = 'r', 26, 'g4'
note[45] = 's', 26, ''
note[46] = 'r', 27, 'a5'
note[47] = 's', 27, ''
note[48] = 'r', 28, 'b5'
note[49] = 'r', 29, 'c5'
note[50] = 's', 29, ''
note[51] = 'r', 30, 'd5'
note[52] = 's', 30, ''
note[53] = 'r', 31, 'e5'
note[54] = 'r', 32, 'f5'
note[55] = 's', 32, ''
note[56] = 'r', 33, 'g5'
note[57] = 's', 33, ''
note[58] = 'r', 34, 'a6'
note[59] = 's', 34, ''
note[60] = 'r', 35, 'b6'
note[61] = 'r', 36, 'c6'

conv = dict()
conv[1] = 0
conv[2] = 1
conv[3] = 2
conv[4] = 3
conv[5] = 4
conv[6] = 6
conv[7] = 7
conv[8] = 8
conv[9] = 9
conv[10] = 10
conv[11] = 11
conv[12] = 12
conv[13] = 14
conv[14] = 15
conv[15] = 16
conv[16] = 17
conv[17] = 18
conv[18] = 20
conv[19] = 21
conv[20] = 22
conv[21] = 23
conv[22] = 24
conv[23] = 25
conv[24] = 26
conv[25] = 28
conv[26] = 29
conv[27] = 30
conv[28] = 31
conv[29] = 32
conv[30] = 34
conv[31] = 35
conv[32] = 36
conv[33] = 37
conv[34] = 38
conv[35] = 39
conv[36] = 40
conv[37] = 42
conv[38] = 43
conv[39] = 44
conv[40] = 45
conv[41] = 46
conv[42] = 48
conv[43] = 49
conv[44] = 50
conv[45] = 51
conv[46] = 52
conv[47] = 53
conv[48] = 54
conv[49] = 56
conv[50] = 57
conv[51] = 58
conv[52] = 59
conv[53] = 60
conv[54] = 62
conv[55] = 63
conv[56] = 64
conv[57] = 65
conv[58] = 66
conv[59] = 67
conv[60] = 68
conv[61] = 70


conv2 = dict()
conv2[1] = 0
conv2[2] = 1
conv2[3] = 2
conv2[4] = 3
conv2[5] = 4
conv2[6] = 5
conv2[7] = 6
conv2[8] = 7
conv2[9] = 8
conv2[10] = 9
conv2[11] = 10
conv2[12] = 11
conv2[13] = 12
conv2[14] = 13
conv2[15] = 14
conv2[16] = 17
conv2[17] = 18
conv2[18] = 20
conv2[19] = 21
conv2[20] = 22
conv2[21] = 23
conv2[22] = 24
conv2[23] = 25
conv2[24] = 26
conv2[25] = 28
conv2[26] = 29
conv2[27] = 30
conv2[28] = 31
conv2[29] = 32
conv2[30] = 34
conv2[31] = 35
conv2[32] = 36
conv2[33] = 37
conv2[34] = 38
conv2[35] = 39
conv2[36] = 40
conv2[37] = 42
conv2[38] = 43
conv2[39] = 44
conv2[40] = 45
conv2[41] = 46
conv2[42] = 48
conv2[43] = 49
conv2[44] = 50
conv2[45] = 51
conv2[46] = 52
conv2[47] = 53
conv2[48] = 54
conv2[49] = 56
conv2[50] = 57
conv2[51] = 58
conv2[52] = 59
conv2[53] = 60
conv2[54] = 62
conv2[55] = 63
conv2[56] = 64
conv2[57] = 65
conv2[58] = 66
conv2[59] = 67
conv2[60] = 68
conv2[61] = 70



def initialWindow():
    # Choose a functional mode
    w = Frame(root, bg='white', bd=3, height=300, width=400)
    wtop = Frame(root, bg='light grey', bd=3, height=30, width=400)
    w.place(x=550, y=300)
    wtop.place(x=550, y=270)
    # Background Image
    img2 = Image.open(imagePath + "frontLogo.png")  # PIL solution
    img2 = img2.resize((int(400), int(300)))
    img2 = ImageTk.PhotoImage(img2)
    label = Label(w, image=img2)
    label.place(x=0, y=0)
    w.update()
    dropMenu_10 = initialDropMenu(wtop, "Menu 10", "Mode Selection",
                                  ["Default", "Guitar Hero", "Create Music"])
    dropMenu_10.dropMenuObject.place(x=0, y=0)
    dropMenu_10.dropMenuObject.config(bg='light grey')
    inputtxt = tkinter.Text(wtop, height=1, width=20, bg='light grey')
    inputtxt.place(x=220, y=5)
    label = Label(wtop, text="UserName: ", bg='light grey')
    label.place(x=150, y=5)

    count = 1
    while True:
        playPause = dropMenu_10.path
        if playPause:
            break
        mode = dropMenu_10.checkMode()
        root.update()
        r1 = random.randrange(1, 200)
        r2 = random.randrange(1, 200)
        r3 = random.randrange(1, 200)
        if beaglePluggedin:
            strip.setPixel([count, r1, r2, r3])
            strip.show()
        count = count + 1
        if count == 108:
            count = 0

    w.destroy()
    txt = inputtxt.get("1.0", "end-1c")
    wtop.destroy()
    return mode, txt


def checkPause(window):
    playPause = window.dropMenu_2.path
    window.outputDialog("Playing...")
    tstart = time.time()
    while playPause is False:
        playPause = window.dropMenu_2.path
        window.outputDialog("Paused...")
        window.updateWindow()

    return time.time() - tstart


def restartProgram(window):
    window.restartProgramFlag = 1


def updateGUI(root):
    root.update()
    tempo_modifier = root.slider.get()
    return 0


def placeNote(w, noteNum, color, on_off, size):
    if not on_off:
        if note[noteNum][0] == 's':
           color = 'black'
        else:
            color = 'white'

    numKeys = 36
    shift = size[0] / numKeys + 0.5
    if note[noteNum][0] == 's':  # regular note place below sharp notes
        coords = note[noteNum][1] * shift-10, 125, note[noteNum][1] * shift + 10, 150
    if note[noteNum][0] == 'r':  # sharp note place above regular notes
        coords = note[noteNum][1] * shift -35, 185, note[noteNum][1] * shift + 30 - 35, 215

    w.create_rectangle(coords, outline=color, fill=color)
    w.update()


class initialDropMenu:
    def __init__(self, w, name, label, menuOptions):
        self.name = name
        self.path = False
        self.menuOptions = menuOptions
        self.clicked = StringVar()
        self.clicked.set("Mode Selection")

        self.dropMenuObject = OptionMenu(w, self.clicked, *self.menuOptions)
        self.dropMenuLabel = tkinter.Label(text=label, font=myFont_large)

    def checkMode(self):
        flag = self.clicked.get()
        if flag == "Default":
            self.path = True
            return 1
        if flag == "Guitar Hero":
            self.path = True
            return 2
        if flag == "Create Music":
            self.path = True
            return 3

        return 0


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
        if flag == "Save":
            return 'Save'
        if flag == "Play":
            self.path = True
            # self.clicked.set("Play/Pause")
            # print("Play")
        if flag == "Show":
            self.show = True
        if flag == "Hide":
            self.show = False


