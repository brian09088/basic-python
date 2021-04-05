n=int(input(">"))

for j in range(n):

    for k in range(n):

        print(" "*(n-1-j),end="")

        for i in range(j+1):
            print("/"+"\\",end="")

        print(" "*(n-1-j),end="")
    print()

print("-"*(n*n*2))

for j in range(n-1,-1,-1):

    for k in range(n):

        print(" "*(n-1-j),end="")

        for i in range(j+1):
            print("\\"+"/",end="")

        print(" "*(n-1-j),end="")
    print()
