"""
Assignment 5-1
Name: 蘇柏瑜
Student Number: 107201522
Course 2020-CE1001
"""
while True:
    start = input("Binary:")
    if start == '-1':
        break
    else:
        n=0
        for a in range(len(start)):
            if int(start[a])<2:
               n+=1
        if n==len(start):
            trans10=0
            for i in range(len(start)):
                aa=int(start[i])
                k=aa*(2**(len(start)-1-i))
                trans10+=k
            num_list=[]
            while trans10>=16:
                num_list+=[trans10%16]
                trans10=trans10//16
            num_list+=[trans10]
            num_list1=num_list[::-1]
            K=""
            for p in range(len(num_list1)):
                if (num_list1[p]>9):
                    K=K+chr(int(num_list1[p])+55)
                else:
                    K=K+str(num_list1[p])
            print("Hexadecimal:"+K)
        else:
            print('Not Binary Number!')


