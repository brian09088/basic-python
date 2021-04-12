"""
Assignment 6-3
Name: 陳羽暉
Student Number: 107201535
Course 2020-CE1001
"""
result = []
while True:
    n_str = input()
    n_int = int(n_str)
    up, down, east, west, south, north = 1, 6, 3, 4, 5, 2
    if n_int == 0:
        break
    else:
        for d in range(n_int):
            d = input()
            if d == "east":
                east, up, west, down = up, west, down, east
            elif d == "west":
                east, down, west, up = down, west, up, east
            elif d == "north":
                up, south, down, north = south, down, north, up
            elif d == "south":
                up, north, down, south = north, down, south, up
        result += ("Up:", up, "North:", north, "East:", east, "South:", south, "West:", west, "Down:", down)
        continue
l = len(result)
for i in range(l):
    result[i] = str(result[i])
for i in range(l // 12):
    print(" ".join(result[(i*12):((i+1)*12)]))