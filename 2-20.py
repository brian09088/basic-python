# 2-20

while True:
      n=int(input('n='))
      
      print('1'*n + ' '*n + '2'*n)
      for a in range(n-2):
          print('1'+' '*(n-2)+'1'+' '*n+'2'+' '*(n-2)+'2')
      print('1'*n + ' '*n + '2'*n)
      
      print(' '*n+'3'*n+' '*n)
      for b in range(n-2):
          print(' '*n+'3'+' '*(n-2)+'3'+' '*n)
      print(' '*n+'3'*n+' '*n)
      
      print('4'*n + ' '*n + '5'*n)
      for a in range(n-2):
          print('4'+' '*(n-2)+'4'+' '*n+'5'+' '*(n-2)+'5')
      print('4'*n + ' '*n + '5'*n)
      
      
           

