from random import randint

def feladat01() -> None:
    szamok:list[int] = []
    abc:str = 'ABCDEF'
    for i in range(6):
        szamok.append(randint(2, 5))
        print(abc[i] * szamok[i], end=' ')


def feladat02(eredeti:str) -> str: 
    # eredeti:str = "Szeretem az árvíztűrő tükörfúrógépet, de NAGYON!"
    # print(eredeti)
    kisbetus:str = eredeti.lower()
    # print(kisbetus)
    ekezetmentes:str = kisbetus
    ek:str = 'áéíóöőúüű'
    em:str = 'aeiooouuu'
    for karakter in kisbetus:
        if karakter in ek:
            index:int = ek.index(karakter)
            ekezetmentes = ekezetmentes.replace(karakter, em[index])
    # print(ekezetmentes)
    spec:str = '!?.,:-;'
    specmentes:str = ekezetmentes
    for karakter in spec:
        if karakter in specmentes:
            specmentes = specmentes.replace(karakter, '')
    # print(specmentes)
    szavak:list[str] = specmentes.split(' ')
    # print(szavak)
    nagybetus_szavak:list[str] = []
    for szo in szavak:
        nagybetus_szavak.append(szo.capitalize())
    # print(nagybetus_szavak)
    pascal_case:str = ''.join(nagybetus_szavak)
    # print(pascal_case)
    return pascal_case


class Hallgato:
    def __init__(self, beolvasott_sor:str) -> None:
        v:list[str] = beolvasott_sor.strip().split(';')
        self.nev:str = v[0]
        self.nem:bool = v[1] == 'm'
        self.befizetes:int = int(v[2])
        self.eredmenyek:dict = {
            'hálózat': int(v[3]),
            'mobil': int(v[4]),
            'frontend': int(v[5]),
            'backend': int(v[6]),
        }
        self.atlag:float = sum(self.eredmenyek.values()) / len(self.eredmenyek)