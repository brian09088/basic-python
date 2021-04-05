n=int(input(">"))

for i in range(1,n+1):
    print(str(i)+"!"+"=",end="")
    m=1
    for j in range(1,i+1):
        m*=j
        if j<i:
            print(str(j)+"x",end="")
        else:
            print(str(j)+"="+str(m),end="")
    print()
        
