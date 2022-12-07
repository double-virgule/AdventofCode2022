# The winner of the whole tournament is the player with the highest score.
# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

# A = Rock
# B = Paper
# C = Scissors
# X = Rock
# Y = Paper
# Z = Scissors


def RockPaperScissors(value1, value2):
    if (value2 == "rock"):
        myPoints = 1
    if (value2 == "paper"):
        myPoints = 2
    if (value2 == "scissors"):
        myPoints = 3
    if (value1 == value2):
        myPoints = 3 + myPoints
        print("Tie!")
    if ((value1 == "scissors" and value2 == "rock") or (value1 == "paper" and value2 == "scissors") or (value1 == "rock" and value2 == "paper")):
        myPoints = myPoints + 6
    return myPoints

with open('C:/Data/Inputs/Advent of Code 2022/advent_of_code_day_2_input.txt') as f:
    game_outcomes = list(filter(None, f.read().split('\n')))

myPoints = 0
totalPoints = 0

for i in game_outcomes:
    #print(i[0], i[2])
    if (i[0] == "A"):
        their_move = "rock"
    if (i[0] == "B"):
        their_move = "paper"
    if (i[0] == "C"):
        their_move = "scissors"
    if (i[2] == "X"):
        my_move = "rock"
    if (i[2] == "Y"):
        my_move = "paper"
    if (i[2] == "Z"):
        my_move = "scissors"

    print(their_move, my_move)

    totalPoints = RockPaperScissors(their_move, my_move) + totalPoints

print(totalPoints)

