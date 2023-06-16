n = int(input("n = "))

ans = [[0] * (2 * n - 1) for i in range(2*n-1)]

a , b = 0 , n-1
ds = [1,1,-1,-1]
dr = [1,-1,-1,1]

mid = n//2 + (1 if n%2 else 0)

dir = 0
for i in range(n*n):
    ans[a][b]=i+1

    if (a == n-1 and b < n-1) or (a == n-1 and b > n-1) or (a>n-1 and b == n-1) or (a<n-1 and b==n-2):
        dir += 1
        if dir == 4 : dir = 0
    a+=ds[dir]
    b+=dr[dir]


for row in ans:
    print(row)