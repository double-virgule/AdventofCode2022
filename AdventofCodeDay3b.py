## Lowercase item types a through z have priorities 1 through 26.
## Uppercase item types A through Z have priorities 27 through 52.


f = open("C:/Data/Inputs/Advent of Code 2022/advent_of_code_day_3_input.txt", "r")
#print(f.read())

g = f.readlines()

totalPriority = 0

i = 0
j = 1
k = 2

for line in g:
    if (i != 300):
        print(i, j, k)
        threeElves = [g[i].strip(), g[j].strip(), g[k].strip()]
        print(threeElves)

        i = i + 3
        j = j + 3
        k = k + 3
        common_character = ''.join(
            set(threeElves[0]).intersection(threeElves[1]).intersection(threeElves[2]))
        print(common_character)
    # print(rucksack_comp_1)
    # print(rucksack_comp_2)
# )
    #
        letterPriorityNumber = ord(common_character)

        if (letterPriorityNumber >= 97):
            actualPriority = letterPriorityNumber - 96
        if (letterPriorityNumber <= 90):
            actualPriority = letterPriorityNumber - 38
        print(actualPriority)
        print(common_character)
        totalPriority = actualPriority + totalPriority
        print(totalPriority)

        # - 96 - 38
        # a = 97 z = 122 A = 65 Z = 90