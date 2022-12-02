# Read day 1 input
# Data downloaded from https://adventofcode.com/2022/day/1/input
i = 0
data = {}
with open('data-day-1-1.txt') as f:
    for line in f:
        # increase counter by 1
        if line == "\n":
            i += 1
        else:
            # initialize each dict key as a list
            if not f"{i}" in data:
                data[f"{i}"] = []
            # save data to dictionary
            data[f"{i}"].append(int(line.rstrip()))
        

# Parse contents of dictionary summing all the elements within each key
calorie_list = [ sum(data[elf]) for elf in data]

# Get max calories
max(calorie_list)

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
sum(calorie_list[-3:])
