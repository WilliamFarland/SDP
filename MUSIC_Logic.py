import csv


class Event:
    def __init__(self, onOff, noteNum, tickTime):
        self.onOff = onOff
        self.noteNum = noteNum
        self.tickTime = tickTime
        self.foundOff = False

    def __str__(self):
        print(f"Note: {self.noteNum} \t On/Off: {self.onOff} \t TickTime: {self.tickTime}")

class Song:
    def __init__(self, songName):
        self.songName = songName
        self.data = []

        data = []
        with open(self.songName, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[' Header'] == " Tempo":
                    default_tempo = int(row[' 1'])
                    bbm = 10000000 * 60 / default_tempo
                    ppq = 24
                    ticks_per_min = bbm * ppq
                    ticks_per_sec = ticks_per_min / 60
                if row[' Header'] == " Note_on_c" or row[' Header'] == " Note_off_c":
                    data.append(row)

        csvfile.close()
        self.rawData = data
        self.ticksPerSec = ticks_per_sec

        self.convertData()

    def convertData(self):
        for entries in self.rawData:
            onOff = entries[' Header']
            if onOff == " Note_on_c":
                onOff = 1
            else:
                onOff = 0
            noteNum = int(entries[' 2']) - 23
            tickTime = entries[' 0']
            newNote = Event(onOff, noteNum, tickTime)
            self.data.append(newNote)

    def combineEvents(self):
        for index, events in enumerate(self.data):
            if events.onOff == 1 and events.foundOff is False:
                # Find off point
                while True:
                    nextIndex = index+1
                    nextNote = self.data[nextIndex]
                    if nextNote.noteNum == events.noteNum:



def iterateSong(data, row):
    noteNum = int(data[row][' 2']) - 23
    if data[row][' Header'] == " Note_on_c":
        on_off = 1
    if data[row][' Header'] == " Note_off_c":
        on_off = 0
    return on_off, noteNum

