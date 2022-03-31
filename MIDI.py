# Beaglebone MIDI recieving code
import Adafruit_BBIO.UART as UART
import serial
import csv
import time

UART.setup("UART1")  # Setup UART1, P9_24 (TX) and P9_26 (RX)

# Open the serial port for UART1 with a baudrate of 31250 (midi standard)
ser = serial.Serial(port="/dev/ttyS1", baudrate=31250)
print(ser.isOpen())


# Note Dictionary for storing Notes
class NoteDict:
    def __init__(self):
        self.data = {}


# Note class
class Note:

    def __init__(self, note, mkey, pressed=0):
        self.note_name = note  # Name of the note (i.e. C4# (middleC))
        self.midi_key = mkey  # Midi number that represents that key
        self.pressed = 0  # Pressed variable to see if note is pressed (currently not in use)

    def _iter_(self):
        return self


# Populate the note dictionary
noteDict = NoteDict()
noteDict.data[36] = Note("c2", 36)
noteDict.data[37] = Note("c2#", 37)
noteDict.data[38] = Note("d2", 38)
noteDict.data[39] = Note("d2#", 39)
noteDict.data[40] = Note("e2", 40)
noteDict.data[41] = Note("f2", 41)
noteDict.data[42] = Note("f2#", 42)
noteDict.data[43] = Note("g2", 43)
noteDict.data[44] = Note("g2#", 44)
noteDict.data[45] = Note("a2", 45)
noteDict.data[46] = Note("a2#", 46)
noteDict.data[47] = Note("b2", 47)
noteDict.data[48] = Note("c3", 48)
noteDict.data[49] = Note("c3#", 49)
noteDict.data[50] = Note("d3", 50)
noteDict.data[51] = Note("d3#", 51)
noteDict.data[52] = Note("e3", 52)
noteDict.data[53] = Note("f3", 53)
noteDict.data[54] = Note("f3#", 54)
noteDict.data[55] = Note("g3", 55)
noteDict.data[56] = Note("g3#", 56)
noteDict.data[57] = Note("a3", 57)
noteDict.data[58] = Note("a3#", 58)
noteDict.data[59] = Note("b3", 59)
noteDict.data[60] = Note("c4", 60)
noteDict.data[61] = Note("c4#", 61)
noteDict.data[62] = Note("d4", 62)
noteDict.data[63] = Note("d4#", 63)
noteDict.data[64] = Note("e4", 64)
noteDict.data[65] = Note("f4", 65)
noteDict.data[66] = Note("f4#", 66)
noteDict.data[67] = Note("g4", 67)
noteDict.data[68] = Note("g4#", 68)
noteDict.data[69] = Note("a4", 69)
noteDict.data[70] = Note("a4#", 70)
noteDict.data[71] = Note("b4", 71)
noteDict.data[72] = Note("c5", 72)
noteDict.data[73] = Note("c5#", 73)
noteDict.data[74] = Note("d5", 74)
noteDict.data[75] = Note("d5#", 75)
noteDict.data[76] = Note("e5", 76)
noteDict.data[77] = Note("f5", 77)
noteDict.data[78] = Note("f5#", 78)
noteDict.data[79] = Note("g5", 79)
noteDict.data[80] = Note("g5#", 80)
noteDict.data[81] = Note("a5", 81)
noteDict.data[82] = Note("a5#", 82)
noteDict.data[83] = Note("b5", 83)
noteDict.data[84] = Note("c6", 84)
noteDict.data[85] = Note("c6#", 85)
noteDict.data[86] = Note("d6", 86)
noteDict.data[87] = Note("d6#", 87)
noteDict.data[88] = Note("e6", 88)
noteDict.data[89] = Note("f6", 89)
noteDict.data[90] = Note("f6#", 90)
noteDict.data[91] = Note("g6", 91)
noteDict.data[92] = Note("g6#", 92)
noteDict.data[93] = Note("a6", 93)
noteDict.data[94] = Note("a6#", 94)
noteDict.data[95] = Note("b6", 95)
noteDict.data[96] = Note("c7", 96)


def writeData(time, keyName, keyNum, onOff):
    f = open('Output.csv', 'a')
    f.write(str(time) + "," + str(keyName) + "," + str(onOff) + str(keyNum) + ", 0"'\n')
    f.close()


# Basic Script for reading if certain notes are pressed/released
while True:
    # Capture command from serial port
    try:
      command = ser.read()
    except:
      print("error: mult access on same port")
    # Convert the byte type to an int values (0-255)
    command = int.from_bytes(command, byteorder='big')
    # Test if Keyboard sent a midi signal of 144 (0b10010000)
    if command == 144:
        # Read the next serial byte from the Keyboard for the MIDI key number (36-96) and convert to int
        key = int.from_bytes(ser.read(1), byteorder='big')
        # Get the musical keyname for that key
        try:
          keyname = noteDict.data[key].note_name
        except:
          print("key error")
          keyname = 'NA'
        # Print the key to terminal
        writeData(time.time(), keyname, key, 1)

 
    # Test if Keyboard sent a midi signal of 128 (0b10000000)
    if command == 128:
        # Read the next serial byte from the Keyboard for the MIDI key number (36-96) and convert to int
        key = int.from_bytes(ser.read(1), byteorder='big')
        # Get the musical keyname for that key
        try:
          keyname = noteDict.data[key].note_name
        except:
          print("key error off")
          keyname = 'na'
        # Print the key to terminal
        print("Time: ", time.time(), "Note Off:", keyname)
        writeData(time.time(), keyname, key, 0)




