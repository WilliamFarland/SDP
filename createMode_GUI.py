# GUI for the 3rd mode of project
# 3/29/22
from guiDependencies_GUI import *
import csv


def readMIDIData():
    f = open('Output.csv', 'r')
    rowList = []
    reader = csv.reader(f, delimiter=",")
    for rows in reader:
        rowList.append(rows)
    f.close()
    return rowList

class createWindow:
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

        if self.dropMenu_1.checkValue() == "Save":
            return 'Save'

    def placeObjects(self):
        self.mainCanvas.grid(row=5, column=0, columnspan=40, rowspan=50)
        self.mainCanvas.configure(background="white")
        self.keyboard.place(x=1, y=270)
        self.logo.place(x=1440, y=5)
        # rectangle borders
        self.mainCanvas.create_rectangle(0, 0, 1920, 5, fill="grey")
        self.dropMenu_1.dropMenuLabel.grid(row=1, column=0, padx=5)
        self.dropMenu_1.dropMenuObject.grid(row=2, column=0, padx=0, rowspan=3)

        self.dropMenu_2.dropMenuLabel.grid(row=1, column=1, padx=5)
        self.dropMenu_2.dropMenuObject.grid(row=2, column=1, padx=0)

        sliderLabel = Label(root, text="Tempo Adjustment", font=myFont_large)
        sliderLabel.grid(row=1, column=2)
        self.slider.grid(row=2, column=2)

        self.dialog.grid(row=0, column=3, columnspan=30, rowspan=5, padx=10)

        restartButtonLabel = Label(root, text="Restart", font=myFont_large)
        restartButtonLabel.grid(row=1, column=3)
        self.restartButton.grid(row=2, column=3)

        frame1 = Canvas(self.mainCanvas, highlightbackground="black", highlightthickness=2)
        frame1.configure(width=300, height=200)
        img2 = Image.open(imagePath + "creatorsModeGraphic.png")  # PIL solution
        img2 = img2.resize((int(300), int(200)))
        img2 = ImageTk.PhotoImage(img2)
        root.img15 = img2
        frame1.create_image(0, 0, anchor=NW, image=img2)
        frame1.place(x=600, y=10)

        shift = 43.2
        #self.mainCanvas.create_rectangle(0, 5, 1, 637, fill='grey')
        for i in range(40):
            self.mainCanvas.create_rectangle(0+shift*i, 220, 1+shift*i, 590, fill='grey')

        self.mainCanvas.create_rectangle(0, 220, 1920, 222, fill="grey")
        self.mainCanvas.create_rectangle(0, 588, 1920, 590, fill="grey")

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


