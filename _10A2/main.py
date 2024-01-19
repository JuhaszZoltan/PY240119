from module import *

hallgatok:list[Hallgato] = []
file = open('course.txt', 'r', encoding='utf-8')
for s in file: hallgatok.append(Hallgato(s))

print(f'3.1: hallgatok szama: {len(hallgatok)} fo')

be_sum:int = 0
for h in hallgatok:
    be_sum += h.eredmenyek['backend']
be_avg:float = round(be_sum / len(hallgatok), 2)
print(f'3.2: backend atlag: {be_avg}%')

maxi:int = 0
for i in range(1, len(hallgatok)):
    if hallgatok[i].ossz_eredmeny > hallgatok[maxi].ossz_eredmeny:
        maxi = i
print(f'3.3: legjobb eredmenyu hallgato: {hallgatok[maxi].nev}')

print('3.4: mar kifizettek:')
for h in hallgatok:
    if h.befizetes >= 2600:
        print(f'\t- {h.nev}')

kv:str = input(f'3.5: ird be a nevet: ')