n=int(input('n= '))
for  b in range(0,-n,-1):
     for  a in range(4*n-3):
          if a-b==2*n-2:
             print((a+1)%10,end='')
          elif a-b==4*n-4:
             print((b+4*n-13)%10,end='')
          elif a+b==0:
             print(a+1,end='')
          elif a+b==2*n-2:
             print((a+1)%10,end='')
          else:
               print(' ',end='')
     print()   
          
