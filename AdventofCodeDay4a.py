f = open("C:/Data/Inputs/Advent of Code 2022/advent_of_code_day_4_input.txt", "r")

g = f.readlines()

encompassesCount = 0

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

    print(low_set_one, low_set_two, high_set_one, high_set_two)
    if low_set_one >= low_set_two and high_set_one <= high_set_two:
        print("low_set_one >= low_set_two and high_set_one <= high_set_two - contains match")
        encompassesCount = encompassesCount + 1
    elif low_set_two >= low_set_one and high_set_two <= high_set_one:
        print("low_set_two >= low_set_one and high_set_two <= high_set_one - contains match")
        encompassesCount = encompassesCount + 1
print(encompassesCount)

