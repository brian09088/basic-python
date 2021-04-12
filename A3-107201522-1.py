"""
Assignment 3-1
Name: 蘇柏瑜
Student Number: 107201522
Course 2020-CE1001
"""
number=int(input("input:"))
def find_factor(number,factor):
    if number%factor==0:
       return 1
    else:
        return 0
def find_prime(factor):
    for i in range(1,factor):
        if factor%i==0 and i!=1:
            return 0
            break
        elif(i==factor-1):
            return 1
print(str(1) + " N")
for i in range(1,number+1):
    if (find_factor(number,i)):
        if find_prime(i)==0:
           print(str(i)+" N")
        elif find_prime(i):
           print(str(i)+" Y")




