n=int(input(">"))

for j in range(n):

    for i in range(n):

        if i>j:
            print(" "*n,end=" ")
        else:
            print(str(i+1)*n,end=" ")
    print()
