"""
Assignment 3-2
Name: 蘇柏瑜
Student Number: 107201522
Course 2020-CE1001
"""
a=input("find: ")
b=input("change to: ")
f=open('text.txt','r')
c=0
fline=f.readlines()
for i in range(len(fline)):
    string=str(fline[i])
    if a in fline[i]:
       if a in string:
          string.replace(a,b)
          c+=string.count(a)
       else:
          pass
    print(fline[i],end='')
    print(string.replace(a,b))
    f.close()
print("change count: "+str(c))