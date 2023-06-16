n = int(input("n = "))

num = int(n*(n+1)/2)

di = [1, 0, 1, 0]
dj = [1, -1, 0, 1]

ans = [[0]*n for _ in range(n)]

p = 0
i , j = 0 , 0

for b in range(1, num+1, 1):
    ans[i][j] = b

    if(i == j and i%2 == 0):    
        p += 1
        if p == 4 : p = 0
        
    if(i == j and i%2 == 1):    
        p += 1
        if p == 4 : p = 0
        
    if(j == 0 and i%2 == 1):
        p += 1
        if p == 4 : p = 0
       
    if(j == 0 and i%2 == 0):
        p += 1
        if p == 4 : p = 0

    i += di[p]
    j += dj[p]

for row in ans:
    print(row)


            
