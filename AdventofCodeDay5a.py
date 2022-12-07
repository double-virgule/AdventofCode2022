f = open("./AdventofCodeDay5.txt", "r")

g = f.readlines()

crates = [g[0].strip(),
          g[1].strip(),
          g[2].strip(),
          g[3].strip(),
          g[4].strip(),
          g[5].strip(),
          g[6].strip(),
          g[7].strip(),
          g[8].strip()]

#print(crates[0][1])

i = 0

for line in g:
    if i >= 10:
        instruction = line.strip()
        instNumOnly = [int(inst) for inst in instruction.split() if inst.isdigit()] #numbers split into a list
        print(instNumOnly[0])
        for cratesToMove in instNumOnly:
            print(cratesToMove)
        #crates.remove(instNumOnly[0])
        #print(crates)

    i = i + 1

#for line in g:
    #print(line.strip())
