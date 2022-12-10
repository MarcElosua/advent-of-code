# Read day 10 input
# Data downloaded from https://adventofcode.com/2022/day/10/input

# Start by figuring out the signal being sent by the CPU. The CPU has a single register, X, which starts with the value 1.
#  It supports only two instructions:
#  -  *addx* V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
#  -  *takes* one cycle to complete. It has no other effect.

# Maybe you can learn something by looking at the value of the X register throughout execution.
#  For now, consider the signal strength (the cycle number multiplied by the value of the X register) during the 20th cycle and every 40 cycles after that
#  (that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles).

# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?
cycle = 0
x = 1
strength = []
i = 1
with open('data-day-10.txt') as f:
    for line in f:
        # print(i)
        # i += 1
        line = line.rstrip()
        if "noop" in line:
            cycle += 1
            print(cycle)
            if cycle in [20, 60, 100, 140, 180, 220]:
                print("here1")
                print(f"cycle:{cycle} X:{x}")
                strength.append(cycle * x)
        elif "addx" in line:
            addx = int(line.split()[1])
            n = 2
            while n > 0:
                cycle += 1
                print(cycle)
                if cycle in [20, 60, 100, 140, 180, 220]:
                    print("here2")
                    print(f"cycle:{cycle} X:{x}")
                    strength.append(cycle * x)
                # if n == 1:
                    # x += addx
                n -= 1
            x += addx

# Part 1
print(f"The sum of the signal strengths is {sum(strength)}")
# The sum of the signal strengths is 14420

# --- Part Two ---
# Cycle   1 -> ######################################## <- Cycle  40
# Cycle  41 -> ######################################## <- Cycle  80
# Cycle  81 -> ######################################## <- Cycle 120
# Cycle 121 -> ######################################## <- Cycle 160
# Cycle 161 -> ######################################## <- Cycle 200
# Cycle 201 -> ######################################## <- Cycle 240
cycle = -1
x = 1
crt = ""
# line = "addx 5"
with open('data-day-10.txt') as f:
    for line in f:
        i += 1
        print(i)
        line = line.rstrip()
        if "noop" in line:
            cycle += 1
            print(f"cycle: {cycle}, x = {x}")
            if cycle in [x-1, x, x+1]:
                t = "#"
            else:
                t = "."
            crt = crt + t
            if cycle in [39, 79, 119, 159, 199, 239]:
                crt = crt + "\n"
                cycle -= 40
        elif "addx" in line:
            addx = int(line.split()[1])
            n = 2
            while n > 0:
                cycle += 1
                print(f"cycle: {cycle}, x = {x}")
                if cycle in [x-1, x, x+1]:
                    t = "#"
                else:
                    t = "."
                crt = crt + t
                if cycle in [39, 79, 119, 159, 199, 239]:
                    crt = crt + "\n"
                    cycle -= 40
                n -= 1
            x += addx
        print(x)

print(crt)
