n=int(input(">"))

for i in range(n):
    print(str((i+1)%10),end="")
print()
for j in range(n-2):
    print(str((n+1+j*2)%10)+" "*(n-2)+str((n+2+j*2)%10))
for i in range(n):
    print(str((n+2*(n-2)+i+1)%10),end="")
print()
    
