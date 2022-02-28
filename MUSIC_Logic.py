import csv


def readSong(songName):
    data = []
    with open(songName, newline='') as csvfile:
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

    return data, ticks_per_sec


def iterateSong(data, row):
    noteNum = int(data[row][' 2']) - 23
    if data[row][' Header'] == " Note_on_c":
        on_off = 1
    if data[row][' Header'] == " Note_off_c":
        on_off = 0
    return on_off, noteNum

