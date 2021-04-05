from random import*
while True:
    n=int(input(">"))
    nom=[[None]*2*n for i in range(2*n)]
    for i in range(2):
        p=randint(1,9)
        q=randint(1,9)
        for s in range(n):
            for t in range(2*n):
                if t<n:
                    nom[n*i+s][t]=p
                else:
                    nom[n*i+s][t]=q
    for j in range(2*n):
        for i in range(2*n):
            print(nom[j][i],end="")
        print()
                
