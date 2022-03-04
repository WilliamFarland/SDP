from GUI_Functions import *
from GUI_Application import *
from MUSIC_Logic import *

import time

control = False
imagePath = 'images/'
size = width * 0.75, height * 0.25

# Sleep Quarter Note
timeQuarter = 1.25
# Sleep Half Note
timeHalf = 2.5


def wait(window, waitTime):
    startTime = time.time()
    while time.time() < startTime + waitTime:
        #time.sleep(0.001)
        window.updateWindow()
        updateKeyboard(window, time.time()-startTime)


def updateKeyboard(window, timeElapsed):
    notesinPlay = []
    for notes in window.sheetMusic.noteList:
        if notes.pos == 6:
            notesinPlay.append(notes)

    if timeElapsed > timeQuarter:
        # shut off any quarters
        for notes in notesinPlay:
            noteName = notes.name
            if notes.noteType == "Quarter":
                for keys in note:
                    vals = note[keys]
                    vals = vals[2]
                    if vals == noteName:
                        noteNum = keys
                        placeNote(window.keyboard, noteNum, 'blue', 0, size)
                        break
    if timeElapsed > timeHalf:
        # shut off any half notes
        for notes in notesinPlay:
            noteName = notes.name
            if notes.noteType == "Half":
                for keys in note:
                    vals = note[keys]
                    vals = vals[2]
                    if vals == noteName:
                        noteNum = keys
                        placeNote(window.keyboard, noteNum, 'blue', 0, size)
                        break

    notesinPlay.clear()


def keyOn(window, notesinPlay):
    for notes in notesinPlay:
        noteName = notes.name
        for keys in note:
            vals = note[keys]
            vals = vals[2]
            if vals == noteName:
                noteNum = keys
                break
        placeNote(window.keyboard, noteNum, 'black', 1, size)


def allOff(window, notesinPlay):
    for notes in notesinPlay:
        noteName = notes.name
        for keys in note:
            vals = note[keys]
            vals = vals[2]
            if vals == noteName:
                noteNum = keys
                break
        placeNote(window.keyboard, noteNum, 'blue', 0, size)

def main():
    # Create Window Object
    # Window Object is main application GUI
    window = mainWindow("Window")

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
    # Old way of extracting MIDI data
    data, ticks_per_sec = SongObject.rawData, SongObject.ticksPerSec
    data = SongObject.cleanData
    timer = 10  # count down
    c = 0
    prevBatch = 0
    batch = 0
    while batch < 4:
        window.outputDialog(f"Song Starting in {timer} seconds")
        window.updateWindow()
        time.sleep(1)
        timer = timer - 1
        noteObject = data[c]
        batch = noteObject.batch
        if batch > prevBatch:
            window.sheetMusic.shiftNoteData()
            prevBatch = batch
        noteNumber = noteObject.noteNum
        noteTranslation = note[noteNumber][2]
        window.sheetMusic.createNoteData(noteTranslation, 10, noteObject.note, 'black')
        window.sheetMusic.drawNotes()
        window.updateWindow()
        wait(window, 0.5)
        c = c + 1


    window.outputDialog("Playing...")

    i = c  # i is a count variable for iterating through the data matrix
    tempo_modifier = 1  # a variable that can be adjusted to speed/slow a song
    tend = 10000000000000000000000 + time.time()
    tstart = time.time()  # calculates the start time
    # This is the main logic loop of the program its setup to loop until the end of the song has been reached
    # this is relative to the timing specified in tics of the MIDI file

    pos = 10
    sleepTime = 0
    batchStart = time.process_time()
    timeStart = 0
    while tstart < tend:
        #updateKeyboard(window, time.time()-timeStart)
        playPause = window.dropMenu_2.path
        window.outputDialog("Playing...")

        while playPause is False:
            playPause = window.dropMenu_2.path
            window.outputDialog("Paused...")
            window.updateWindow()

        notesinPlay = []
        flag = [0]
        for notes in window.sheetMusic.noteList:
            if notes.pos == 6:
                notesinPlay.append(notes)
        for notes in notesinPlay:
            if notes.noteType == "Quarter":
                flag.append(timeQuarter)
            if notes.noteType == "Half":
                flag.append(timeHalf)

        sleepTime = max(flag)

        noteObject = data[i]
        if noteObject.batch > prevBatch:
            timeStart = time.time()
            prevBatch = noteObject.batch
            window.sheetMusic.shiftNoteData()
            window.sheetMusic.drawNotes()
            keyOn(window, notesinPlay)
            window.updateWindow()
            wait(window, sleepTime)
            allOff(window, notesinPlay)

        flag.clear()

        noteNumber = noteObject.noteNum
        noteTranslation = note[noteNumber][2]
        window.sheetMusic.createNoteData(noteTranslation, pos, noteObject.note, 'black')

        i = i + 1

        # make sure that each time we loop, the GUI is responsive, with a checkUpdate
        window.updateWindow()


if __name__ == "__main__":
    main()