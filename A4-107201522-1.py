"""
Assignment 4-1
Name: 蘇柏瑜
Student Number: 107201522
Course 2020-CE1001
"""
f=open('score.txt','r')
fline=f.readlines()
text=fline[0]
for i in range(1,len(fline)):
    string=str(fline[i])
    text=text+string.split("\n")[0]
    a=string.split(" ")
    ascore = int(a[1])
    for k in range(1,len(a)):
        score=int(a[k])
        if  k+1<len(a):
            ascore=ascore+int(a[k+1])
        if  k==len(a)-1:
            k=ascore/4
    text=text+" "+str(k)+"\n"
print(text)
filename=('score_107201522.txt','w')
f1=open('score_107201522.txt','w')
f1.write(text)
f1.close()

