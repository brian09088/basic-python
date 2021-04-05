hh,vv=chr(9472),chr(9474)
nw,ne,sw,se=chr(9484),chr(9488),chr(9492),chr(9496)
n=int(input(">"))

for j in range(2*n-1):

    for k in range(n):

        for i in range(n):
            if i==0 and j-k==0:
                print(nw,end="")
            elif i==n-1 and j-k==0:
                print(ne,end="")
            elif i==0 and j-k==n-1:
                print(sw,end="")
            elif i==n-1 and j-k==n-1:
                print(se,end="")
            elif (i==0 or i==n-1) and 0<j-k<n-1:
                print(vv,end="")
            elif 0<=j-k<=n-1 and 0<i<n-1:
                print(hh,end="")
            else:
                print(" ",end="")
    print()
