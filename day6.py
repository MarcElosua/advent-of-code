# Read day 6 input
# Data downloaded from https://adventofcode.com/2022/day/6/input

# Read initial setting
with open('data-day-6.txt') as f:
    for line in f:
        code = (line.rstrip())

# Set index
i = 0
idx = []
# Iterate over all the possible 4 letter combinations in order
for l in code:
    # Convert to set since sets can't have repeated elements
    print(code[i:i+4])
    if len(set(code[i:i+4])) == 4:
        idx.append(i + 4)
    i += 1

print(idx[0])

# --- Part Two ---
# A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.
# Set index
i = 0
idx = []
# Iterate over all the possible 4 letter combinations in order
for l in code:
    # Convert to set since sets can't have repeated elements
    print(code[i:i+14])
    if len(set(code[i:i+14])) == 14:
        idx.append(i + 14)
    i += 1
