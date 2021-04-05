a=int(input('>'))
for i in range(1,4*a-3):
    if i==a+1 or i==a+3 or i==a+5 or i==a+7: 
       print(i,"+"*(a-2))
    elif i > 0:
       i=i%(10) 
    print(i)



   
