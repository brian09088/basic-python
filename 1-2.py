n=int(input(">"))
s=0
for k in range(1,n+2):
    s+=k


for i in range(n,0,-1):
    s-=i+1
    print("sum"+"("+"["+str(1)+","+str(i)+"]"+")"+"=",end="")
    for j in range(1,i+1):
        if j<i:
            print(str(j)+"+",end="")
        else:
            print(str(j)+"="+str(s))
