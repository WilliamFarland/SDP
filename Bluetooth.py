import Adafruit_BBIO.UART as UART
import serial
import time

UART.setup("UART4")
ser = serial.Serial(port="/dev/ttyO4", baudrate=9600) #Open serial comm on UART4

def fingOn(finger):

  fing = ['1','2','3','4','5']
  byte_message1 = bytes('6', 'ascii')
  byte_message2 = bytes(fing[finger], 'ascii')
    
  ser.write(byte_message1)
  ser.write(byte_message2)

 

def fingOff(finger):

  fing = ['1','2','3','4','5']
  byte_message1 = bytes('7', 'ascii')
  byte_message2 = bytes(fing[finger], 'ascii')

  ser.write(byte_message1)
  ser.write(byte_message2)
  
def vibOn(finger):
  fing = ['1','2','3','4','5']
  byte_message1 = bytes('8', 'ascii')
  byte_message2 = bytes(fing[finger], 'ascii')

  ser.write(byte_message1)
  ser.write(byte_message2)
  
def vibOff(finger):
  fing = ['1','2','3','4','5']
  byte_message1 = bytes('9', 'ascii')
  byte_message2 = bytes(fing[finger], 'ascii')

  ser.write(byte_message1)
  ser.write(byte_message2)

if ser.isOpen():
  print("Serial is Open")


'''
  while (1) :
   
   
    for i in range(5):
    
        fingOn(i)
        vibOn(i)
        
        time.sleep(1)
        
        fingOff(i)
        vibOff(i)
    
        time.sleep(1)
'''
