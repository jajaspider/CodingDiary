import sys

N = int(sys.stdin.readline())
serial = []

for _ in range(0, N):
    Nserial = sys.stdin.readline().replace("\n", "")
    Nserialnum = 0
    for i in Nserial:
        if i.isdigit():
            Nserialnum += int(i)
    serial.append((Nserial, Nserialnum))

serial.sort(key=lambda x: (len(x[0]), x[1], x[0]))
for i in range(0, len(serial)):
    print(serial[i][0])
