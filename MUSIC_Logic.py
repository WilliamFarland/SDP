import csv

noteLookup = dict()
noteLookup[244] = "Quarter"
noteLookup[487] = "Half"


def convertColor(noteList):
    for notes in noteList:
        if notes.hand == 'left':
            if notes.finger == 1:
                notes.color = 'red'
            if notes.finger == 2:
                notes.color = 'orange'
            if notes.finger == 3:
                notes.color = 'yellow'
            if notes.finger == 4:
                notes.color = 'green'
            if notes.finger == 5:
                notes.color = 'blue'
        if notes.hand == 'right':
            if notes.finger == 1:
                notes.color = 'purple'
            if notes.finger == 2:
                notes.color = 'cyan'
            if notes.finger == 3:
                notes.color = 'magenta'
            if notes.finger == 4:
                notes.color = 'violet red'
            if notes.finger == 5:
                notes.color = 'goldenrod'


def fingerPlacement(noteList):
    # if note is in play find closest finger to note
    # also, must satisfy all notes are pressed
    currentBatch = 0
    batchedNotes = dict()

    flag = False
    while True:
        for notes in noteList:
            if notes.batch == currentBatch:
                # do the calculation
                batchedNotes.setdefault(notes.batch, [])
                batchedNotes[currentBatch].append(notes)
                flag = True
        if flag is False:
            break
        flag = False
        currentBatch = currentBatch + 1

    keyNumber = []
    for batches in range(currentBatch):
        for notes in batchedNotes[batches]:
            keyNumber.append(notes.noteNum)
        keyNumber.sort()

        # following chopin's natural finger placement
        left = []
        right = []
        leftHand = dict()
        rightHand = dict()
        leftHand[1] = 32
        leftHand[2] = 34
        leftHand[3] = 35
        leftHand[4] = 36
        leftHand[5] = 38
        rightHand[1] = 34
        rightHand[2] = 36
        rightHand[3] = 38
        rightHand[4] = 39
        rightHand[5] = 41

        for vals in keyNumber:
            if vals >= 33:
                right.append(vals)
            else:
                left.append(vals)

        sumLeft = 0
        sumRight = 0
        for vals in left:
            sumLeft = sumLeft + vals
        if sumLeft > 0:
            meanLeft = sumLeft/len(left)
            minLeft = min(left)
            maxLeft = max(left)

        for vals in right:
            sumRight = sumRight + vals
        if sumRight > 0:
            meanRight = sumRight / len(right)
            minRight = min(right)
            maxRight = max(right)

        if len(right) > 0:
            # now assign close values (hopefully)
            rightHand[1] = int(meanRight) - 2
            rightHand[2] = int(meanRight) - 1
            rightHand[3] = int(meanRight)
            rightHand[4] = int(meanRight) + 1
            rightHand[5] = int(meanRight) + 2
        if len(left) > 0:
            # now assign close values (hopefully)
            leftHand[1] = int(meanLeft) - 2
            leftHand[2] = int(meanLeft) - 1
            leftHand[3] = int(meanLeft)
            leftHand[4] = int(meanLeft) + 1
            leftHand[5] = int(meanLeft) + 2

        rightHandTaken = dict()
        rightHandTaken[1] = 0
        rightHandTaken[2] = 0
        rightHandTaken[3] = 0
        rightHandTaken[4] = 0
        rightHandTaken[5] = 0
        leftHandTaken = dict()
        leftHandTaken[1] = 0
        leftHandTaken[2] = 0
        leftHandTaken[3] = 0
        leftHandTaken[4] = 0
        leftHandTaken[5] = 0
        for keys in keyNumber:
            minDistance = 100
            finger = 0
            if keys >= meanRight:
                # assign to right hand
                for fingers in rightHand:
                    if abs(rightHand[fingers] - keys) <= minDistance and rightHandTaken[fingers] == 0:
                        rightHandTaken[fingers] = 1
                        minDistance = abs(rightHand[fingers] - keys)
                        for notes in batchedNotes[batches]:
                            if notes.noteNum == keys:
                                notes.finger = fingers
                                notes.hand = 'right'

            else:
                # assign to left hand
                for fingers in leftHand:
                    if abs(leftHand[fingers] - keys) <= minDistance and leftHandTaken[fingers] == 0:
                        leftHandTaken[fingers] = 1
                        minDistance = rightHand[fingers]
                        for notes in batchedNotes[batches]:
                            if notes.noteNum == keys:
                                notes.finger = fingers
                                notes.hand = 'left'


        keyNumber.clear()
        leftHand.clear()
        rightHand.clear()
        left.clear()
        right.clear()



class Event:
    def __init__(self, onOff, noteNum, tickTime):
        self.onOff = onOff
        self.noteNum = noteNum
        self.onTime = int(tickTime)
        self.offTime = 0
        self.foundOff = False
        self.turnedOn = False
        self.turnedOff = False
        self.timeOn = 0
        self.note = ""
        self.batch = 0
        self.absoluteOn = 0
        self.absoluteOff = 0
        self.shiftOn = 0
        self.shiftOff = 0
        self.shiftOnprev = False
        self.shiftOffprev = False
        self.color = 'black'
        self.finger = ''
        self.hand = ''


    def __str__(self):
        print(f"Note: {self.noteNum} \t On/Off: {self.onOff} \t TickTime: {self.tickTime}")


class Song:
    def __init__(self, songName):
        self.songName = songName
        self.data = []
        self.cleanData = []

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
        self.combineEvents()
        self.clean()
        self.generateTimeline()
        self.calculateDelay()
        print("")

    def calculateDelay(self):
        currMax = 0
        shift = 8.2
        for events in self.cleanData:
            events.shiftOn = events.absoluteOn + shift
            events.shiftOff = events.absoluteOff-events.absoluteOn + events.shiftOn


    def generateTimeline(self):
        for events in self.cleanData:
            if events.note == 'Quarter':
                events.playTime = 1.5  # 1.5 seconds per quarter note
            if events.note == 'Half':
                events.playTime = 3  # 3 seconds per half note

            events.absoluteOn = events.onTime / 162
            events.absoluteOff = (events.onTime / 162) + events.playTime

    def clean(self):
        for events in self.data:
            if events.onOff == 1:
                self.cleanData.append(events)

        prev = 0
        batch = 0
        for events in self.cleanData:
            events.timeOn = int(events.offTime)-int(events.onTime)
            events.note = noteLookup[events.timeOn]
            events.batch = batch

            if int(events.onTime) > int(prev):
                prev = events.onTime
                batch = batch + 1
                events.batch = batch

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
                nextIndex = index
                while True:
                    nextIndex = nextIndex + 1
                    nextNote = self.data[nextIndex]
                    if nextNote.noteNum == events.noteNum:
                        events.foundOff = True
                        events.offTime = nextNote.onTime
                        break


def iterateSong(data, row):
    noteNum = int(data[row][' 2']) - 23
    if data[row][' Header'] == " Note_on_c":
        on_off = 1
    if data[row][' Header'] == " Note_off_c":
        on_off = 0
    return on_off, noteNum
