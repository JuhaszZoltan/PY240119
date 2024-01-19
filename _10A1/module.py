from random import randint

def feladat01() -> None:
    szamok:list[int] = []
    for _ in range(6):
        szamok.append(randint(2, 5))
    abc:str = "ABCDEF"
    for i in range(len(abc)):
        print(abc[i] * szamok[i], end=' ')


def feladat02(bekert_szoveg:str) -> str:
    szavak:list[str] = bekert_szoveg.split(' ')
    nagybetus_szavak:list[str] = []
    for szo in szavak:
        nagybetus_szavak.append(szo.capitalize())
    pascal_case:str = ''.join(nagybetus_szavak)
    irasjelek:str = '_.!?,:;"\''
    for irasjel in irasjelek:
        pascal_case = pascal_case.replace(irasjel, '')
    ek:str = 'áéíóöőúüűÁÉÍÓÖŐÚÜŰ'
    em:str = 'aeiooouuuAEIOOOUUU'
    for karakter in pascal_case:
        if karakter in ek:
            index:int = ek.index(karakter)
            pascal_case = pascal_case.replace(karakter, em[index])
    return pascal_case


class Hallgato:
    def __init__(self, beolvasott_sor:str) -> None:
        v:list[str] = beolvasott_sor.strip().split(';')
        self.nev:str = v[0]
        self.nem:bool = v[1] == 'm'
        self.befizetes:int = int(v[2])
        self.halozat_e:int = int(v[3])
        self.mobil_e:int = int(v[4])
        self.frontend_e:int = int(v[5])
        self.backend_e:int = int(v[6])
        self.osszeredmeny = self.halozat_e + self.mobil_e + self.backend_e + self.frontend_e