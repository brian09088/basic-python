while True:
    n=int(input(">"))
    for j in range(2*n-1):

        for i in range(n):
            if i<=j<n+i-1:
                print(str(i+1)+" "*(n-2)+str(i+1),end=" ")
            elif j==n+i-1:
                print(str(i+1)*n,end=" ")
            else:
                print(" "*n,end=" ")
        print()
