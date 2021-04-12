import math
a=int(input("a="))
b=int(input("mod="))
i=0
while(True):
    if ((a*i)%b!=1):
        i+=1
        continue
    elif ((a*i)%b==1):
        print("a^-1=",i)
        break




