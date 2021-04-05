n=int(input(">"))
m=1
for k in range(3):
    for i in range(k+1):
        print(str(m+i)*(2*n-1),end=" ")
    print()

    for j in range(n-2):

        for i in range(k+1):
            print(str(m+i)+" "*(2*n-3)+str(m+i),end=" ")
        print()

    for i in range(k+1):
        print(str(m+i)*(2*n-1),end=" ")
    print()
    print()
    m+=k+1
