with open("3dane.txt") as f:
    dane = [i for i in f.read().split()]


epsilon = ''
gamma = ''
x = len(dane[0])
for bit in range(0, x):
    one = 0
    zero = 0
    for bit1 in range(0, len(dane)):
        if dane[bit1][bit] == '0':
            zero += 1
        else:
            one += 1
    if zero > one:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

e = int(gamma, 2)
g = int(epsilon, 2)


print(g * e)