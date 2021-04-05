a=int(input(">"))
b=int(input(">"))

n=len(str(a))
m=len(str(b))
k=max(m,n)
print(" "+"{:>k}".format(a))
print("x"+"{:>k}".format(b))
print("-"*(k+1))

for j in range(m):
    print(

