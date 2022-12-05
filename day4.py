# Read day 4 input
# Data downloaded from https://adventofcode.com/2022/day/4/input

# In how many assignment pairs does one range fully contain the other?
import re

overlap = 0
with open('data-day-4.txt') as f:
    for line in f:
        line = line.rstrip()
        # line = 
        # Split string by - and ,
        split_line = re.split('-|,', line)
        # Convert to numeric
        split_line = [int(x) for x in split_line]
        if (split_line[0] >= split_line[2] and split_line[1] <= split_line[3]) or \
            (split_line[0] <= split_line[2] and split_line[1] >= split_line[3]) :
            overlap += 1

print(overlap)

# Part 2
# In how many assignment pairs do the ranges overlap?
# Help from - https://stackoverflow.com/questions/6821156/how-to-find-range-overlap-in-python
overlap2 = 0
with open('data-day-4.txt') as f:
    for line in f:
        line = line.rstrip()
        # line = "97-98,14-98"
        # Split string by - and ,
        split_line = re.split('-|,', line)
        # Convert to numeric
        split_line = [int(x) for x in split_line]
        # Set as ranges
        x = range(split_line[0], split_line[1] + 1) # Add +1 for the upper limit
        y = range(split_line[2], split_line[3] + 1) # Add +1 for the upper limit
        xs = set(x)
        # Check if the two ranger have overlapping numbers
        if len(xs.intersection(y)) > 0:
            overlap2 += 1

print(overlap2)


