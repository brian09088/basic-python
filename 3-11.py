while True:
    n=int(input(">"))
    for j in range(n-1,-1,-1):

        for i in range(2*n-1):
            p=i if i<n else 2*n-i-2
            if j==p:
                print(str(p+1)*(p+1),end="")
            elif j<p:
                print("-"*(p+1),end="")
            else:
                print(" "*(p+1),end="")
        print()
    for j in range(n):

        for i in range(2*n-1):
            p=i if i<n else 2*n-i-2
            if j==p:
                print(str(p+1)*(p+1),end="")
            elif j<p:
                print("-"*(p+1),end="")
            else:
                print(" "*(p+1),end="")
        print()
