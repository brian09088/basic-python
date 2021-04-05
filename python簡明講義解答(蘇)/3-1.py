# 3-1 
n=int(input('n='))
for a in range(n):
    for b in range(n):
        print(" "*(n*(n-a-1)),end='')
        for c in range(a+1):
            if b==0 or b==n-1:
                print(" "*(n-b-1)+str(c+1)*(2*b+1)+" "*(n-b-1),end='')
            else:
                print(" "*(n-b-1)+str(c+1)+" "*(n-b-1)+str(c+1)+" "*(n-b-1),end='')
        print() 
        
          


