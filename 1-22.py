n=int(input(">"))

print(str(1)+"-"*(4*n-5)+str(2)+"-"*(4*n-5)+str(3))

for j in range(n-2):
    print(" "*(2*j+2)+str((4+4*j)%10)+"-"*(4*n-5-4*(j+1))+str((5+4*j)%10)+" "*(3+4*j)+str((6+4*j)%10)+"-"*(4*n-5-4*(j+1))+str((7+4*j)%10))

print(" "*(2*(n-1))+str((4+4*(n-2))%10)+" "*(3+4*(n-2))+str((5+4*(n-2))%10))