n=int(input(">"))

for j in range(n-1):

    for i in range(n):

        print(" "*(n-1-j)+"/"+"|"*2*j+"\\"+" "*(n-2-j),end="")
    print()

for i in range(n):
    print("x"+"|"*2*(n-1),end="")
print("X")

for j in range(n-2,-1,-1):

    for i in range(n):

        print(" "*(n-1-j)+"\\"+"|"*2*j+"/"+" "*(n-2-j),end="")
    print()
