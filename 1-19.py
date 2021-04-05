n=int(input(">"))
m=1
for k in range(n):

    for j in range(n):

        for i in range(k+1):
            print(str(m+i)*n,end=" ")
        print()
    m+=k+1
    print()
