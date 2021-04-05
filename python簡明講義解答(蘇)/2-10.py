n=int(input('n='))
for y in range(1-n,n):
    for x in range(1-n,n):
        if (x-y)>n-1 or (x-y)<1-n or (x+y)>n-1 or (x+y)<1-n:
           print(' ',end='')
        else:
           print(n-max(abs(x),abs(y)),end='')   
    print()
