while True:
    n=int(input(">"))
    for k in range(7):

        for j in range(n):

            for m in range(5):

                for i in range(n):
                    if (k==2 or k==4) or m==2 or (k==3 and(m==0 or m==4)):
                        print("中",end="")
                    else:
                        print("  ",end="")
            print()
