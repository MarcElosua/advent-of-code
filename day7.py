# Read day 6 input
# Data downloaded from https://adventofcode.com/2022/day/6/input

# Read initial setting
import pandas as pd

mem_d = {}
path = []

with open('data-day-7.txt') as f:
    for line in f:
        line = line.rstrip()
        # Split by space
        line_ls = line.split()
        if line.startswith("$ cd"):
            dir = line_ls[2]
            if dir == "/":
                path.append(dir)
            elif dir == "..":
                rm = path.pop()
            else:
                path.append(f"{path[-1]}{'/' if path[-1] != '/' else ''}{dir}")
        if line_ls[0].isnumeric():
            for p in path:
                # initialize each dict key as 0
                if not p in mem_d:
                    mem_d[p] = 0
                mem_d[p] += int(line_ls[0])

# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
print(sum([m for m in mem_d.values() if m <= 100_000]))

# The total disk space available to the filesystem is 70000000. 
# To run the update, you need unused space of at least 30000000. 
# You need to find a directory you can delete that will free up enough space to run the update.
# Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
total = mem_d["/"]
free = 70000000 - total
min_needed = 30000000 - free
# Select those directories with more memory than the required to remove and grab the minimum
min(s for s in mem_d.values() if s >= min_needed)
