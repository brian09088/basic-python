from random import*
while True:
    n=int(input(">"))
    nos=[[randint(0,1) for i in range(n)] for i in range(n)]
    nom=[[randint(0,1) for i in range(n)] for i in range(n)]
    now=[[None]*n for i in range(n)]
    for j in range(n):
        for i in range(n):
            if nos[j][i]==1 and nom[j][i]==1:
                now[j][i]=1
            else:
                now[j][i]=2
    for j in range(n):
        for k in range(3):
            for i in range(n):
                if k==0:
                    if j==n-2 and i==n-1:
                        print(nos[j][i],end="X")
                    else:
                        print(nos[j][i],end=" ")
                if k==1:
                    if j==n-2 and i==n-1:
                        print(nom[j][i],end="=")
                    else:
                        print(nom[j][i],end=" ")
                else:
                        print(now[j][i],end=" ")
        print()
