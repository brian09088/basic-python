"""
Assignment 2-1
Name: 蘇柏瑜
Student Number: 107201522
Course 2020-CE1001
"""
import random
k=random.randint(1,100)
c=0
while True:
      print("輸入一數字:",end='')
      n=int(input())
      if n>k:
         print("比"+str(n)+"還要小")
         c+=1
      elif n<k:
         print("比"+str(n)+"還要大")
         c+=1
      elif n==k:
         c+=1
         print("猜對了!總共猜了"+str(c)+"次")
         break