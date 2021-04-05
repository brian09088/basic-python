#2-19
while True:
      n=int(input('n='))
#loop 1
      for a in range(n):
          print('1'*n + ' '*n + '2'*n)
#loop 2
      for b in range(n):
          print(' '*n + '3'*n + ' '*n)
#loop 3
      for y in range(n-1,-1,-1):
#loop 4
          for x in range(3*n):
              if x<=n-1 and y<=n-1:
                 print(4,end='')
              elif (2*n)<=x<=3*n:
                 print(5,end='')
              else:
                 print(' ',end='')
          print()       