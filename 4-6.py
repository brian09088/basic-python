while True:
    n=int(input(">"))
    nos=[[None]*(i+1) for i in range(n)]
    s,t=0,0
    k=0
    q=n*(n+1)//2
    for i in range(q):
        nos[s][t]=i+1
        if t==k:
            s+=1
            if s%2==0:
                k=0
                t=s
            else:
                k=s
                t=0
        else:
            if s%2==0:
                t-=1
            else:
                t+=1
        
    for j in range(n):
        for i in range(n):
            if j>=i:
                print(nos[j][j-i],end=" ")
            else:
                print(" ",end=" ")
        print()
                
                
