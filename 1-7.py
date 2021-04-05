n=int(input(">"))
k=1
for j in range(n):
    print(" "*(n-1-j),end="")
    for i in range(j+1):
        print(str((k+i)%10),end="")
    k+=j+1
    print()
