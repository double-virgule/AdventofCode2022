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

#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

def RockPaperScissors(value1, value2):
    if (value1 == "scissors" and value2 == "lose"):
        #print("He plays scissors, I play paper.")
        myThrow = "paper"
        outcome = "lose"
    if (value1 == "paper" and value2 == "lose"):
        #print("He plays paper, I play rock.")
        myThrow = "rock"
        outcome = "lose"
    if (value1 == "rock" and value2 == "lose"):
        #print("He plays rock, I play scissors.")
        myThrow = "scissors"
        outcome = "lose"
####
    if (value1 == "scissors" and value2 == "draw"):
        #print("He plays scissors, I play scissors.")
        myThrow = "scissors"
        outcome = "draw"
    if (value1 == "paper" and value2 == "draw"):
        #print("He plays paper, I play paper.")
        myThrow = "paper"
        outcome = "draw"
    if (value1 == "rock" and value2 == "draw"):
        #print("He plays rock, I play rock.")
        myThrow = "rock"
        outcome = "draw"
####
    if (value1 == "scissors" and value2 == "win"):
        #print("He plays scissors, I play rock.")
        myThrow = "rock"
        outcome = "win"
    if (value1 == "paper" and value2 == "win"):
        #print("He plays paper, I play scissors.")
        myThrow = "scissors"
        outcome = "win"
    if (value1 == "rock" and value2 == "win"):
        #print("He plays rock, I play paper.")
        myThrow = "paper"
        outcome = "win"
    if (myThrow == "rock"):
        myPoints = 1
    if (myThrow == "paper"):
        myPoints = 2
    if (myThrow == "scissors"):
        myPoints = 3
    if (outcome == "win"):
        myPoints = myPoints + 6
    if (outcome == "draw"):
        myPoints = myPoints + 3
    if (outcome == "lose"):
        myPoints = myPoints + 0
    print("Results: " + outcome + " I played " + myThrow + " versus their " + value1 + ", because I was supposed to " + value2 + ".")
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
        my_move = "lose"
    if (i[2] == "Y"):
        my_move = "draw"
    if (i[2] == "Z"):
        my_move = "win"

    #print(their_move, my_move)

    totalPoints = RockPaperScissors(their_move, my_move) + totalPoints

print(totalPoints)

