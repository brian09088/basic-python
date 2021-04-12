"""
Assignment 5-2
Name: 蘇柏瑜
Student Number: 107201522
Course 2020-CE1001
"""
while True:
    a=input()
    if '+' in a:
        x = a.split('+')[0]
        y = a.split('+')[1]
        trans1 = 0
        trans2 = 0
        for i in range(len(x)):
            k1 = int(x[i]) * 2 ** (len(x) - 1 - i)
            trans1 += k1

        for j in range(len(y)):
            k2 = int(y[j]) * 2 ** (len(y) - 1 - j)
            trans2 += k2
        sum=trans1+trans2
        result=sum
    elif a=='-1':
        break
    else:
        x = a.split('-')[0]
        y = a.split('-')[1]
        trans1 = 0
        trans2 = 0
        for i in range(len(x)):
            k1 = int(x[i]) * 2 ** (len(x) - 1 - i)
            trans1 += k1

        for j in range(len(y)):
            k2 = int(y[j]) * 2 ** (len(y) - 1 - j)
            trans2 += k2
        minus=trans1-trans2
        result=minus
    list=[]
    while result >= 2:
        list += [result % 2]
        result = result // 2
    list += [result]
    list1 = list[::-1]
    K=''
    for p in range(len(list1)):
        if list1[p]>-1:
            K = K + str(list1[p])
    print(K)