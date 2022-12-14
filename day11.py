# Read day 11 input
# Data downloaded from https://adventofcode.com/2022/day/11/input
import math
# Chasing all of the monkeys at once is impossible; you're going to have to focus on the two most active monkeys 
# if you want any hope of getting your stuff back. Count the total number of times each monkey inspects items over 20 rounds:


# 1st step is to parse the data
dict = {}
with open('data-day-11.txt') as f:
    for line in f:
        line = line.strip()
        if "Monkey" in line:
            monk = line.split()[1][0]
            if not monk in dict:
                dict[f"monkey {monk}"] = {}
                dict[f"monkey {monk}"]["counter"] = 0
        if "Starting" in line:
            # split line to get worry numbers
            dict[f"monkey {monk}"]["items"] = [int(x) for x in line.split(": ")[1].split(", ")]
        if "Operation" in line:        
            dict[f"monkey {monk}"]["operation"] = line.split(": ")[1].split("=")[1].strip()
        if "Test" in line:        
            dict[f"monkey {monk}"]["test"] = int(line.split(" ")[-1])
        if "true" in line:        
            dict[f"monkey {monk}"]["true"] = line.split(": ")[1].split()[3]
        if "false" in line:        
            dict[f"monkey {monk}"]["false"] = line.split(": ")[1].split()[3]

# Run 20 cycles and keep track of how many items each monkey looks at
cycle = 0

while cycle < 20:
    print(f"cycle: {cycle}")
    for key in dict:
        print(f"key: {key}")
        if len(dict[key]["items"]) > 0:
            for old in dict[key]["items"]:
                print(f"items for {key} are {dict[key]['items']}")
                # operation - different one for each monkey
                mod = eval(dict[key]['operation'])
                print(f"Worry level is multiplied by 19 to {mod}.")
                # divide by 3
                mod = math.floor(mod / 3)
                print(f"Worry level is divide by 3 to {mod}.")
                # test
                if mod % dict[key]['test'] == 0:
                    m = f"monkey {dict[key]['true']}"
                else:
                    m = f"monkey {dict[key]['false']}"
                print(f"Item is passed to {m}.")
                # pass to other monkey
                dict[m]['items'].append(mod)
                # add counter
                dict[key]['counter'] += 1
            # Remove from item list
            dict[key]['items'] = []
    cycle += 1

# Figure out which monkeys to chase by counting how many items they inspect over 20 rounds.
#  What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
counter_ls = [dict[x]['counter'] for x in dict]
counter_ls.sort(reverse=True)
# -- Part 1 response --
print(f"The level of monkey business after 20 rounds is {counter_ls[0] * counter_ls[1]}")
# The level of monkey business after 20 rounds is 78960

# --- Part Two ---

# Function to get primer numbers:
# https://stackoverflow.com/questions/16996217/prime-factorization-list
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

# re-parse the data
dict = {}
with open('data-day-11.txt') as f:
    for line in f:
        line = line.strip()
        if "Monkey" in line:
            monk = line.split()[1][0]
            if not monk in dict:
                dict[f"monkey {monk}"] = {}
                dict[f"monkey {monk}"]["counter"] = 0
        if "Starting" in line:
            # split line to get worry numbers
            dict[f"monkey {monk}"]["items"] = [int(x) for x in line.split(": ")[1].split(", ")]
        if "Operation" in line:        
            dict[f"monkey {monk}"]["operation"] = line.split(": ")[1].split("=")[1].strip()
        if "Test" in line:        
            dict[f"monkey {monk}"]["test"] = int(line.split(" ")[-1])
        if "true" in line:        
            dict[f"monkey {monk}"]["true"] = line.split(": ")[1].split()[3]
        if "false" in line:        
            dict[f"monkey {monk}"]["false"] = line.split(": ")[1].split()[3]

# Run 10k cycles and keep track of how many items each monkey looks at
cycle = 0
supermod = math.prod([dict[x]['test'] for x in dict])
while cycle < 10000:
    print(f"cycle: {cycle}")
    for key in dict:
        if len(dict[key]["items"]) > 0:
            for old in dict[key]["items"]:
                # operation - different one for each monkey
                mod = eval(dict[key]['operation'])
                mod = mod % supermod
                # test
                if mod % dict[key]['test'] == 0:
                    m = f"monkey {dict[key]['true']}"
                else:
                    m = f"monkey {dict[key]['false']}"
                # pass to other monkey
                dict[m]['items'].append(mod)
                # add counter
                dict[key]['counter'] += 1
            # Remove from item list
            dict[key]['items'] = []
    cycle += 1

# Figure out which monkeys to chase by counting how many items they inspect over 20 rounds.
#  What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
counter_ls = [dict[x]['counter'] for x in dict]
counter_ls.sort(reverse=True)
# -- Part 1 response --
print(f"The level of monkey business after 10000 rounds is {counter_ls[0] * counter_ls[1]}")
# The level of monkey business after 10000 rounds is 78960
