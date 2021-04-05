n=int(input(">"))

print(str(1)+" "*(2*n-3)+str((2*n-1)%10)+" "*(2*n-3)+str((4*n-3)%10))

for j in range(n-2):
    print(" "*(j+1)+str(2+j)+" "*(2*n-5-2*j)+str((2*n-2-j)%10)+" "*(1+2*j)+str((2*n+j)%10)+" "*(2*n-5-2*j)+str((4*n-4)%10))

print(" "*(n-1)+str(n)+" "*(2*n-3)+str((3*n-2)%10))
