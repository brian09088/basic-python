n=int(input(">"))
for i in range(n):
    print(" "*(n-1)+str(1)+" "*(n-1),end=" ")
print()
for j in range(n-2):

    for i in range(n):

        print(" "*(n-2-j)+str(2+j)+" "*(2*j+1)+str(2+j)+" "*(n-2-j),end=" ")
    print()

for i in range(n):
    print(str(n)*(1+2*(n-1)),end=" ")
