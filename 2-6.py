n=int(input(">"))

print("*"+" "*(2*n-3)+"*"+" "*(2*n-3)+"*")

for j in range(n-2):
    print(" "*(j+1)+"*"+" "*(2*n-5-2*j)+"*"+" "*(1+2*j)+"*"+" "*(2*n-5-2*j)+"*")

print(" "*(n-1)+"*"+" "*(2*n-3)+"*")
