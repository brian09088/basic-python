n=int(input(">"))

for j in range(n):

    for i in range(n):
        print(" "*j+"\\"+" "*2*(n-1-j)+"/"+" "*j,end="")
    print()
for j in range(n-1,-1,-1):

    for i in range(n):
        print(" "*j+"/"+" "*2*(n-1-j)+"\\"+" "*j,end="")
    print()
