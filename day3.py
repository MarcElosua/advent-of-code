# Read day 3 input
# Data downloaded from https://adventofcode.com/2022/day/3/input

# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

# Set priority scores
import string
print("Alphabet from a-z:")
abc = f"{string.ascii_lowercase}{string.ascii_uppercase}"

score = []
with open('data-day-3.txt') as f:
    for line in f:
        line = line.rstrip()
        leng = len(line)
        mid = int(leng / 2)
        l1 = line[0:mid]
        l2 = line[mid:]
        score.append(abc.index(list(set([*l1]).intersection([*l2]))[0]) + 1)

sum(score)
        
### Part 2
# Find the item type that corresponds to the badges of each three-Elf group.
# What is the sum of the priorities of those item types?

# https://stackoverflow.com/questions/5832856/how-to-read-file-n-lines-at-a-time
from itertools import islice

score2 = []
group_dict = {} # Initialize array
i = 0 # Initialize iterator


# Read and group data
with open('data-day-3.txt') as f:
    for line in f:
        line = line.rstrip()
        # Set new key for the group
        if i % 3 == 0:
            k = i 
            group_dict[f"{k}"] = [] # Initialize new key in dictionary
        # Add line to dictionary
        group_dict[f"{k}"].append([*line])
        i += 1


# Process groups
for k in group_dict:
    # Find the intersect between all lists
    inter = list(set.intersection(*map(set, group_dict[k])))[0]
    # Get priority score & add to score
    score2.append(abc.index(inter) + 1)

# Sum all priorities
sum(score2)
