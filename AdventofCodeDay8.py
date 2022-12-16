import numpy as np

f = open("AdventofCodeDay8.txt", "r")

g = f.read().splitlines()

#print(g[0])

mat = np.array(g)
print(mat)

matrix_length = len(mat)

print(matrix_length)

# 99 x 99 = 9801

x = 0
y = 0

for tree in mat: #gets active value
    while x < 99:
        while y < 99:
            #print(mat[x][y])
            y += 1
            #print(x,y)
            if (x != 0 and x != 99) and (y != 0 and y != 99): #only get internal numbers
                #print(x,y)
                # now just have to check this number against all numbers in a row or column adjacent (take x and y values and then iterate up and down to check the numbers
        x += 1
        y = 0

#for tree in :
#    print(tree)

#while i < matrix_length:
#    print(mat[i][i])
#    i += 1
#for i in g:
    #print([i])