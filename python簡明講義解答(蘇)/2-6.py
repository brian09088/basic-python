n=int(input('n= '))
for  b in range(0,-n,-1):
     for  a in range(4*n-3):
          if a-b==2*n-2 or a-b==4*n-4 or a+b==0 or a+b==2*n-2:
             print('*',end='')
          else:
             print(' ',end='')
     print()   
          
