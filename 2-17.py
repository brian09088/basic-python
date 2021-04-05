# python簡明學習講義2-17
n=int(input('n='))
for y in range(0,1-2*n,-1):
    for x in range(pow(n,2)):
        if x%n==0 and -(x//n)+1-n<=y<=-(x//n):
            print((x//n)+1,end='')
        elif x%n==(n-1) and -(x//n)+1-n<=y<=-(x//n):
            print((x//n)+1,end='')
        elif 0<(x%n)<(n-1) and y==-(x//n)+1-n:
            print((x//n)+1,end='')
        else:
            print(' ',end='')
    print()        
