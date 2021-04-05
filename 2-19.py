while True:
    n=int(input(">"))
    for k in range(3):

        for j in range(n):

            for m in range(3):

                for i in range(n):

                    if k==0 and m%2==0:
                        print(str(k+1+(m//2)),end="")
                    elif k==1 and m%2==1:
                        print(str(3),end="")
                    elif k==2 and m%2==0:
                        print(str(k+2+(m//2)),end="")
                    else:
                        print(" ",end="")
            print()
