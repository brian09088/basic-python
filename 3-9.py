while True:
    n=int(input(">"))
    for j in range(n):

        for i in range(2*n-1):
            p=i if i<n else 2*n-2-i
            if j>=n-1-p and i%2==0:
                print(" "*(n-1-j)+"/"+"|"*2*(p-n+j+1)+"\\"+" "*(n-1-j),end="")
            else:
                print(" "*(2*(p+1)),end="")
        print()
    for j in range(n-1,-1,-1):

        for i in range(2*n-1):
            p=i if i<n else 2*n-2-i
            if j>=n-1-p and i%2==1:
                print(" "*(n-1-j)+"\\"+"|"*2*(p-n+j+1)+"/"+" "*(n-1-j),end="")
            else:
                print(" "*(2*(p+1)),end="")
        print()
