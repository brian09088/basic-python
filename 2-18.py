while True:
    n=int(input(">"))
    hh,vv=chr(9472),chr(9474)
    nw,ne,sw,se=chr(9484),chr(9488),chr(9492),chr(9496)
    for j in range(n):

        for i in range(n):

            if j==0:
                print(" "*2*(n-1)+nw+hh*2+ne+" "*2*(n-1),end=" ")
            else:
                print(" "*2*(n-1-j)+nw+hh+se+" "*2*(2*j-1)+sw+hh+ne+" "*2*(n-1-j),end=" ")
        print()
    for i in range(n):
        print(vv+" "*2*(2*n-1)+vv,end=" ")
    print()
    for j in range(n-1,-1,-1):

        for i in range(n):

            if j==0:
                print(" "*2*(n-1)+sw+hh*2+se+" "*2*(n-1),end=" ")
            else:
                print(" "*2*(n-1-j)+sw+hh+ne+" "*2*(2*j-1)+nw+hh+se+" "*2*(n-1-j),end=" ")
        print()
