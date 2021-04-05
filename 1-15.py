n=int(input(">"))

for j in range(n):

    for i in range(n):

        print(str(2*i+1)*(n-j)+"/"+str(2*i+2)*(j+1),end=" ")
    print()
