from tkinter import *
from PIL import ImageTk, Image


# Monitor screen dimensions
height = 1080
width = 1920
imagePath = 'images/'

noteHeight = dict()
noteHeight['f2'] = 435
noteHeight['g2'] = 425
noteHeight['a3'] = 410
noteHeight['b3'] = 395
noteHeight['c3'] = 380
noteHeight['d3'] = 365
noteHeight['e3'] = 352
noteHeight['f3'] = 338
noteHeight['g3'] = 325
noteHeight['a4'] = 310
noteHeight['b4'] = 300
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


class NoteVariable:
    def __init__(self, name, noteType, pos):
        self.name = name
        self.noteType = noteType
        self.pos = pos


class SheetMusicGraphics:
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
        self.noteList = []
        print(self.noteList)

    def drawNote(self, note):
        y = noteHeight[note.name]
        noteType = note.noteType
        pos = note.pos
        x = self.midCord[pos - 1]
        if note.name == "c4":
            self.innerCanvas.create_line(x - 20, 185, x + 40, 185, width=3, tag='notes')
        if note.name == "a6":
            self.innerCanvas.create_line(x - 20, 25, x + 40, 25, width=3, tag='notes')
        if noteType == "Quarter":
            self.drawQuarterNote(pos, y)
        if noteType == "Half":
            self.drawHalfNote(pos, y)
        if noteType == "Eighth":
            self.drawEighthNote(pos, y)
        if noteType == "Whole":
            self.drawWholeNote(pos, y)

    def drawNotes(self):
        for notes in self.noteList:
            if notes.pos < 10:
                self.drawNote(notes)

    def shiftNoteData(self):
        for notes in self.noteList:
            notes.pos = notes.pos + 1
        self.deleteNotes()

    def createNoteData(self, note, pos, noteType):
        newNote = NoteVariable(note, noteType, pos)
        self.noteList.append(newNote)

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
        oval = self.innerCanvas.create_oval(x-7, y-2, x + 30, y + 22, fill='', width=4.5, tags='notes')

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