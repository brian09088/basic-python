n=int(input('n= '))
for y in range(0,-2*n,-1):
    for x in range(3*n):
        if x<=(n-1) and y>=-(n-1):
           print('*',end='')
        elif x<=(n-1) and y<=-n:
           print('+',end='')  
        else:
           print('-',end='') 
    print()
