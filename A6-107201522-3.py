"""
Assignment 6-3
Name: 蘇柏瑜
Student Number: 107201522
Course 2020-CE1001
"""
final=[]
while True:
      up, north, south, east, west, down = 1, 2, 5, 3, 4, 6
      n= int(input())
      if n==0:
         break
      else:
        for i in range(n):
           dir=input()
           if dir == "east":
              east, up, west, down = up, west, down, east
           elif dir == "west":
               east, down, west, up = down, west, up, east
           elif dir == "north":
               up, south, down, north = south, down, north, up
           elif dir == "south":
               up, north, down, south = north, down, south, up
        final+=('Up:',up,'North:',north,'East:',east,'South:',south,'West:',west,'Down',down)
        continue
long=len(final)
for k in range(long):
    final[k]=str(final[k])
for p in range(long//12):
    print(" ".join(final[12*p:12*(p+1)]))