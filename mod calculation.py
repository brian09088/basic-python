import math
a=int(input("a="))
module=int(input("除數:"))
remainder=int(input("remainder"))
i=0
while (True):
    i=i+1
    if (pow(a,i))%module != remainder:
        continue;
    elif (pow(a,i))%module == remainder:
        print(i,"冪次")
        break
