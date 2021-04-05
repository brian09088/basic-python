n=int(input('n='))

for i in range(1,n+1):
    print(i,end='')
print()
if n%5==2:
   for k in range(0,n-2): 
       print((abs(4-k))%10,end='')
       print(' '*(n-3),(n+1+k)%10)
   for b in range(0,n):
       print((10+2*n+n-2-b)%10,end='')    
if n%5==3:
   for k in range(0,n-2):
         print((abs(8-k))%10,end='')
         print(' '*(n-3),(n+1+k)%10)
   for b in range(0,n):
       print((10+2*n+n-2-b)%10,end='')        
if n%5==4:
   for k in range(0,n-2):
         print((abs(2-k))%10,end='')
         print(' '*(n-3),(n+1+k)%10)
   for b in range(0,n):
       print((10+2*n+n-2-b)%10,end='')       
if n%5==0:
   for k in range(0,n-2):
         print((abs(6-k))%10,end='')
         print(' '*(n-3),(n+1+k)%10)
   for b in range(0,n):
       print((10+2*n+n-2-b)%10,end='')       
if n%5==1:
   for k in range(0,n-2):
         print((10-abs(0-k))%10,end='')
         print(' '*(n-3),(n+1+k)%10)
   for b in range(0,n):
       print((10+2*n+n-2-b)%10,end='')       
#' '*(n-3)應該為' '*(n-2)?
  


   
