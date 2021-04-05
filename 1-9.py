n=int(input(">"))
for i in range(n):
    for j in range(n):
        if i+j<=n-1:
            print(str(i+j+1),end="")
        else:
            print(str(i+j-(n-1)),end="")
    print()
