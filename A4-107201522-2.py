"""
Assignment 4-2
Name: 蘇柏瑜
Student Number: 107201522
Course 2020-CE1001
"""
item=input('查詢項目:')
name=input('姓名:')
s1=item.lower()
s2=name.lower()
f=open("score_107201522.txt",'r')
fline=f.readlines()
first=fline[0].lower()
first1=first.split()
num=first1.index(s1)
for i in range(1,len(fline)):
    who=fline[i].split(' ')[0].lower()
    if s2==who:
        a=fline[i].split(' ')[num]
    else:
        continue
print(name+' '+item+' '+str(a))
f.close()