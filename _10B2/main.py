from module import *

hallgatok:list[Hallgato] = []
file = open('course.txt', 'r', encoding='utf-8')
for sor in file:
    hallgatok.append(Hallgato(sor))

print(f'3.1: hallgatok szama: {len(hallgatok)} fo')

be_sum:int = 0
for hallgato in hallgatok:
    be_sum += hallgato.eredmenyek['backend']
be_avg:float = be_sum / len(hallgatok)
print(f'3.2: backend eredmenyek atlaga: {round(be_avg, 2)}%')

maxi:int = 0
for index in range(1, len(hallgatok)):
    if hallgatok[index].atlag > hallgatok[maxi].atlag:
        maxi = index
print(f'3.3: legjobb tanulo neve: {hallgatok[maxi].nev}')

print('3.4: akik mar kifizettek a tanfolyamot:')
for hallgato in hallgatok:
    if hallgato.befizetes >= 2600:
        print(f'\t- {hallgato.nev}')

keresett_nev:str = input(f'3.5: irja be a keresett nevet: ')
for hallgato in hallgatok:
    if hallgato.nev == keresett_nev:
        van_pv:bool = False
        for e in hallgato.eredmenyek.values():
            if e < 51: van_pv = True
            break
        if not van_pv:
            print(f'\t{hallgato.nev} minden tanegysegmodulja sikeres!')
        else:
            print(f'\t{hallgato.nev}-nek az alabbiakbol kell PVznie:')
            for tantargy, szazalek in hallgato.eredmenyek.items():
                if szazalek <= 50:
                    print(f'\t\t{tantargy} ({szazalek}%-os eredmeny)')
        break
else: print('\tnincs ilyen nevu hallgato')