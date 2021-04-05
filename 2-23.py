while True:
    n=int(input(">"))
    for j in range(2*n-1):
        for i in range(2*n-2):
            print("*" if (i==j or i+j==2*n-2) else " ",end="")
        for i in range(n):
            if j<n:
                print("*" if (i==j or i+j==n-1) else " ",end="")
            else:
                print("*" if (i==j-n+1 or i+j-n+1==n-1) else " ",end="")
        for i in range(1,n):
            if j<n:
                print("*" if (i==j or i+j==n-1) else " ",end="")
            else:
                print("*" if (i==j-n+1 or i+j-n+1==n-1) else " ",end="")
        for i in range(1,2*n-1):
            print("*" if (i==j or i+j==2*n-2) else " ",end="")
        print()
