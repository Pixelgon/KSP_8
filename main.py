# Programovy komentar
# KSP 8 - Spirala prvocisel
import math


def isprime(cislo):
    if cislo == 1:
        return False

    if cislo == 2:
        return True
    if cislo > 2 and cislo % 2 == 0:
        return False

    max_delitel = math.floor(math.sqrt(cislo))
    for a in range(3, 1 + max_delitel, 2):
        if cislo % x == 0:
            return False
    return True


n = int(input("Zadejte číslo: "))
odmocnina = math.ceil(math.sqrt(n))
radek = "" * odmocnina
sloupce = []

for i in range(odmocnina):
    sloupce.append(radek)

y = 0
x = odmocnina // 2
if odmocnina % 2 == 0:
    x -= 1
    y -= 1
y = odmocnina // 2
sloupce[y] = sloupce[y][:x] + 'X' + sloupce[y][x+1:]
# doprava, 1 .. nahoru, 2 .. doleva, 3 .. dolu
smer = 0

for i in range(2, n):
    # doprava
    if smer == 0:
        x += 1
        if sloupce[y - 1][x] == ' ':
            smer = 1
    # nahoru
    elif smer == 1:
        y -= 1
        if sloupce[y][x - 1] == ' ':
            smer = 2
    # doleva
    elif smer == 2:
        x -= 1
        if sloupce[y + 1][x] == ' ':
            smer = 3
    # dolu
    elif smer == 3:
        y += 1
        if sloupce[y][x + 1] == ' ':
            smer = 0

    if isprime(i):
        sloupce[y] = sloupce[y][:x] + '.' + sloupce[y][x + 1:]
    else:
        sloupce[y] = sloupce[y][:x] + '#' + sloupce[y][x + 1:]

file = input("Pod jakým názvem chcete uložit soubor?")
output = open(file, "w")
for x in sloupce:
    output.write(x)


output.close()
exit()
