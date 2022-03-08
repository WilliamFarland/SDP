
from GUI_Application import *
from MUSIC_Logic import *
import time
import csv
import os

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
        # exec(open("MIDI.py").read())
    except:
        print("you didnt build alex's library correctly")



def initializeHardware():
    strip.makeStrip(105)
    strip.beginStrip()
    strip.clear()
    strip.show()


def hardwareOn(keyNum, color):
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
    else:
        r = 255
        g = 255
        b = 255
    strip.setPixel([keyNum, r, g, b])


def checkPause(window):
    playPause = window.dropMenu_2.path
    window.outputDialog("Playing...")

    while playPause is False:
        playPause = window.dropMenu_2.path
        window.outputDialog("Paused...")
        window.updateWindow()


def clearOutput():
    try:
        os.remove("Output.csv")
    except:
        print("No need to remove Output as it dosent exsist...")



def main():
    clearOutput()
    # Create Window Object
    # Window Object is main application GUI
    window = mainWindow("Window")
    if beaglePluggedin == 1:
        initializeHardware()
    # An initial loop to pause program until a song is selected and the play button is pressed
    # Let the user know why we are waiting.... using the outputDialog function
    window.outputDialog("Please choose a song to begin the program")
    window.updateWindow()
    while True:
        condition = window.dropMenu_1.path
        if condition:
            break
        window.updateWindow()

    window.outputDialog("Choose play option to begin song")
    window.updateWindow()
    # Second initial while loop, waits forever until the user presses the play button
    while True:
        playPause = window.dropMenu_2.path
        if playPause:
            break
        window.updateWindow()

    # Extract the data, and timing requirements from the user's chosen song
    SongObject = Song(window.dropMenu_1.path)
    data = SongObject.cleanData
    fingerPlacement(data)
    convertColor(data)
    timer = 5  # count down
    tempo_modifier = 1  # a variable that can be adjusted to speed/slow a song
    tend = 10000000000000000000000 + time.time()
    tstart = time.time()   # calculates the start time
    # This is the main logic loop of the program its setup to loop until the end of the song has been reached
    # this is relative to the timing specified in tics of the MIDI file

    for notes in data:
        window.sheetMusic.createNoteData(note[notes.noteNum][2], notes.batch+9, notes.note, notes.color)

    for i in range(timer):
        window.outputDialog("Song Starting in " + str(timer - i) + " seconds")
        time.sleep(1)
        window.sheetMusic.shiftNoteData()
        window.sheetMusic.drawNotes()
        window.updateWindow()
    window.outputDialog("Playing...")

    prevBatch = 1
    while tstart < tend:
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
                    window.sheetMusic.shiftNoteData()
                    window.sheetMusic.drawNotes()
                    prevBatch = notes.batch
            if ticker >= notes.shiftOff and notes.turnedOff is False:
                notes.turnedOff = True
                try:
                    f = open("Output.csv")
                    lines = f.readlines()
                    for line in lines:
                        line = line.split(',')
                        timeFromFile = line[1]
                        onOff = line[2]
                        noteNum = line[3]
                        if noteNum == notes.noteNum and abs(float(timeFromFile) - float(notes.shiftOff)) < 1.5 and onOff == 'Off':
                            notes.color == 'green'
                        else:
                            notes.color == 'red'

                except FileNotFoundError:
                    print("Output does not exist")
                placeNote(window.keyboard, notes.noteNum, notes.color, 0, size)
                if beaglePluggedin == 1:
                    hardwareOn(notes.noteNum, 'off')
                    strip.show()
        # make sure that each time we loop, the GUI is responsive, with a checkUpdate
        window.updateWindow()

if __name__ == "__main__":
    main()
