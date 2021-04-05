hh,vv=chr(9472),chr(9474)
nw,ne,sw,se=chr(9484),chr(9488),chr(9492),chr(9496)
n=int(input(">"))
for j in range(n):

    for k in range(2):

        for i in range(n+1-k):

            if i==j and j<=(n+1)/2-1-k:
                print(nw,end="")
            elif i+j==n-k and j<=(n+1)/2-1-k:
                print(ne,end="")
            elif i+j==n-1-k and j>(n+1)/2-1-k:
                print(sw,end="")
            elif i==j and j>(n+1)/2-1-k:
                print(se,end="")
            elif (i>j and i+j<n-k and j<=(n+1)/2-1-k) or (i+j>n-1-k and i<j and j>(n+1)/2-1-k):
                print(hh,end="")
            elif i==n and j==n-1:
                print(sw,end="")
            else:
                print(vv,end="")
    print()
    
