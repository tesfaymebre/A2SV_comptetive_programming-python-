n = 5
space = 3
for i in range(4):
    for j in range(space):
        print(" ",end="")
    space-=1
    for k in range(2*i + 1):
        print("*",end="")
    print()
