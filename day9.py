# Read day 9 input
# Data downloaded from https://adventofcode.com/2022/day/9/input
import math

coord_ls = []
xh = 0
yh = 0
xt = 0
yt = 0

with open('data-day-9.txt') as f:
    for line in f:
        line = line.rstrip()
        # line = "U 4"
        # extract information
        d = line.split()[0]
        n = int(line.split()[1])
        # Loop through the information
        while n > 0:
            # Move head
            if d == "R":
                xh += 1
            if d == "L":
                xh -= 1
            if d == "U":
                yh += 1
            if d == "D":
                yh -= 1
            # Check where T is with respect to H, if the distance is within an adjacent spot don't move, if it is then move it accordingly
            # Move tail if H & T and in the same row or tail
            if math.dist([xh, yh], [xt, yt]) == 2:
                print((f"Move tail distance is {math.dist([xh, yh], [xt, yt])} & coordinates are H {[xh, yh]} T {[xt, yt]}"))
                if (xh - xt) > 1:
                    xt += 1
                if (xh - xt) < -1:
                    xt -= 1
                if (yh - yt) > 1:
                    yt += 1
                if (yh - yt) < -1:
                    yt -= 1
                print((f"New coordinates are H {[xh, yh]} T {[xt, yt]}"))
            # Move tail if H & T are diagonally
            elif math.dist([xh, yh], [xt, yt]) > 2:
                print((f"Move tail distance is {math.dist([xh, yh], [xt, yt])} & coordinates are H {[xh, yh]} T {[xt, yt]}"))
                if (xh - xt) >= 1:
                    xt += 1
                if (xh - xt) <= -1:
                    xt -= 1
                if (yh - yt) >= 1:
                    yt += 1
                if (yh - yt) <= -1:
                    yt -= 1
                print((f"New coordinates are H {[xh, yh]} T {[xt, yt]}"))
            else:
                print((f"skip bc distance is {math.dist([xh, yh], [xt, yt])} & coordinates are H {[xh, yh]} T {[xt, yt]}"))
            # Append new coordinate visited by Y
            coord_ls.append(f"{yt},{xt}")
            # Remove one from the counter
            n -= 1

# --- Part One ---
# Lets find how many unique positions where visited
len(set(coord_ls)) # 6503

# --- Part Two ---
# Now, you need to keep track of the positions the new tail, 9, rope length = 10 - H123456789
# Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at least once?
coord_ls2 = []
# Initialize directory
cdict = {}
for i in range(0, 10):
    if not i in cdict:
        cdict[i] = [0,0]

with open('data-day-9.txt') as f:
    for line in f:
        line = line.rstrip()
        # line = "U 4"
        # extract information
        d = line.split()[0]
        n = int(line.split()[1])
        # Loop through the steps
        while n > 0:
            # Move head
            if d == "R":
                cdict[0][0] += 1
            if d == "L":
                cdict[0][0] -= 1
            if d == "U":
                cdict[0][1] += 1
            if d == "D":
                cdict[0][1] -= 1
            # Loop through all the tails bits
            for i in range(1, 10): # This iterates from 1 to 9
                print(i)
                # Check where T is with respect to H, if the distance is within an adjacent spot don't move, if it is then move it accordingly
                # Move tail if H & T and in the same row or tail
                x0 = cdict[i-1][0]
                y0 = cdict[i-1][1]
                x1 = cdict[i][0]
                y1 = cdict[i][1]
                if math.dist([x0, y0], [x1, y1]) == 2:
                    print((f"Move tail distance is {math.dist([x0, y0], [x1, y1])} & coordinates are H {[x0, y0]} T {[x1, y1]}"))
                    if (x0 - x1) > 1:
                        cdict[i][0] += 1
                    if (x0 - x1) < -1:
                        cdict[i][0] -= 1
                    if (y0 - y1) > 1:
                        cdict[i][1] += 1
                    if (y0 - y1) < -1:
                        cdict[i][1] -= 1
                    print((f"New coordinates are H {[x0, y0]} T {[x1, y1]}"))
                # Move tail if H & T are diagonally
                elif math.dist([x0, y0], [x1, y1]) > 2:
                    print((f"Move tail distance is {math.dist([x0, yh], [xt, yt])} & coordinates are H {[x0, yh]} T {[xt, yt]}"))
                    if (x0 - x1) >= 1:
                        cdict[i][0] += 1
                    if (x0 - x1) <= -1:
                        cdict[i][0] -= 1
                    if (y0 - y1) >= 1:
                        cdict[i][1] += 1
                    if (y0 - y1) <= -1:
                        cdict[i][1] -= 1
                    print((f"New coordinates are H {[x0, y0]} T {[cdict[i][0],cdict[i][1]]}"))
                else:
                    print((f"skip bc distance is {math.dist([x0, y0], [cdict[i][0],cdict[i][1]])} & coordinates are H {[x0, y0]} T {[cdict[i][0],cdict[i][1]]}"))
                if i == 9:
                    # Append new coordinate visited by Y
                    coord_ls2.append(f"{cdict[i][1]},{cdict[i][0]}")
            # Remove one from the counter
            n -= 1

cdict
coord_ls2
len(set(coord_ls2)) # 2724
