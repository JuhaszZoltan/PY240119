from random import randint

def feladat01() -> None:
    szamok:list[int] = []
    abc:str = 'ABCDEF'
    for i in range(6):
        szamok.append(randint(2, 5))
        print(abc[i] * szamok[i], end= ' ')


def feladat02(inp:str) -> str:
    kisbetus:str = inp.lower()
    ek:str = 'áéíóöőúüű'
    em:str = 'aeiooouuu'
    abc:str = ' abcdefghijklmnopqrstuvwxyz'
    for k in kisbetus:
        if k in ek:
            kisbetus = kisbetus.replace(k, em[ek.index(k)])
    specmentes:str = kisbetus
    for k in kisbetus:
        if k not in abc: specmentes = specmentes.replace(k, '')
    szavak:list[str] = specmentes.split(' ')
    pascal_case:str = ''
    for szo in szavak:
        pascal_case += szo.capitalize()
    return pascal_case


class Hallgato:
    def __init__(self, beolvasott_sor:str) -> None:
        v:list[str] = beolvasott_sor.strip().split(';')
        self.nev:str = v[0]
        self.nem:bool = v[1] == 'm'
        self.befizetes:int = int(v[2])
        self.eredmenyek:dict = {
            'hálózat' : int(v[3]),
            'mobil' : int(v[4]),
            'frontend' : int(v[5]),
            'backend' : int(v[6])
        }
        self.ossz_eredmeny = sum(self.eredmenyek.values())
