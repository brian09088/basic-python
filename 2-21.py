while True:
    n=int(input(">"))

    for k in range(3):

        for j in range(n):

            for m in range(3):

                for i in range(n):
                    if k==m or k+m==2:
                        if i==j and i+j==n-1:
                            print("X",end="")
                        elif i==j:
                            print("\\",end="")
                        elif i+j==n-1:
                            print("/",end="")
                        else:
                            print(" ",end="")
                    else:
                        print(" ",end="")
            print()
                        
