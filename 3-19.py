while True:
    n=int(input(">"))
    for k in range(n):

        for j in range(2):

            for m in range(2):

                for i in range(m,2*n-1):
                    if (k>=i and i<n) or (k+i>=2*n-2 and i>=n):
                        if j==1:
                            print("/"+"|"+"\\",end=" ")
                        else:
                            print("\\"+"|"+"/",end=" ")
                    else:
                        print(" "*3,end=" ")
            print()
    for k in range(n-2,-1,-1):

        for j in range(2):

            for m in range(2):

                for i in range(m,2*n-1):
                    if (k>=i and i<n) or (k+i>=2*n-2 and i>=n):
                        if j==1:
                            print("/"+"|"+"\\",end=" ")
                        else:
                            print("\\"+"|"+"/",end=" ")
                    else:
                        print(" "*3,end=" ")
            print()
