from defaultMode_GUI import *
from guitarHero_GUI import *
from createMode_GUI import *

from MUSIC_Logic import *
from hardwareDependencies_BBB import *

import time
from time import process_time as timer
import random

# Sleep Quarter Note
timeQuarter = 1.25
# Sleep Half Note
timeHalf = 2.5


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
        exitCode = dropMenu_10.path
        if exitCode:
            break
        mode = dropMenu_10.checkMode()
        root.update()
        r1 = random.randrange(1, 200)
        r2 = random.randrange(1, 200)
        r3 = random.randrange(1, 200)
        hardwareOn(count, [r1, r2, r3])
        count = count + 1
        if count == 108:
            count = 0

    w.destroy()
    txt = inputtxt.get("1.0", "end-1c")
    wtop.destroy()
    return mode, txt


# Extracts Data from selected file
def dataExtraction(window, userName):
    if window.restartProgramFlag == 1:
        return None, None
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
        if window.restartProgramFlag == 1:
            return None, None

    window.outputDialog("Please choose play option to begin song after adjusting the tempo")
    window.updateWindow()

    # Second initial while loop, waits forever until the user presses the play button
    while True:
        playPause = window.dropMenu_2.path
        if playPause:
            break
        window.updateWindow()
        if window.restartProgramFlag == 1:
            return None, None

    tempo = window.current_tempo
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
        tempoAdjustment = 2
    if tempo == 9:
        tempoAdjustment = 3
    if tempo == 10:
        tempoAdjustment = 4

    SongObject = Song(window.dropMenu_1.path)
    # SongObject.adjustTempo(tempoAdjustment)
    data = SongObject.cleanData
    fingerPlacement(data)
    convertColor(data)
    tempoAdjustment = 1
    return data, tempoAdjustment


def defaultMode(userName):
    window = defaultWindow("Window")
    data, tempoAdjustment = dataExtraction(window, userName)
    if window.restartProgramFlag == 1:
        return
    for notes in data:
        window.sheetMusic.createNoteData(note[notes.noteNum][2], notes.batch + 11, notes.note, notes.color,
                                         notes.noteNum)
    tstart = time.time()

    for i in range(5):
        window.outputDialog("Song Starting in " + str(5 - i) + " seconds")
        window.sheetMusic.shiftNoteData()
        window.sheetMusic.drawNotes()
        window.updateWindow()
        time.sleep(1)
        if window.restartProgramFlag == 1:
            return

    window.sheetMusic.shiftNoteData()
    window.sheetMusic.drawNotes()
    window.outputDialog("Playing...")
    prevBatch = 0
    delay = 0
    while data[len(data) - 1].turnedOff is False:
        ticker = time.time() - tstart - delay
        delay = delay + checkPause(window)
        for notes in data:
            if ticker >= notes.shiftOn and notes.turnedOn is False:
                # turn on note
                notes.turnedOn = True
                placeNote(window.keyboard, notes.noteNum, notes.color, 1, size)
                hardwareOn(notes.noteNum, notes.color)
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
                hardwareOn(notes.noteNum, 'off')
        if window.restartProgramFlag == 1:
            return
        # make sure that each time we loop, the GUI is responsive, with a checkUpdate
        window.updateWindow()

    time.sleep(5)


def guitarHeroMode(userName):
    window = guitarWindow('window')
    if window.restartProgramFlag == 1:
        return
    data, tempoAdjustment = dataExtraction(window, userName)
    if window.restartProgramFlag == 1:
        return
    tempoAdjustment = 1
    for i in range(5):
        window.outputDialog("Song Starting in " + str(5 - i) + " seconds")
        window.updateWindow()
        time.sleep(1)
        if window.restartProgramFlag == 1:
            return
    window.outputDialog("Playing...")

    ts = calculateSleepTime(tempoAdjustment)
    #     checkPause(window)
    for notes in data:
        notes.startY = notes.absoluteOn * 100
        notes.stopY = notes.absoluteOff * 100

    tStart = timer()
    count = 0.01
    while timer() < tStart + data[len(data) - 1].absoluteOff + 15:
        timeElapsed = timer() - tStart

        if timeElapsed > count:
            count = count + 0.01
            window.down()

        currY = timeElapsed*100
        for notes in data:
            if notes.startY <= currY and notes.turnedOn is False:
                notes.turnedOn = True
                window.createRect(notes.noteNum, notes.note, notes.color, tempoAdjustment)

        window.checkOn()
        window.checkOff()
        window.updateWindow()

        if window.restartProgramFlag == 1:
            return


def createMusicMode(userName):
    window = createWindow('window')
    window.outputDialog("Welcome, " + str(userName) + " lets start creating!")
    while True:
        if window.updateWindow() == 'Save':
            return

        data = readMIDIData()
        for rows in data:
            if rows[4] == 0:
                # we haven't touched this yet
                if rows[2] == 1:
                    window.turnonKey(str(rows[2]), color='blue')
                if rows[2] == 0:
                    window.turnoffKey(str(rows[2]))


        if window.restartProgramFlag == 1:
            return


def main():
    while True:
        # Clear Output file, so program doesnt load slowly
        open('Output.csv', 'w').close()

        # Clear root, if this is the second time running the program
        for child in root.winfo_children():
            child.destroy()

        # Check if hardware variable is set to True
        if beaglePluggedin == 1:
            initializeHardware()

        # Call initial splash screen
        mode, userName = initialWindow()

        # Call defaultMode if user selects option 1
        if mode == 1:
            defaultMode(userName)

        # Call guitarHero if user selects option 2
        if mode == 2:
            guitarHeroMode(userName)

        # Call createMode if user selects option 3
        if mode == 3:
            createMusicMode(userName)


if __name__ == "__main__":
    main()
