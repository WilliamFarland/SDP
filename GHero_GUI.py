# GUI for the 2nd mode of project
# 3/29/22
import time
from GUI_Application import *

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


class guitarWindow:
    # GUI Setup Commands
    def __init__(self, name):
        self.rectDict = dict()
        self.name = name
        self.play = False
        self.dialog = None
        self.keyboard = None
        self.logo = None
        self.imgRef = []
        self.mainCanvas = Canvas(root, width=width, height=height, highlightthickness=1,
                                 highlightbackground="black")

        self.dropMenu_1 = DropMenu("Menu 1", "Option Menu",
                                   ["File", "Exit", "Save", "Choose Song File"])
        self.dropMenu_2 = DropMenu("Menu 2", "Play/Pause",
                                   ["Play", "Pause"])

        self.current_tempo = tkinter.DoubleVar
        self.slider = tkinter.Scale(root, from_=1, to=10, orient='horizontal', variable=self.current_tempo)
        self.restartButton = Button(root, text='\u21BA', command=restartProgram)
        self.configureKeyboard()
        self.configureLogo()
        self.configureDialog()
        self.placeObjects()

    def configureKeyboard(self):
        # Canvas for Image creation
        w = Canvas(self.mainCanvas, width=width * 0.8, height=height * 0.25)  # Create canvas inside root widget
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

    def updateWindow(self):
        root.update()
        self.dropMenu_1.checkValue()
        self.dropMenu_2.checkValue()

    def placeObjects(self):
        self.mainCanvas.grid(row=5, column=0, columnspan=40, rowspan=50)
        self.mainCanvas.configure(background="white")
        #self.dialog.grid(row=1, column=5, rowspan=2, padx=10)
        self.keyboard.place(x=1, y=570)
        self.logo.place(x=1440, y=5)
        # rectangle borders
        self.mainCanvas.create_rectangle(0, 0, 1920, 5, fill="grey")
        # Place dropmenu
        self.dropMenu_1.dropMenuLabel.grid(row=1, column=0, padx=5)
        self.dropMenu_1.dropMenuObject.grid(row=2, column=0, padx=0, rowspan=3)
        #self.dropMenu_1.dropMenuObject.config(width=7)

        self.dropMenu_2.dropMenuLabel.grid(row=1, column=1, padx=5)
        self.dropMenu_2.dropMenuObject.grid(row=2, column=1, padx=0)

        sliderLabel = Label(root, text="Tempo Adjustment", font=myFont_large)
        sliderLabel.grid(row=1, column=2)
        self.slider.grid(row=2, column=2)

        self.dialog.grid(row=0, column=3, columnspan=30, rowspan=5, padx=10)

        restartButtonLabel = Label(root, text="Restart", font=myFont_large)
        restartButtonLabel.grid(row=1, column=3)
        self.restartButton.grid(row=2, column=3)
        shift = 43.2
        self.mainCanvas.create_rectangle(0, 5, 1, 620, fill='grey')
        for i in range(40):
            self.mainCanvas.create_rectangle(0+shift*i, 5, 1+shift*i, 620, fill='grey')

    def configureDialog(self):
        # Create another canvas for dialog between user and program
        dialog = Frame(root, width=width * 0.25, height=50)
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

    def circleGraphic(self, keyNum, color):
        shift = 43.2 / 2
        # add in different
        self.mainCanvas.create_oval(7+shift*keyNum, 550, 12+shift*keyNum+25, 570, fill=color, outline='black', tag=str(keyNum)+'i')

    def turnonKey(self, keyNum, color):
        # dot guitar hero graphic for turning on key
        shift = 43.2/2
        # add in different colors later
        self.circleGraphic(keyNum, color)
        # light up actual key
        self.keyboard.create_rectangle(10 + shift * keyNum, 0, 12+shift*keyNum+20, 300, fill=color,tag=str(keyNum)+'i')

    def turnoffKey(self, keyNum):
        self.mainCanvas.delete(str(keyNum)+'i')
        self.keyboard.delete(str(keyNum)+'i')

    def createRect(self, keyNum, notetype, color='blue'):
        keyNum=keyNum-1
        if notetype == 'quarter':
            length = 50
        if notetype == 'half':
            length = 100
        if notetype == 'whole':
            length = 200
        shift = 43.2 / 2
        rect = self.mainCanvas.create_rectangle(15+shift*(keyNum), 0, 28+shift*(keyNum), length, fill=color)
        self.rectDict[keyNum] = rect

    def down(self):
        for elements in self.rectDict:
            self.mainCanvas.move(self.rectDict[elements], 0, 2)
        time.sleep(0.05)

    def checkOn(self):
        for index, elements in self.rectDict.items():
            ycord = self.mainCanvas.coords(elements)
            ycord = ycord[3]
            if ycord > 570:
                self.turnonKey(index, 'blue')

    def checkOff(self):
        for index, elements in self.rectDict.items():
            ycord = self.mainCanvas.coords(elements)
            ycord = ycord[1]
            if ycord > 568:
                self.turnoffKey(index)