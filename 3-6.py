while True:
    n=int(input(">"))
    for k in range(n):
        
        for j in range(3):
            
            for m in range(2*n-1):
                p=m if m<n else (n-abs(m-n+1)-1)
                if n-1-p<=k:
                    print(" "*(3*(n-1-k)),end="")
                    for i in range(p+k-n+2):
                        print(str(p+k-n+2)*5,end=" ")
                    print(" "*(3*(n-1-k)),end="")
                    
                else:
                    print(" "*(5*(p+1)+p),end=" ")
            print()
    for k in range(n-2,-1,-1):
        
        for j in range(3):
            
            for m in range(2*n-1):
                p=m if m<n else (n-abs(m-n+1)-1)
                if n-1-p<=k:
                    print(" "*(3*(n-1-k)),end="")
                    for i in range(p+k-n+2):
                        print(str(p+k-n+2)*5,end=" ")
                    print(" "*(3*(n-1-k)),end="")
                    
                else:
                    print(" "*(5*(p+1)+p),end=" ")
            print()
