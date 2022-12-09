# Read day 8 input
# Data downloaded from https://adventofcode.com/2022/day/8/input

# Read initial setting
import pandas as pd
import numpy as np

# split each element into a new column
grid = []
with open('data-day-8.txt') as f:
    for line in f:
        grid.append([int(i) for i in line.rstrip()])

# Convert grid to pandas df
df = pd.DataFrame(grid)

dim = len(df)
tcoord = []

# Looking from left and right
for idy, j in df.iterrows():
    print(idy)
    dir = df.iloc[idy,:].tolist() # extract row to list
    # iterate over elments in each list
    th = -1 # initial tree heigh, initialize at every row/column
    for idx, t in enumerate(dir):
        if t > th:
            th = t # update tallest tree so far
            tcoord.append(f"{idy},{idx}")
    # Now for the reverse
    th = -1 # initial tree heigh, initialize at every row/column
    # start from the right
    idx = dim - 1 
    # Iterate till 1st element and keep on decrementing i
    while idx >= 0 :  
        print(idx)
        t = dir[idx]
        if t > th:
            th = t # update tallest tree so far
            tcoord.append(f"{idy},{idx}")
        idx -= 1

# Looking from top and bottom
for idx, j in df.iteritems():
    print(idx)
    dir = df.iloc[:,idx].tolist() # extract row to list
    # iterate over elments in each list
    th = -1 # initial tree heigh, initialize at every row/column
    for idy, t in enumerate(dir):
        if t > th:
            th = t # update tallest tree so far
            tcoord.append(f"{idy},{idx}")
    # Now for the reverse
    th = -1 # initial tree heigh, initialize at every row/column
    # start from the right
    idy = dim - 1 
    # Iterate till 1st element and keep on decrementing i
    while idy >= 0 :  
        print(idy)  
        t = dir[idy]
        if t > th:
            th = t # update tallest tree so far
            tcoord.append(f"{idy},{idx}")
        idy -= 1

# --- Part One ---
# Lets find how many unique copies there are
len(set(tcoord))

# --- Part Two ---
# Consider each tree on your map. What is the highest scenic score possible for any tree?
# A tree's scenic score is found by multiplying together its viewing distance in each of the four directions.

# Iterate over all trees X, Y
scores = []
for idx, j in df.iteritems():
    for idy, j in df.iterrows():
        # Once in a position scan all the way to the edges
        # To the left
        idxx = idx - 1
        sl = 0
        while idxx >= 0:
            sl += 1
            if df.iloc[idy,idxx] >= df.iloc[idy,idx]:
                break
            idxx -= 1
        # To the right
        idxx = idx + 1
        sr = 0
        while idxx <= dim-1:
            sr += 1
            if df.iloc[idy,idxx] >= df.iloc[idy,idx]:
                break
            idxx += 1
        # to the top
        idyy = idy - 1
        st = 0
        while idyy >= 0:
            st += 1
            if df.iloc[idyy,idx] >= df.iloc[idy,idx]:
                break
            idyy -= 1
        # to the bottom
        idyy = idy + 1
        sb = 0
        while idyy <= dim-1:
            sb += 1
            if df.iloc[idyy,idx] >= df.iloc[idy,idx]:
                break
            idyy += 1
        # Get tree score
        scores.append([f"{idy},{idx}", sl*sr*st*sb])

# Get which position has the highest scores
s = 0
for x in scores:
    if x[1] > s:
        coord = x
        s = x[1]

print(f"The tree with the best views to build a house is in position {coord[0]} and has a score of {coord[1]}")