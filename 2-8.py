n = int(input(">"))

for j in range(2*n):

    if j<n:
        print("*"*n+"-"*2*n)
    else:
        print("+"*n+"-"*2*n)
