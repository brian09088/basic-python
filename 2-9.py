n=int(input(">"))

for j in range(-n+1,n):

    for i in range(-n+1,n):

        print(str(n-max(abs(i),abs(j))),end="")
    print()
