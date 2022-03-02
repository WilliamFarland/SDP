from GUI_Functions import *
from GUI_Application import *
from MUSIC_Logic import *

import time
import tkinter


control = False
imagePath = 'images/'


def main():
    window = mainWindow("Window")
    window.mainCanvas.grid(row=10, column=0, columnspan=40, rowspan=50)
    window.mainCanvas.configure(background="white")
    window.dialog.grid(row=1, column=3, columnspan=30, rowspan=5, padx=10, pady=10)
    window.keyboard.place(x=52, y=10)
    window.logo.place(x=1400, y=10)
    allura = font.Font(family='Roman', size=10, weight='bold')
    label = tkinter.Label(window.root, text="Team 22", font=allura)
    label1 = tkinter.Label(window.root, text="SDP", font=allura)
    label1.place(x=1360, y=15)
    label.place(x=1350, y=30)
    window.mainCanvas.create_rectangle(0, 0, 1920, 5, fill="grey")
    window.sheetMusic.innerCanvas.place(x=0, y=300)

    # Place dropmenu
    window.dropMenu_1.dropMenuLabel.grid(row=1, column=0, padx=5)
    window.dropMenu_1.dropMenuObject.grid(row=2, column=0, padx=0, pady=5, rowspan=3)
    window.dropMenu_1.dropMenuObject.config(width=7)

    window.dropMenu_2.dropMenuLabel.grid(row=1, column=1, padx=5)
    window.dropMenu_2.dropMenuObject.grid(row=2, column=1, padx=0, rowspan=3)

    window.dropMenu_3.dropMenuLabel.grid(row=1, column=3, padx=5)
    window.dropMenu_3.dropMenuObject.grid(row=2, column=3, padx=0, rowspan=3)
    # Place slider
    window.slider.sliderLabel.grid(row=1, column=4, padx=10)
    window.slider.sliderObject.grid(row=2, column=4, padx=10)

    # An initial loop to pause program until a song is selected and the play button is pressed
    window.outputDialog("Please choose a song to begin the program")

    window.updateWindow()

    while True:
        condition = window.dropMenu_1.path
        if condition:
            break
        window.updateWindow()
    window.outputDialog("Choose play option to begin song")
    while True:
        playPause = window.dropMenu_2.path
        if playPause:
            break
        window.updateWindow()

    # Extract the data, and timing requirements from the user's chosen song
    data, ticks_per_sec = readSong(window.dropMenu_1.path)

    timer = 5  # count down
    while timer:
        window.outputDialog(f"Song Starting in {timer} seconds")
        window.updateWindow()
        time.sleep(1)
        timer = timer - 1
    window.outputDialog("Playing...")

    i = 0  # i is a count variable for iterating through the data matrix
    tempo_modifier = 1  # a variable that can be adjusted to speed/slow a song
    tend = time.time() + int(data[len(data) - 1][' 0']) / ticks_per_sec  # calculates the time at which song is over
    tstart = time.time()  # calculates the start time

    # This is the main logic loop of the program its setup to loop until the end of the song has been reached
    # this is relative to the timing specified in tics of the MIDI file
    while tstart < tend:
        playPause = window.dropMenu_2.path
        window.outputDialog("Playing...")

        while playPause is False:
            playPause = window.dropMenu_2.path
            window.outputDialog("Paused...")
            window.updateWindow()

        # If statement checks to see if the time of the next note has been reached
        if time.time() > (int(data[i][' 0']) / ticks_per_sec + tstart):
            # from the data, we can extract the proper note, as well as if the instruction is an on or off signal
            on_off, noteNum = iterateSong(data, i)
            # future color option for when we develop color logic
            color = 'red'

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