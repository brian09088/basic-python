while True:
    n=int(input(">"))
    for k in range(n):

        for j in range(3):
            p=1
            for m in range(n):
                
                if k+m>=n-1:
                    print(" "*3*(n-k-1),end="")
                    for i in range(m-n+k+2):
                        print(str(p)*5,end=" ")
                    print(" "*3*(n-k-1),end="")
                    p+=1
                else:
                    print(" "*(5*(m+1)+m),end=" ")
                
            print()
