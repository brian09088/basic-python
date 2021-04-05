n=int(input(">"))

for j in range(n-1):
    print(" "*(2*j)+str((1+2*j)%10)+"-"*(4*n-5-4*j)+str((2+2*j)%10))
print(" "*2*(n-1)+str((2*n-1)%10))
