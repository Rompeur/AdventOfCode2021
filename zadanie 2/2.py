# otwieranie pliku txt i sortowanie po wszystkich nowych liniach
with open("2dane.txt") as f:
    dane = [i for i in f.read().split("\n")]

forward = 0
depth = 0

for row in dane:
    row = row.split()
    if row[0] == "forward":
        forward += int(row[1])
    elif row[0] == "down":
        depth += int(row[1])
    elif row[0] == "up":
        depth -= int(row[1])

print("forward and depths respectively equals: ", forward, depth)
print("the value of those multipied is: " + str(forward*depth))
