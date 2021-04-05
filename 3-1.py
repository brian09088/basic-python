while True:
    n=int(input(">"))
    for k in range(n):

        for j in range(n):
            print(" "*n*(n-1-k),end="")

            for i in range(k+1):
                if j==0 or j==n-1:
                    print(" "*(n-1-j)+str(i+1)*(2*j+1)+" "*(n-1-j),end=" ")
                else:
                    print(" "*(n-1-j)+str(i+1)+" "*(2*j-1)+str(i+1)+" "*(n-1-j),end=" ")
            print()
