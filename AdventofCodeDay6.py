f = open("AdventofCodeDay6.txt", "r")

g = f.readlines()

fullString = g[0]

codeString = []
j = 0

print("Input length of string to search for:")
stringDetectorLength = input()

for i in fullString:
    j += 1
    codeString.append(i)
    #print(codeString)
    if len(codeString) > int(stringDetectorLength):
        codeString.pop(0)
    if len(set(codeString)) == int(stringDetectorLength):
        print(codeString)
        print("Characters: " + str(j))
        break
