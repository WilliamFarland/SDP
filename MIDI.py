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
noteDict.data[36] = Note("C2", 36)
noteDict.data[37] = Note("C2#", 37)
noteDict.data[38] = Note("D2", 38)
noteDict.data[39] = Note("D2#", 39)
noteDict.data[40] = Note("E2", 40)
noteDict.data[41] = Note("F2", 41)
noteDict.data[42] = Note("F2#", 42)
noteDict.data[43] = Note("G2", 43)
noteDict.data[44] = Note("G2#", 44)
noteDict.data[45] = Note("A2", 45)
noteDict.data[46] = Note("A2#", 46)
noteDict.data[47] = Note("B2", 47)
noteDict.data[48] = Note("C3", 48)
noteDict.data[49] = Note("C3#", 49)
noteDict.data[50] = Note("D3", 50)
noteDict.data[51] = Note("D3#", 51)
noteDict.data[52] = Note("E3", 52)
noteDict.data[53] = Note("F3", 53)
noteDict.data[54] = Note("F3#", 54)
noteDict.data[55] = Note("G3", 55)
noteDict.data[56] = Note("G3#", 56)
noteDict.data[57] = Note("A3", 57)
noteDict.data[58] = Note("A3#", 58)
noteDict.data[59] = Note("B3", 59)
noteDict.data[60] = Note("C4", 60)
noteDict.data[61] = Note("C4#", 61)
noteDict.data[62] = Note("D4", 62)
noteDict.data[63] = Note("D4#", 63)
noteDict.data[64] = Note("E4", 64)
noteDict.data[65] = Note("F4", 65)
noteDict.data[66] = Note("F4#", 66)
noteDict.data[67] = Note("G4", 67)
noteDict.data[68] = Note("G4#", 68)
noteDict.data[69] = Note("A4", 69)
noteDict.data[70] = Note("A4#", 70)
noteDict.data[71] = Note("B4", 71)
noteDict.data[72] = Note("C5", 72)
noteDict.data[73] = Note("C5#", 73)
noteDict.data[74] = Note("D5", 74)
noteDict.data[75] = Note("D5#", 75)
noteDict.data[76] = Note("E5", 76)
noteDict.data[77] = Note("F5", 77)
noteDict.data[78] = Note("F5#", 78)
noteDict.data[79] = Note("G5", 79)
noteDict.data[80] = Note("G5#", 80)
noteDict.data[81] = Note("A5", 81)
noteDict.data[82] = Note("A5#", 82)
noteDict.data[83] = Note("B5", 83)
noteDict.data[84] = Note("C6", 84)
noteDict.data[85] = Note("C6#", 85)
noteDict.data[86] = Note("D6", 86)
noteDict.data[87] = Note("D6#", 87)
noteDict.data[88] = Note("E6", 88)
noteDict.data[89] = Note("F6", 89)
noteDict.data[90] = Note("F6#", 90)
noteDict.data[91] = Note("G6", 91)
noteDict.data[92] = Note("G6#", 92)
noteDict.data[93] = Note("A6", 93)
noteDict.data[94] = Note("A6#", 94)
noteDict.data[95] = Note("B6", 95)
noteDict.data[96] = Note("C7", 96)



# Basic Script for reading if certain notes are pressed/released
while True:
    # Capture command from serial port
    command = ser.read()
    # Convert the byte type to an int values (0-255)
    command = int.from_bytes(command, byteorder='big')
    # Test if Keyboard sent a midi signal of 144 (0b10010000)
    if command == 144:
        # Read the next serial byte from the Keyboard for the MIDI key number (36-96) and convert to int
        key = int.from_bytes(ser.read(1), byteorder='big')
        # Get the musical keyname for that key
        keyname = noteDict.data[key].note_name
        # Print the key to terminal
        print("Time: ", time.time(), "Note On:", keyname)
        f = open('Output.csv', 'a')
        writer = csv.writer(f)
        row = ['On', str(keyname)]
        writer.writerow(row)
        f.close()
    # Test if Keyboard sent a midi signal of 128 (0b10000000)
    if command == 128:
        # Read the next serial byte from the Keyboard for the MIDI key number (36-96) and convert to int
        key = int.from_bytes(ser.read(1), byteorder='big')
        # Get the musical keyname for that key
        keyname = noteDict.data[key].note_name
        # Print the key to terminal
        print("Time: ", time.time(), "Note Off:", keyname)
        f = open('Output.csv', 'a')
        writer = csv.writer(f)
        row = ['Off', str(keyname)]
        writer.writerow(row)
        f.close()

