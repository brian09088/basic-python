n=int(input('n='))

for y in range(2*n-1,-1,-1):
    for x in range(8*n+4):
        if x-y==0 and y<=n-1: 
           print('/',end='')
        elif x-y==2*n:
           print('/',end='')
        elif x-y==6*n and y<=n+1:
           print('/',end='') 
        elif x-y==6*n and y<=n+1:
           print('/',end='') 
        elif x+y==2*n-1 and y<=n-1: 
           print('\\',end='')
        elif x+y==6*n-1:
           print('\\',end='')
        elif x+y==8*n+3 and y<=n+1:
           print('\\',end='')
        elif x+y==8*n+3 and y<=n+1:
           print('\\',end='') 
        elif x+y<6*n-1 and x-y>2*n and y>=0:
           print('-',end='')
        elif x+y<2*n-1 and x-y>0 and y>=0:
           print('-',end='')
        elif x+y<8*n+3 and x-y>6*n and y>=0:
           print('-',end='')   
        else:
           print(' ',end='')
    print()      

