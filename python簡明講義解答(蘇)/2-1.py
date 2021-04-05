a=1
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            if i != j != k != i and i+j+k==10:
               print(i,j,k,'第',a,'個',sep='') 
               a=a+1
                
