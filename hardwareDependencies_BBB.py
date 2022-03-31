from guiDependencies_GUI import *


def importStrip():
    if beaglePluggedin == 1:
        try:
            import strip
            strip.clear()
        except:
            print("Something went wrong with strip library")


def initializeHardware():
    if beaglePluggedin == 1:
        strip.makeStrip(105)
        strip.beginStrip()
        strip.clear()
        strip.show()


def hardwareOn(keyNum, color):
    if beaglePluggedin == 1:
        keyNum = note[keyNum][1]
        keyNum = keyNum * 3 - 3
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
        elif color == 'purple':
            r = 106
            g = 13
            b = 173
        elif color == 'yellow':
            r = 255
            g = 255
            b = 0
        else:
            r = 0
            g = 0
            b = 0
        strip.setPixel([keyNum, g, r, b])
        strip.setPixel([keyNum + 1, g, r, b])
        strip.setPixel([keyNum + 2, g, r, b])

        strip.show()