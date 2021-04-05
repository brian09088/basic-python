# 2-21
n=int(input('n='))
for y in range(3*n-1,-1,-1):
    for x in range(3*n):
        if x==(3*n-1)/2 and y==(3*n-1)/2:
             print('x',end='')
        elif x==(n-1)/2 and y==(n-1)/2:
             print('x',end='')   
        elif x==(5*n-1)/2 and y==(5*n-1)/2:
             print('x',end='')       
        elif x==(n-1)/2 and y==(5*n-1)/2:
             print('x',end='')
        elif x==(5*n-1)/2 and y==(n-1)/2:
             print('x',end='')  
        elif (x+y)%(2*n)==n-1:
             print('\\',end='')
        elif (x-y)%(2*n)==0:
             print('/',end='')     
        else:
             print(' ',end='')
    print()       