n=int(input(">"))

for j in range(n):

    for i in range(n):
        print(" "*(n-1-j)+str(j+1)*(2*j+1)+" "*(n-1-j),end=" ")
    print()
