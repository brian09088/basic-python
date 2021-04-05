n=int(input(">"))

for m in range(n-1):

    for j in range(n):

        print(" "*(n*m)+str(m+1)*n+" "*n*(n*2-3-2*m)+str(m+1)*n)

for j in range(n):
    print(" "*n*(n-1)+str(n)*n)
