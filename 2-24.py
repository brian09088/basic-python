# 2-24
n=int(input('n='))
for y in range(n+5,-2*n-6,-1):
    for x in range(-2*n-4,7*n+24):
        if y-x==1 and 1<=y<=(n+2):
            print('/',end='')
        elif x==0 and -n-1<=y<=0:
            print('|',end='')
        elif y==n+3 and (3*n+7)>=x>=(n+2):
            print('-',end='')
        elif x-y==2*n+5 and 2<=y<=(n+3):
            print('/',end='')
        elif y==n+4 and (3*n+9)<=x<=(5*n+15):
            print('_',end='') 
        elif x+y==3*n+7 and -n<=y<=1:
            print('\\',end='')
        elif y==-n and 4*n+8<=x<=4*n+10:
            print('_',end='')
        elif x-y==5*n+11 and -n<=y<=0:
            print('/',end='')
        elif x==4*n+15 and y==1:
            print('@',end='')
        elif 4*n+15<=x<=7*n+16 and y==-n:
            print('_',end='')
        elif x+y==6*n+19 and -n-2<=y<=n+3:     
            print('\\',end='')
        elif x-y==n+2 and -n-1<=x<=0: 
            print('/',end='')
        elif x==-n-2 and y==-2*n-4:
            print('*',end='')
        elif x==1 and y==-n-2:
            print('\\',end='')
        elif x==2 and -2*n-5<=y<=-n-3:
            print('I',end='')
        elif x==n+5 and -2*n-5<=y<=-n-3:
            print('I',end='')    
        elif x==3*n+11 and -2*n-5<=y<=-n-3:
            print('I',end='')
        elif x==4*n+14 and -2*n-5<=y<=-n-3:
            print('I',end='')    
        elif y==-2*n-5 and 3<=x<=n+4:
            print('_',end='')
        elif y==-2*n-5 and 3*n+11<=x<=4*n+13:
            print('_',end='')    
        elif y==-n-2 and n+6<=x<=3*n+10:
            print('_',end='')
        elif x==4*n+15 and y==-n-2:
            print('/',end='')
        elif x==4*n+15 and y==-n-1:
            print('|',end='')
        elif 7*n+17<=x<=8*n+18 and x+y==6*n+16:
            print('\\',end='')
        elif x==8*n+19 and -2*n-4<=y<=-2*n-3:      
            print('|',end='')
        elif x==8*n+21 and -2*n-4<=y<=-n-3:      
            print('|',end='')    
        elif 8*n+19<=x<=8*n+21 and y==-n-6:    
            print(':',end='')       
        else:
            print(' ',end='')
    print()        