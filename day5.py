# Read day 5 input
# Data downloaded from https://adventofcode.com/2022/day/5/input

# In how many assignment pairs does one range fully contain the other?
import re

layout = {}
# Read initial setting
with open('data-day-5.txt') as f:
    for line in f:
        line = line.rstrip()
        if not "move" in line and "[" in line:
            # Split bins with a regex - https://stackoverflow.com/questions/9475241/split-string-every-nth-character
            arr = re.findall('....?',line)
            # Start iterator to track position
            j = 1
            for i in arr:
                if i != "    ":
                    # Initialize dictionary to store the initial stacks
                    if not f"{j}" in layout:
                        layout[f"{j}"] = []
                    # Append crate label to dictionary
                    layout[f"{j}"].append(i[1]) # [1] to only keep the letter
                j += 1


# Move crates around
with open('data-day-5.txt') as f:
    for line in f:
        if "move" in line:
            line = line.rstrip()
            # line = "move 3 from 1 to 3"
            line_arr = line.split( )
            # Modify layout dictionary
            # https://www.geeksforgeeks.org/python-ways-to-concatenate-two-lists/
            mv = layout[line_arr[3]][:int(line_arr[1])]
            mv.reverse()
            layout[line_arr[5]] = mv + layout[line_arr[5]]
            layout[line_arr[3]] = layout[line_arr[3]][int(line_arr[1]):]


# Extract keys
key_list = []
for i in layout.keys():
    key_list.append(int(i))

# Sort keys
key_list.sort()

# Extract the top crate of each pile
top = []
for key in key_list:
    top.append(layout[f"{key}"][0])

# put any characher to join
s = ""
# joins elements of list1 by '-'
# and stores in string s
s.join(top)

print(s)

## Part 2
# re-read the data 
layout = {}
# Read initial setting
with open('data-day-5.txt') as f:
    for line in f:
        line = line.rstrip()
        if not "move" in line and "[" in line:
            # Split bins with a regex - https://stackoverflow.com/questions/9475241/split-string-every-nth-character
            arr = re.findall('....?',line)
            # Start iterator to track position
            j = 1
            for i in arr:
                if i != "    ":
                    # Initialize dictionary to store the initial stacks
                    if not f"{j}" in layout:
                        layout[f"{j}"] = []
                    # Append crate label to dictionary
                    layout[f"{j}"].append(i[1]) # [1] to only keep the letter
                j += 1

# Move crates around
with open('data-day-5.txt') as f:
    for line in f:
        if "move" in line:
            line = line.rstrip()
            # line = "move 3 from 1 to 3"
            line_arr = line.split( )
            # Modify layout dictionary
            # https://www.geeksforgeeks.org/python-ways-to-concatenate-two-lists/
            mv = layout[line_arr[3]][:int(line_arr[1])]
            layout[line_arr[5]] = mv + layout[line_arr[5]]
            layout[line_arr[3]] = layout[line_arr[3]][int(line_arr[1]):]


# Extract keys
key_list = []
for i in layout.keys():
    key_list.append(int(i))

# Sort keys
key_list.sort()

# Extract the top crate of each pile
top = []
for key in key_list:
    top.append(layout[f"{key}"][0])

# put any characher to join
s = ""
# joins elements of list1 by '-'
# and stores in string s
s.join(top)

print(s)