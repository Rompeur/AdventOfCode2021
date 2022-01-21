with open("2dane.txt") as f:
    dane = [i for i in f.read().split("\n")]

forward = 0
depth = 0
aim = 0

for col in dane:
    col = col.split()
    if col[0] == "forward":
        forward += int(col[1])
        depth += int(col[1]) * int(aim)
    elif col[0] == "down":
        aim += int(col[1])
    elif col[0] == "up":
        aim -= int(col[1])

print("forward, depth, and aim respectively equals: ", forward, depth)
print("the value of the forward and depth multiplied is: " + str(forward*depth))