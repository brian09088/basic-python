# python學習講義2-18

hh=chr(9472) # 橫
vv=chr(9474) # 豎
nw=chr(9484) #左上
ne=chr(9488) #右上
sw=chr(9492) #左下
se=chr(9496) #右下
n=int(input('n='))
for y in range(n,-n-1,-1):
    for x in range(4*n**2+1):
        if (y-x/2)%((4*n+1)/2)==1:
            print(nw,end='')
        elif (y-x/2)%((4*n+1)/2)==1 and x%(4*n+1)==2*(n-1)+1:
            print(' ',end='')   
        elif (y-x/2)%((4*n+1)/2)==1 and x%(4*n+1)==2*n:
            print(' ',end='')    
        elif (y-x/2)%((4*n+1)/2)==1 and x%(4*n+1)==0:
            print(' ',end='')    
        elif (y-x/2)%((4*n+1)/2)==1 and x%(4*n+1)==2:
            print(' ',end='')    
        elif y==0 and x%(4*n-1)==2 and x>4*n-1:
            print(vv,end='')
        elif y==0 and x%(4*n-1)==0 and x<=4*n-1:
            print(vv,end='')
        else:
            print(' ',end='')
    print()        
            






