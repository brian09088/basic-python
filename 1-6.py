n=int(input(">"))
for i in range(n):
    print(str((i+1)%10),end="")
print()
for j in range(n-2):
    print(str((4*(n-1)-j)%10)+" "*(n-2)+str((n+1+j)%10))
for i in range(n):
    print(str((4*(n-1)-(n-2)-i)%10),end="")
print()
