def calculateSleepTime(tempo):
    if tempo == 1:
        length = 100
    if tempo == 2:
        length = 200
    if tempo == 4:
        length = 400

    timeQuarterNote = (1) * 1 / tempo
    timeSleep = timeQuarterNote/length
    return timeSleep

print(calculateSleepTime(2))