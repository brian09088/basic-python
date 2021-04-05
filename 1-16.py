n=8
for k in range(n//4):

    for j in range(n-5):

        for i in range(n-4):
            print(str(i+4*k+1)*5,end="")
        print(" ")
    print()
