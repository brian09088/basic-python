while True:
    n=int(input(">"))
    for j in range(n-1,-1,-1):

        for i in range(2*n-1):
            p=abs((n-1)-i)
            if j<=p:
                print("|"*j+"/"+" "*2*(p-j)+"\\"+"|"*j,end="")
            else:
                print("|"*2*(p+1),end="")
        print()
    for j in range(n):

        for i in range(2*n-1):
            p=abs((n-1)-i)
            if j<=p:
                print("|"*j+"\\"+" "*2*(p-j)+"/"+"|"*j,end="")
            else:
                print("|"*2*(p+1),end="")
        print()
