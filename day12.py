# Read day 12 input
# Data downloaded from https://adventofcode.com/2022/day/12/input

# letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.
# Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E).
#  Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

# You'd like to reach E, but to save energy, you should do it in as few steps as possible.
#  During each step, you can move exactly one square up, down, left, or right. 
# To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation 
# of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. 
# (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

# What is the fewest steps required to move from your current position to the location that should get the best signal?

# My reasoning is to start from the end and work backwards
import pandas as pd
import string

df = pd.read_csv('data-day-12.txt', names=["string"], header=None)
df = df.string.str.split("", expand=True)
# drop first & last columns
df = df.iloc[:, 1:-1]

# Start from the end and try to find the shortest path to the end
for j in range(df.shape[1]): # columns
    print('Column Name : ', j)
    for i in range(df.shape[0]): # rows
        print('Row Name : ', i)
        if df.iloc[i, j] == 'S':
            start = (int(i), int(j))

for j in range(df.shape[1]): # columns
    print('Column Name : ', j)
    for i in range(df.shape[0]): # rows
        print('Row Name : ', i)
        if df.iloc[i, j] == 'E':
            end = (int(i), int(j))

queue = [start]
step_ls = [0]
visited = set()
visited2 = []
n = 0
while len(queue) > 0:
    # Extract current node
    row, col = queue.pop()
    step = step_ls.pop()
    if (row, col) == end:
        print(f"Number of steps necessary are: {step}")
        break
    counter = step
    step += 1
    # Add node to the visited set
    visited.add((row, col))
    visited2.append((row, col, step))
    # Get letter & height
    l = df.iloc[row, col]
    if l == "S":
        l = "a"
    elif l == "E":
        l = "z"
    h = string.ascii_lowercase.index(l)
    # Check the 4 neighbors
    options = [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]
    real_options = [x for x in options if (x[0] >= 0) and (x[1] >= 0) and (x[0] <= df.shape[0]-1) and (x[1] <= df.shape[1]-1) and x not in visited]
    # queue + real_options
    for i in real_options:
        # print(f"testing neighboor {i}")
        # Don't visit inexistent positions
        lt = df.iloc[i[0], i[1]]
        if lt == "E":
            lt = "z"
        # print(f"letter is {lt} & coord is {i}")
        ht = string.ascii_lowercase.index(lt)
        if (ht <= h+1) and (i not in queue):
            # Add new elements to the begining of the list since we are "popping" them from the back
            queue.insert(0, i)
            step_ls.insert(0, step)


# Part 1 solution
# We remove 1 from the final solution since we have added the counter at the end of the process so it goes 1 extra
for i in visited2:
    if (i[0], i[1]) == end:
        print(i)
        print(f"Number of steps necessary are: {i[2]}")

print(f"Minimum number of steps required to get to the END is {list(counter)[-1]-1}")
# Minimum number of steps required to get to the END is 472

# --- Part Two ---
# To maximize exercise while hiking, the trail should start as low as possible: elevation a.
# The goal is still the square marked E. However, the trail should still be direct, 
# taking the fewest steps to reach its goal. So, you'll need to find the shortest path from any square at elevation a to the square marked E.
start_ls = []
for j in range(df.shape[1]): # columns
    print('Column Name : ', j)
    for i in range(df.shape[0]): # rows
        print('Row Name : ', i)
        if df.iloc[i, j] in ['S', 'a']:
            start_ls.append((int(i), int(j)))

# Iterate over all starting points
min_ls = []
for start in start_ls:
    queue = [start]
    step_ls = [0]
    visited = set()
    # visited2 = []
    # n = 0
    while len(queue) > 0:
        # Extract current node
        row, col = queue.pop()
        step = step_ls.pop()
        if (row, col) == end:
            print(f"Number of steps necessary are: {step}")
            counter = step
            break
        # counter = step
        step += 1
        # Add node to the visited set
        visited.add((row, col))
        # visited2.append((row, col, step))
        # Get letter & height
        l = df.iloc[row, col]
        if l == "S":
            l = "a"
        elif l == "E":
            l = "z"
        h = string.ascii_lowercase.index(l)
        # Check the 4 neighbors
        options = [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]
        real_options = [x for x in options if (x[0] >= 0) and (x[1] >= 0) and (x[0] <= df.shape[0]-1) and (x[1] <= df.shape[1]-1) and x not in visited]
        # queue + real_options
        for i in real_options:
            # print(f"testing neighboor {i}")
            # Don't visit inexistent positions
            lt = df.iloc[i[0], i[1]]
            if lt == "S":
                lt = "a"
            elif lt == "E":
                lt = "z"
            # print(f"letter is {lt} & coord is {i}")
            ht = string.ascii_lowercase.index(lt)
            if (ht <= h+1) and (i not in queue):
                # Add new elements to the begining of the list since we are "popping" them from the back
                queue.insert(0, i)
                step_ls.insert(0, step)
    # Save the minimum number of steps for each start
    min_ls.append(counter)

## Solution
print(f"Minimum number of steps to go from an a to the E is {min(min_ls)}")