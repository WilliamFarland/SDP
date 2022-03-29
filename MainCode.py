from GUI_Application import *
from MUSIC_Logic import *
from GHero_GUI import *
import time
import random

control = False
imagePath = 'images/'
size = width * 0.8, height * 0.45
# Sleep Quarter Note
timeQuarter = 1.25
# Sleep Half Note
timeHalf = 2.5
beaglePluggedin = 0

if beaglePluggedin == 1:
    try:
        import strip
    except:
        print("you didnt build alex's library correctly")


def initializeHardware():
    strip.makeStrip(105)
    strip.beginStrip()
    strip.clear()
    strip.show()


def checkError(correctNote):
    value = False
    f = open('Output.csv', 'r')
    rowList=[]
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


def hardwareOn(keyNum, color):
    keyNum = note[keyNum][1]
    keyNum = keyNum * 3 - 3
    if color == 'blue':
        r = 0
        g = 0
        b = 255
    elif color == 'green':
        r = 0
        g = 255
        b = 0
    elif color == 'red':
        r = 255
        g = 0
        b = 0
    elif color == 'off':
        r = 0
        g = 0
        b = 0
    elif color == 'purple':
        r = 106
        g = 13
        b = 173
    elif color == 'yellow':
        r = 255
        g = 255
        b = 0
    else:
        r = 0
        g = 0
        b = 0
    strip.setPixel([keyNum, g, r, b])
    strip.setPixel([keyNum+1, g, r, b])
    strip.setPixel([keyNum+2, g, r, b])


def checkPause(window):
    playPause = window.dropMenu_2.path
    window.outputDialog("Playing...")

    while playPause is False:
        playPause = window.dropMenu_2.path
        window.outputDialog("Paused...")
        window.updateWindow()


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
                           ["Default", "Guitar Hero"])
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


# Extracts Data from selected file
def initialSetup(window, userName):
    if beaglePluggedin == 1:
      strip.clear()
    # Create Window Object
    # Window Object is default application GUI
    # An initial loop to pause program until a song is selected and the play button is pressed
    # Let the user know why we are waiting.... using the outputDialog function

    window.outputDialog("Welcome " + str(userName) + ", please choose a song to begin the program")
    window.updateWindow()
    while True:
        condition = window.dropMenu_1.path
        if condition:
            break
        window.updateWindow()

    window.outputDialog("Please choose play option to begin song after adjusting the tempo")
    window.updateWindow()
    tempo = window.slider.get()
    # Second initial while loop, waits forever until the user presses the play button
    while True:
        playPause = window.dropMenu_2.path
        if playPause:
            break
        window.updateWindow()

    # Extract the data, and timing requirements from the user's chosen song
    # adjust by selected tempo
    if tempo == 1:
        tempoAdjustment = 0.6
    if tempo == 2:
        tempoAdjustment = 0.7
    if tempo == 3:
        tempoAdjustment = 0.8
    if tempo == 4:
        tempoAdjustment = 0.9
    if tempo == 5:
        tempoAdjustment = 1
    if tempo == 6:
        tempoAdjustment = 1.1
    if tempo == 7:
        tempoAdjustment = 1.2
    if tempo == 8:
        tempoAdjustment = 1.3
    if tempo == 9:
        tempoAdjustment = 1.4
    if tempo == 10:
        tempoAdjustment = 1.5

    SongObject = Song(window.dropMenu_1.path)
    SongObject.adjustTempo(tempoAdjustment)
    data = SongObject.cleanData
    fingerPlacement(data)
    convertColor(data)

    for notes in data:
        window.sheetMusic.createNoteData(note[notes.noteNum][2], notes.batch+11, notes.note, notes.color, notes.noteNum)
    return data


def defaultMode(userName):
    window = mainWindow("Window")
    data = initialSetup(window, userName)

    tstart = time.time()

    for i in range(5):
        window.outputDialog("Song Starting in " + str(5- i) + " seconds")
        window.sheetMusic.shiftNoteData()
        window.sheetMusic.drawNotes()
        window.updateWindow()
        time.sleep(1)

    window.sheetMusic.shiftNoteData()
    window.sheetMusic.drawNotes()
    window.outputDialog("Playing...")
    prevBatch = 0
    while data[len(data)-1].turnedOff is False:
        ticker = time.time() - tstart
        checkPause(window)
        for notes in data:
            if ticker >= notes.shiftOn and notes.turnedOn is False:
                # turn on note
                notes.turnedOn = True
                placeNote(window.keyboard, notes.noteNum, notes.color, 1, size)
                if beaglePluggedin == 1:
                    hardwareOn(notes.noteNum, notes.color)
                    strip.show()
                if notes.batch > prevBatch:
                    # Search through previous batch and see what was incorrect/correct
                    noteListforBatch = findBatch(prevBatch, data)
                    for noteinbatch in noteListforBatch:
                        correct = checkError(note[noteinbatch.noteNum][2])
                        print(note[noteinbatch.noteNum][2])
                        print(correct)
                        if correct == True:
                            changeColor(noteinbatch, 'green', window)
                        else:
                            changeColor(noteinbatch, 'red', window)
                            
                    window.sheetMusic.shiftNoteData()
                    window.sheetMusic.drawNotes()
                    prevBatch = notes.batch
            if ticker >= notes.shiftOff and notes.turnedOff is False:
                notes.turnedOff = True
                placeNote(window.keyboard, notes.noteNum, notes.color, 0, size)
                if beaglePluggedin == 1:
                    hardwareOn(notes.noteNum, 'off')
                    strip.show()
        # make sure that each time we loop, the GUI is responsive, with a checkUpdate
        window.updateWindow()

    time.sleep(5)


def guitarHeroMode(userName):
   window = guitarWindow('window')
   initialSetup(window, userName)


def main():
    while True:
        # Clear root if this is the second time in the while loop
        for ele in root.winfo_children():
            ele.destroy()

        # Check if hardware variable is set to True
        if beaglePluggedin == 1:
            initializeHardware()

        # Call initial splash screen
        mode, userName = initialWindow()

        # Call defaultMode if user selects this option
        if mode == 1:
            defaultMode(userName)

        # Call guitarHero if user selects this option
        if mode == 2:
            guitarHeroMode(userName)


if __name__ == "__main__":
    main()
