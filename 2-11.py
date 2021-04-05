n=int(input('n='))
for y in range(n-1,-n,-1):
   for x in range(2*n**2-n+1):
       if (x-y)%(2*n-1)==0 and y!=0:
          print('/',end='')
       elif (x-y)==0 and y!=0:
          print('/',end='')   
       elif (x+y)%(2*n-1)==0 and y!=0:
          print('\\',end='')
       elif (x+y)==0 and y!=0:
          print('\\',end='')   
       elif y==0 and (x-y)%(2*n-1)==0 and (x+y)%(2*n-1)==0:
          print('x',end='')
       elif 0<(x-y)%(2*n-1)<(2*n-1) and 0<(x+y)%(2*n-1)<(2*n-1) and (x-y)//(2*n-1)==(x+y)//(2*n-1):
          print('|',end='')
       else:
          print(' ',end='')
   print()

