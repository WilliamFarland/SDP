from GUI_Functions import *
from GUI_Application import *
from MUSIC_Logic import *

import time

control = False
imagePath = 'images/'


def main():
    # Create Window Object
    # Window Object is main application GUI
    window = mainWindow("Window")

    '''
    # Testing zone
    window.sheetMusic.createNoteData("f2", 0, 'Quarter')
    window.sheetMusic.drawNotes()
    window.updateWindow()
    '''

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
    data, ticks_per_sec = SongObject.rawData, SongObject.ticksPerSec

    timer = 5  # count down
    while timer:
        window.outputDialog(f"Song Starting in {timer} seconds")
        window.updateWindow()
        time.sleep(1)
        timer = timer - 1
    window.outputDialog("Playing...")

    i = 0  # i is a count variable for iterating through the data matrix
    tempo_modifier = 0.1  # a variable that can be adjusted to speed/slow a song
    tend = time.time() + (int(data[len(data) - 1][' 0']) / ticks_per_sec)*1/tempo_modifier  # calculates the time at which song is over
    tstart = time.time()  # calculates the start time

    # This is the main logic loop of the program its setup to loop until the end of the song has been reached
    # this is relative to the timing specified in tics of the MIDI file
    prevtimeBatch = 0
    while tstart < tend:
        playPause = window.dropMenu_2.path
        window.outputDialog("Playing...")

        while playPause is False:
            playPause = window.dropMenu_2.path
            window.outputDialog("Paused...")
            window.updateWindow()

        batch = 1
        # If statement checks to see if the time of the next note has been reached
        timeExtract = int(data[i][' 0'])*1/tempo_modifier
        if time.time() > (timeExtract / ticks_per_sec + tstart):
            timeBatch = int(data[i][' 0'])
            on_off = data[i][' Header'] == " Note_on_c"
            if timeBatch > prevtimeBatch and on_off:
                prevtimeBatch = timeBatch
                batch = batch + 1
                window.sheetMusic.shiftNoteData()
                window.sheetMusic.drawNotes()

            if batch > 9:
                batch = 0

            # from the data, we can extract the proper note, as well as if the instruction is an on or off signal
            on_off, noteNum = iterateSong(data, i)
            noteTranslation = note[noteNum][2]
            window.sheetMusic.createNoteData(noteTranslation, batch, 'Quarter')
            # future color option for when we develop color logic
            color = 'blue'

            # actually turns on/off the specified note, this is on GUI side only, will need a function for hardware
            size = width * 0.75, height * 0.25

            placeNote(window.keyboard, noteNum, color, on_off, size)
            # increment data to next index
            i = i + 1

            # make sure that each time we loop, the GUI is responsive, with a checkUpdate
            window.updateWindow()

        # still need to make sure GUI is responsive, may be able to eliminate
        window.updateWindow()


if __name__ == "__main__":
    main()