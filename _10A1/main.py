from module import *

# feladat01()

hallgatok:list[Hallgato] = []
file = open('course.txt', 'r', encoding='utf8')
for sor in file:
    hallgatok.append(Hallgato(sor))

print(f'3.1: hallgatok szama: {len(hallgatok)} fo')

sum_bcke:int = 0
for h in hallgatok:
    sum_bcke += h.backend_e
avg_bcke:float = round(sum_bcke/len(hallgatok), 2)
print(f'3.2: backend atlag: {avg_bcke}%')

maxi:int = 0
for i in range(1, len(hallgatok)):
    if hallgatok[i].osszeredmeny > hallgatok[maxi].osszeredmeny:
        maxi = i
print(f'3.3: legjobb eredmenyu hallgato: {hallgatok[maxi].nev}')

print("3.4 mar befizettek:")
for h in hallgatok:
    if h.befizetes >= 2600:
        print(f'\t- {h.nev}')