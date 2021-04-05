n=int(input('n='))
for y in range(-n+1,n):
    for x in range(-n+1,n):
        print(min(n-abs(x),n-abs(y)),end='')          
    print()    


