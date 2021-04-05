while True:
    n=int(input(">"))
    nom=[[None]*i for i in range(n,0,-1)]
    s,t=0,0
    k=n-1
    q=n*(n+1)//2
    for i in range(q):
        nom[s][t]=i+1
        if t==k:
            s+=1
            t=0
            k-=1
        else:
            t+=1
    for j in range(n):
        for i in range(n):
            if j>=i:
                print(nom[i][j-i],end=" ")
            else:
                print(" ",end=" ")
        print()
