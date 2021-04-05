while True:
    n=int(input(">"))
    for j in range(n):

        for i in range(2*n-1):
            p=abs(n-1-i)
            if j>=p:
                print("|"*(n-j-1)+"/"+" "*2*(j-p)+"\\"+"|"*(n-j-1),end="")
            else:
                print("|"*2*(n-p),end="")
        print()
    for j in range(n-1,-1,-1):

        for i in range(2*n-1):
            p=abs(n-1-i)
            if j>=p:
                print("|"*(n-j-1)+"\\"+" "*2*(j-p)+"/"+"|"*(n-j-1),end="")
            else:
                print("|"*2*(n-p),end="")
        print()
