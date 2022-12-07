f = open("C:/Data/Inputs/Advent of Code 2022/advent_of_code_day_1_input.txt", "r")
#print(f.read())

g = f.readlines()

arrayofelves = []
values = 0

for line in g:

    elf = line.strip()
    if elf == "":
        print("Null value found")
        arrayofelves.append(values)
        values = 0
    else:
        values = values + int(elf)
print(max(arrayofelves))

print(arrayofelves)

#for index, line in enumerate(g):
#    print("Line {}: {}".format(index, line.strip()))
