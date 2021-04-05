for m in range(1,10):

    for i in range(1,10):
        print("{:>3}".format(m),end=" ")
    print()
    for i in range(1,10):
        print("X"+"{:>2}".format(i),end=" ")
    print()
    for i in range(1,10):
        print("-"*3,end=" ")
    print()
    for i in range(1,10):    
        print("{:>3}".format(i*m),end=" ")
    print()
