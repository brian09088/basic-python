#2-22
n=int(input('n='))
if n % 2 != 0:
   for y in range(n-1,-n,-1):
       for x in range(3*n-2):
           if  x<=2*n-2 and x+y==n-1 :
               print('*',end='')
           elif  x<=2*n-2 and x-y==n-1 :
               print('*',end='') 
           elif  x>=2*n-2 and x+y==3*n-3:
               print('*',end='')
           elif  x>=2*n-2 and x+y==2*n-2:
               print('*',end='')
           elif  x>=2*n-2 and x-y==3*n-3:
               print('*',end='')
           elif  x>=2*n-2 and x-y==2*n-2:
               print('*',end='')     
           else :
               print(' ',end='')
       print()        
else: 
    pass
       