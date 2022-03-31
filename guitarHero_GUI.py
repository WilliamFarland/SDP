# GUI for the 2nd mode of project
# 3/29/22
from guiDependencies_GUI import *


def calculateSleepTime(tempo):
    if tempo == 1:
        length = 100
    if tempo == 2:
        length = 200
    if tempo == 4:
        length = 400
    timeQuarterNote = (1) * 1 / tempo
    timeSleep = timeQuarterNote / length
    return timeSleep


class guitarNote:
    def __init__(self, ID, position, color, rectObject):
        self.ID = ID
        self.position = position
        self.color = color
        self.rectObject = rectObject
        self.turnedOff = False
        self.turnedOn = False


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
        self.restartProgramFlag = 0
        self.mainCanvas = Canvas(root, width=width, height=height, highlightthickness=1,
                                 highlightbackground="black")

        self.dropMenu_1 = DropMenu("Menu 1", "Option Menu",
                                   ["File", "Exit", "Save", "Choose Song File"])
        self.dropMenu_2 = DropMenu("Menu 2", "Play/Pause",
                                   ["Play", "Pause"])

        self.current_tempo = tkinter.DoubleVar
        self.slider = tkinter.Scale(root, from_=1, to=10, orient='horizontal', variable=self.current_tempo)
        self.restartButton = Button(root, text='\u21BA', command= lambda: restartProgram(self))
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

    def createRect(self, keyNum, notetype, color, tempoAdjustment):
        keyNum = conv[keyNum]
        if notetype == 'Quarter':
            length = 100
        if notetype == 'Half':
            length = 200
        if notetype == 'Whole':
            length = 400
        length = length/tempoAdjustment
        shift = 43.2 / 2
        ID = random.randrange(1000, 1000000)
        rect = self.mainCanvas.create_rectangle(15 + shift * keyNum, -length, 28 + shift * keyNum, 0, fill=color, tag=str(ID))
        newNote = guitarNote(ID, keyNum, color, rect)
        self.rectDict[ID] = newNote

    def down(self):
        for elements in self.rectDict:
            self.mainCanvas.move(self.rectDict[elements].rectObject, 0, 1)

    def checkOn(self):
        for elements in self.rectDict:
            elements = self.rectDict[elements]
            if elements.turnedOn is False and self.mainCanvas.coords(elements.rectObject)[3] > 570:
                elements.turnedOn = True
                self.turnonKey(elements.position, elements.color)
                if beaglePluggedin == 1:
                    hardwareOn(elements.position, elements.color)
                    strip.show()

    def checkOff(self):
        for elements in self.rectDict:
            elements = self.rectDict[elements]
            if elements.turnedOff is False and self.mainCanvas.coords(elements.rectObject)[1] > 570:
                elements.turnedOff = True
                self.turnoffKey(elements.position)
                self.mainCanvas.delete(str(elements.ID))

                if beaglePluggedin == 1:
                    hardwareOn(elements.position, 'off')
                    strip.show()
