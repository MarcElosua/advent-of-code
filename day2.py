# This strategy guide predicts and recommends the following:

#   In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
#   In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
#   The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

# What would your total score be if everything goes exactly according to your strategy guide?

# Set Guide play
guide_dict = {
    "A": 'Rock',
    "B": 'Paper', 
    "C": 'Scissors', 
    "X": 'Rock', 
    "Y": 'Paper', 
    "Z": 'Scissors'}
scores_dict = {"Rock": 1, "Paper": 2, "Scissors": 3}
win_dict = {"Win": 6, "Draw": 3, "Loss": 0}

# Read day 2 input
# Data downloaded from https://adventofcode.com/2022/day/2/input
score = []
with open('data-day-2.txt') as f:
    for line in f:
        print(line)
        arr = line.split( )
        
        # Get play score
        sc1 = scores_dict[guide_dict[arr[1]]]
        
        # Get W-D-L score
        if arr[0] == "A":
            if arr[1] == "X":
                sc2 = win_dict["Draw"]
            elif arr[1] == "Y":
                sc2 = win_dict["Win"]
            elif arr[1] == "Z":
                sc2 = win_dict["Loss"]
        elif arr[0] == "B":
            if arr[1] == "X":
                sc2 = win_dict["Loss"]
            elif arr[1] == "Y":
                sc2 = win_dict["Draw"]
            elif arr[1] == "Z":
                sc2 = win_dict["Win"]
        elif arr[0] == "C":
            if arr[1] == "X":
                sc2 = win_dict["Win"]
            elif arr[1] == "Y":
                sc2 = win_dict["Loss"]
            elif arr[1] == "Z":
                sc2 = win_dict["Draw"]
        # Sum both scores and append them to score array
        score.append(sc1 + sc2)

# Total score
sum(score)

### --- Part Two ---
# The Elf finishes helping with the tent and sneaks back over to you. 
# "Anyway, the second column says how the round needs to end:
# X means you need to lose,
# Y means you need to end the round in a draw
# Z means you need to win. Good luck!"
guide_dict = {
    "A": 'Rock',
    "B": 'Paper', 
    "C": 'Scissors', 
    "X": 'Loss', 
    "Y": 'Draw', 
    "Z": 'Win'}
scores_dict = {"Rock": 1, "Paper": 2, "Scissors": 3}
win_dict = {"Win": 6, "Draw": 3, "Loss": 0}

score2 = []
with open('data-day-2.txt') as f:
    for line in f:
        print(line)
        arr = line.split( )
        
        # Get play score
        sc1 = win_dict[guide_dict[arr[1]]]
        
        # Get W-D-L score
        if arr[0] == "A":
            if arr[1] == "X":
                sc2 = win_dict["Draw"]
            elif arr[1] == "Y":
                sc2 = win_dict["Win"]
            elif arr[1] == "Z":
                sc2 = win_dict["Loss"]
        elif arr[0] == "B":
            if arr[1] == "X":
                sc2 = win_dict["Loss"]
            elif arr[1] == "Y":
                sc2 = win_dict["Draw"]
            elif arr[1] == "Z":
                sc2 = win_dict["Win"]
        elif arr[0] == "C":
            if arr[1] == "X":
                sc2 = win_dict["Win"]
            elif arr[1] == "Y":
                sc2 = win_dict["Loss"]
            elif arr[1] == "Z":
                sc2 = win_dict["Draw"]
        # Sum both scores and append them to score array
        score2.append(sc1 + sc2)

# Total score
sum(score2)
