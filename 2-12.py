n=int(input(">"))

for j in range(2*n-1):

    for i in range(3):

        if  i==1:
            print(" "*(2*n-1-j)+"/"+"_"*2*j+"\\"+" "*(2*n-1-j),end="")
        elif j<n :
            print(" "*2*n,end="")
        else:
            print(" "*(n-1-j+n)+"/"+"_"*2*(j-n)+"\\"+" "*(2*n-1-j),end="")
    print()
print("/"+"_"*2*(n-1)+"\\"+"/"+"_"*2*(2*n-1)+"\\"+"/"+"_"*2*(n-1)+"\\")
