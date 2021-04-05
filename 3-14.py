while True:
    n=int(input(">"))
    for k in range(5):

        for j in range(5):

            for m in range(n):

                for i in range(n):
                    if (k==0 or k==2 or k==4 or (k==1 and m==n-1) or (k==3 and m==0)) and (j==0 or j==2 or j==4 or (j==1 and i==n-1) or (j==3 and i==0)):
                        print("2",end="")
                    else:
                        print(" ",end="")
                print(" ",end="")
            print()
