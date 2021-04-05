while True:
    n=int(input(">"))
    for k in range(n-1):

        for j in range(n):

            for m in range(2):
                if m==0:
                    print(" "*n*(n-1-k),end="")
                else:
                    print(" "*n*(n-2-k),end="")
                for i in range(k+1):
                        print(" "*(n-1-j)+str(j+1)*(2*j+1)+" "*(n-1-j),end=" ")
                if m==1:
                    print(" "*n*(n-1-k),end="")
                else:
                    print(" "*n*(n-2-k),end="")
            print()
                    
    for j in range(n):
        for i in range(2*n-1):
            print(" "*(n-1-j)+str(j+1)*(2*j+1)+" "*(n-1-j),end=" ")
        print()
