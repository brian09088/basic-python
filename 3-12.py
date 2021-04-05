while True:
    n=int(input(">"))
    for k in range(n):

        for j in range(3):

            for i in range(n):
                if i==k or i+k==n-1:
                    print(str(n)*3,end="")
                else:
                    print(" "*3,end="")
            print()
