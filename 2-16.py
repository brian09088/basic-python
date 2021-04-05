# python簡明學習講義2-16
hh=chr(9472) # 橫
vv=chr(9474) # 豎
nw=chr(9484) #左上
ne=chr(9488) #右上
sw=chr(9492) #左下
se=chr(9496) #右下
n=int(input('n='))
for y in range(0,1-2*n,-1):
    for x in range(n**2+3*n-2):
        if x%(n+3)==n and -(x//(n+3))+3-n-1<=y<=-(x//(n+3))-1:
            print(vv,end='')
        elif x%(n+3)==0 and -(x//(n+3))+3-n-1<=y<=-(x//(n+3))-1:
            print(vv,end='')    
        elif x%(n+3)==0 and y==-(x//(n+3)):
            print(nw,end='')
        elif x%(n+3)==n and y==-(x//(n+3)):
            print(ne,end='')
        elif 0<x%(n+3)<n and -(x//(n+3))-(n-1)<=y<=-(x//(n+3)):
            print(hh,end='')
        elif x%(n+3)==0 and  y==-(x//(n+3))-(n-1):
            print(sw,end='')
        elif x%(n+3)==n and y==-(x//(n+3))-(n-1):
            print(se,end='')
        else:
            print(' ',end='')
    print()        
        
