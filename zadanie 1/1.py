with open("1dane.txt") as f:
    dane = [i for i in f.read().split("\n")]

previous = dane[0]
licznik = 0


for i in range(3, len(dane)):
    jedynka = int(dane[i]) + int(dane[i-1]) + int(dane[i-2])
    dwojka = int(dane[i-1]) + int(dane[i-2]) + int(dane[i-3])
    if int(jedynka) > int(dwojka):
        licznik += 1

print(licznik)





