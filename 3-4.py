while True :
    n=int(input(">"))
    for k in range(n):

        for j in range(n):
            print(" "*n*(n-1-k),end="")
            for i in range(k+1):
                if i==0 or i==k:
                    if j==0 or j==n-1:
                        print(" "*(n-1-j)+str(j+1)*(2*j+1)+" "*(n-1-j),end=" ")
                    else:
                        print(" "*(n-1-j)+str(j+1)+" "*(2*j-1)+str(j+1)+" "*(n-1-j),end=" ")
                else:
                    print(" "*(2*n-1),end=" ")
            print()
    for k in range(n-1,-1,-1):
        if k==n-1:
            for j in range(n-2,-1,-1):
                print(" "*n*(n-1-k),end="")
                for i in range(k+1):
                    if i==0 or i==k:
                        if j==0 or j==n-1:
                            print(" "*(n-1-j)+str(j+1)*(2*j+1)+" "*(n-1-j),end=" ")
                        else:
                            print(" "*(n-1-j)+str(j+1)+" "*(2*j-1)+str(j+1)+" "*(n-1-j),end=" ")
                    else:
                        print(" "*(2*n-1),end=" ")
                print()
        else:
            for j in range(n-1,-1,-1):
                print(" "*n*(n-1-k),end="")
                for i in range(k+1):
                    if i==0 or i==k:
                        if j==0 or j==n-1:
                            print(" "*(n-1-j)+str(j+1)*(2*j+1)+" "*(n-1-j),end=" ")
                        else:
                            print(" "*(n-1-j)+str(j+1)+" "*(2*j-1)+str(j+1)+" "*(n-1-j),end=" ")
                    else:
                        print(" "*(2*n-1),end=" ")
                print()   
