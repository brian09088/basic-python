n=int(input(">"))

for j in range(-n+1,n):

    for i in range(-n+1,n):

        if abs(i)+abs(j)>=n:
            print(" ",end="")

        else:
            print(str(n-max(abs(i),abs(j))),end="")
    print()
