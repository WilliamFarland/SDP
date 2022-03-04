# ---------- Important Variables ----------
# Monitor screen dimensions
height = 1080
width = 1920

note = dict()
note[1] = 'r', 1, 'c1'
note[2] = 's', 1, ''
note[3] = 'r', 2, 'd1'
note[4] = 's', 2, ''
note[5] = 'r', 3, 'e1'
note[6] = 'r', 4, 'f1'
note[7] = 's', 4, ''
note[8] = 'r', 5, 'g1'
note[9] = 's', 5, ''
note[10] = 'r', 6, 'a2'
note[11] = 's', 6, ''
note[12] = 'r', 7, 'b2'
note[13] = 'r', 8, 'c2'
note[14] = 's', 8, ''
note[15] = 'r', 9, 'd2'
note[16] = 's', 9, ''
note[17] = 'r', 10, 'e2'
note[18] = 'r', 11, 'f2'
note[19] = 's', 11, ''
note[20] = 'r', 12, 'g2'
note[21] = 's', 12, ''
note[22] = 'r', 13, 'a3'
note[23] = 's', 13, ''
note[24] = 'r', 14, 'b3'
note[25] = 'r', 15, 'c3'
note[26] = 's', 15, ''
note[27] = 'r', 16, 'd3'
note[28] = 's', 16, ''
note[29] = 'r', 17, 'e3'
note[30] = 'r', 18, 'f3'
note[31] = 's', 18, ''
note[32] = 'r', 19, 'g3'
note[33] = 's', 19, ''
note[34] = 'r', 20, 'a4'
note[35] = 's', 20, ''
note[36] = 'r', 21, 'b4'
note[37] = 'r', 22, 'c4'
note[38] = 's', 22, ''
note[39] = 'r', 23, 'd4'
note[40] = 's', 23, ''
note[41] = 'r', 24, 'e4'
note[42] = 'r', 25, 'f4'
note[43] = 's', 25, ''
note[44] = 'r', 26, 'g4'
note[45] = 's', 26, ''
note[46] = 'r', 27, 'a5'
note[47] = 's', 27, ''
note[48] = 'r', 28, 'b5'
note[49] = 'r', 29, 'c5'
note[50] = 's', 29, ''
note[51] = 'r', 30, 'd5'
note[52] = 's', 30, ''
note[53] = 'r', 31, 'e5'
note[54] = 'r', 32, 'f5'
note[55] = 's', 32, ''
note[56] = 'r', 33, 'g5'
note[57] = 's', 33, ''
note[58] = 'r', 34, 'a6'
note[59] = 's', 34, ''
note[60] = 'r', 35, 'b6'
note[61] = 'r', 36, 'c6'


def updateGUI(root):
    root.update()
    tempo_modifier = root.slider.get()
    return 0


def placeNote(w, noteNum, color, on_off, size):
    if not on_off:
        if note[noteNum][0] == 's':
           color = 'black'
        else:
            color = 'white'

    numKeys = 36
    shift = size[0] / numKeys + 0.5
    if note[noteNum][0] == 's':  # regular note place below sharp notes
        coords = note[noteNum][1] * shift-10, 125, note[noteNum][1] * shift + 10, 150
    if note[noteNum][0] == 'r':  # sharp note place above regular notes
        coords = note[noteNum][1] * shift -35, 170, note[noteNum][1] * shift + 30 - 35, 205

    w.create_rectangle(coords, outline=color, fill=color)
    w.update()


def tempConvert(slider):
    for i in range(1, slider):
        tempoMod = tempoMod + (2-0.1)/10
    return tempoMod


def configureButtons(root, myFont):
    # Pause Button Creation
    control = False
    pause_btn = Button(root, text=u'\u23F8', bd='5', command=test, font=myFont)
    # Play Button Creation
    play_btn = Button(root, text=u'\u23F5', bd='5', command=lambda: control == controlMethod())

    return pause_btn, play_btn, control






