while True:
    n=int(input(">"))
    for k in range(n-1):

        for j in range(n):
            
            for m in range(2):
                print(" "*n*(n-1-k-m),end="")
                for i in range(k+1):
                    if j==0 or j==n-1:
                        print(" "*(n-1-j)+str(j+1)*(2*j+1)+" "*(n-1-j),end=" ")
                    else:
                        print(" "*(n-1-j)+str(j+1)+" "*(2*j-1)+str(j+1)+" "*(n-1-j),end=" ")
                print(" "*n*(n-2-k),end=" ")
            print()
    for j in range(n):

        for i in range(2*n-1):
            if j==0 or j==n-1:
                print(" "*(n-1-j)+str(j+1)*(2*j+1)+" "*(n-1-j),end=" ")
            else:
                print(" "*(n-1-j)+str(j+1)+" "*(2*j-1)+str(j+1)+" "*(n-1-j),end=" ")
        print()
    for j in range(n-2,-1,-1):

        for i in range(2*n-1):
            if j==0 or j==n-1:
                print(" "*(n-1-j)+str(j+1)*(2*j+1)+" "*(n-1-j),end=" ")
            else:
                print(" "*(n-1-j)+str(j+1)+" "*(2*j-1)+str(j+1)+" "*(n-1-j),end=" ")
        print()
    for k in range(n-2,-1,-1):

            for j in range(n-1,-1,-1):
            
                for m in range(2):
                    print(" "*n*(n-1-k-m),end="")
                    for i in range(k+1):
                        if j==0 or j==n-1:
                            print(" "*(n-1-j)+str(j+1)*(2*j+1)+" "*(n-1-j),end=" ")
                        else:
                            print(" "*(n-1-j)+str(j+1)+" "*(2*j-1)+str(j+1)+" "*(n-1-j),end=" ")
                    print(" "*n*(n-2-k),end=" ")
                print()
