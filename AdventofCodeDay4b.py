f = open("C:/Data/Inputs/Advent of Code 2022/advent_of_code_day_4_input.txt", "r")

g = f.readlines()

matches = 0

for line in g:
    groupPair = line.strip()
    #print(groupPair)
    splitPairs = groupPair.split(",")
    #print(splitPairs[0])
    #print(splitPairs[1])

    numberSet1 = splitPairs[0].split("-")
    numberSet2 = splitPairs[1].split("-")
    #print(str(numberSet1) + " " + str(numberSet2))

    low_set_one = int(numberSet1[0])
    low_set_two = int(numberSet2[0])
    high_set_one = int(numberSet1[1])
    high_set_two = int(numberSet2[1])

    if(low_set_one == high_set_one):
        allLow = [low_set_one]
    else:
        print(low_set_one, high_set_one)
        allLow = list(range(low_set_one, high_set_one+1))
    if(low_set_two == high_set_two):
        allHigh = [low_set_two]
    else:
        print(low_set_two, high_set_two)
        allHigh = list(range(low_set_two, high_set_two+1))

    print(allLow)
    print(allHigh)
    if(set(allLow).intersection(allHigh)):
        print("Set found.")
        matches = matches + 1
print(matches)
