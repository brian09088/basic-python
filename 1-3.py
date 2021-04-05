n=int(input(">"))

for i in range(n):

    for j in range(n):
        print(str((j+1+n*i)%10),end="")
    print()
