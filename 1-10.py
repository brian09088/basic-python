n=int(input(">"))
for j in range(n):
    print("|",end="")
    for k in range(n):

        for i in range(n):
            if (j+i+k+1)%n==0:
                print(str(n),end="")
            else:
                print(str((j+i+k+1)%n),end="")
        print("|",end="")
    print()
            
