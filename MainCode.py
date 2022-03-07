from GUI_Application import *
from MUSIC_Logic import *
import time

control = False
imagePath = 'images/'
size = width * 0.8, height * 0.45
# Sleep Quarter Note
timeQuarter = 1.25
# Sleep Half Note
timeHalf = 2.5


def checkPause(window):
    playPause = window.dropMenu_2.path
    window.outputDialog("Playing...")

    while playPause is False:
        playPause = window.dropMenu_2.path
        window.outputDialog("Paused...")
        window.updateWindow()


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
    data = SongObject.cleanData
    fingerPlacement(data)
    convertColor(data)
    timer = 5  # count down
   # window.sheetMusic.shiftNoteData()
    goalBatch = 0
    for i in range(timer):
        window.outputDialog(f"Song Starting in {timer-i} seconds")



    window.outputDialog("Playing...")

    tempo_modifier = 1  # a variable that can be adjusted to speed/slow a song
    tend = 10000000000000000000000 + time.time()
    tstart = time.time()  # calculates the start time
    # This is the main logic loop of the program its setup to loop until the end of the song has been reached
    # this is relative to the timing specified in tics of the MIDI file

    for notes in window.sheetMusic.noteList:
        notes.pos = notes.pos + 1

    i = 0
    prevBatch = 1
    while tstart < tend:
        ticker = time.time() - tstart
        checkPause(window)
        for notes in data:
            if ticker >= notes.absoluteOn and notes.turnedOn is False:
                # turn on note
                notes.turnedOn = True
                if notes.batch > prevBatch:
                    window.sheetMusic.shiftNoteData()
                    window.sheetMusic.drawNotes()
                    prevBatch = notes.batch
                window.sheetMusic.createNoteData(note[notes.noteNum][2], 10, notes.note, notes.color)
            if ticker >= notes.absoluteOff and notes.turnedOff is False:
                notes.turnedOff = True
                #placeNote(window.keyboard, notes.noteNum, 'black', 0, size)

            if ticker >= notes.shiftOn and notes.shiftOnprev is False:
                notes.shiftOnprev = True
                placeNote(window.keyboard, notes.noteNum, notes.color, 1, size)
            if ticker >= notes.shiftOff and notes.shiftOffprev is False:
                notes.shiftOffprev = True
                placeNote(window.keyboard, notes.noteNum, notes.color, 0, size)

        time.sleep(0.01)
        window.updateWindow()
        i = i + 1
        # make sure that each time we loop, the GUI is responsive, with a checkUpdate
        window.updateWindow()

if __name__ == "__main__":
    main()
