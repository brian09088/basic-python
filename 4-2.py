n=int(input(">"))
nom=[[None]*n for i in range(n)]
for i in range(n):
    for s in range(n):
        for t in range(n):
            if abs(s-t)==i:
                nom[s][t]=i+1
            else:
                continue

for j in range(n):
    for  i in range(n):
        print(nom[j][i],end=" ")
    print()
    
            
    
