while True:
    n=int(input(">"))
    for k in range(3):

        for j in range(n):

            for i in range(3):

                if k%2==0 and i%2==0:
                    if j==0 or j==n-1:
                        print(str(3*(k//2)+1+i//2)*n,end="")
                    else:
                        print(str(3*(k//2)+1+i//2)+" "*(n-2)+str(3*(k//2)+1+i//2),end="")
                elif k%2==1 and i%2==1:
                    if j==0 or j==n-1:
                        print(str(3)*n,end="")
                    else:
                        print(str(3)+" "*(n-2)+str(3),end="")
                else:
                    print(" "*n,end="")
            print()
