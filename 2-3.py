a=int(input('a='))
b=int(input('b='))
x=len(str(b))


print("{:>10}".format(a))
print("{:<1}{:>9}".format('x',b))
print("{:_<10}".format(''))


for aa in range(1,x+1):

    b1=(b%pow(10,aa))//pow(10,aa-1)
    if b1 != 0 :
       print("{:>10}".format(a*b1*pow(10,aa-1)))
print("{:_<10}".format(''))

s=a*(b%10)
def total(s):
    for aa in range(1,x+1):
        b1=(b%pow(10,aa))//pow(10,aa-1)
        if b1 != 0 :
           k=a*b1*pow(10,aa-1)
           if k != a*b1*pow(10,0):
              s=s+k
           else:
               s=a*(b%10)
    return s
          
print("{:>10}".format(total(s)))    
    

    
    
      



