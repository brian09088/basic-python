
hh=chr(9472)
vv=chr(9474)
nw=chr(9484)
ne=chr(9488)
sw=chr(9492)
se=chr(9496)
n=int(input('n='))
for y in range(n-1,-1,-1):
    for x in range(n+1):
        if x==0 and y==n-1:
            print(nw,end='')
        elif x!=0 and y==n-1:
            print(hh,end='')
        elif x==0 and y!=0:
            print(vv,end='') 
        elif x==0 and y==0:
            print(sw,end='')
        elif y==0 and x!=n:
            print(hh,end='')
        elif y==0 and x==n:
            print(se,end='')
        elif y==(n-2) and x==n:
            print(ne,end='')    
        elif y<=(n-3) and x==n:
            print(vv,end='') 
        elif y==n-2 and x>=2:
            print(hh,end='')
        elif x==1 and y==n-2:
            print(nw,end='')
        elif x==1 and 2<=y<n-2:    
            print(vv,end='')
        elif x==1 and y==1:
            print(sw,end='')
        elif y==1 and 2<=x<=n-2:
            print(hh,end='')
        elif x==n-1 and y==1:
            print(se,end='')
        elif x==n-1 and 1<y<n-3:
            print(vv,end='')
        elif x==n-1 and y==n-3:
            print(ne ,end='')
        elif 2<x<n-1 and y==n-3:
            print(hh,end='')
        elif x==2 and y==n-3:
            print(nw,end='')
        elif x==2 and y==2:
            print(sw,end='') 
        elif 2<x<n-2 and y==2:    
            print(hh,end='')
        elif x==n-2 and y==2:
            print(se,end='')
        else:
            print(' ',end='')
    print()       



    
