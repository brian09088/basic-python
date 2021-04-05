n=int(input(">"))
m=(3*n+1)//2

for j in range(2*n):

    for i in range(3):

        if i==0:
            if j<n:
                print(" "*2*n,end="")
            else:
                print(" "*(n-1-(j-n))+"/"+"_"*2*(j-n)+"\\"+" "*(n-1-(j-n)),end="")
        elif i==1:
            print(" "*(2*n-1-j)+"/"+"_"*2*j+"\\"+" "*(2*n-1-j),end="")
        else:
            if j<2*n-m:
                print(" "*2*m,end="")
            else:
                print(" "*(m-1-(j-2*n+m))+"/"+"_"*2*(j-2*n+m)+"\\"+" "*(m-1-(j-2*n+m)),end="")
    print()
        
