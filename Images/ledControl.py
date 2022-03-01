import time

ch = input("Please choose a file: ")
f = open(ch, "r")

for lines in f:
    lines = lines.split(",")
    key = lines[0]
    ts = int(lines[1])
    print(key)
    #turnonKey(key, blue)
    time.sleep(ts)