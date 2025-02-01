#1. Feladat
#Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket (egész számokat) összeadja és az összegükkel tér vissza! A program tartalmazza a függvény hívását is!

def osszegzo(lista):
    osszeg = 0
    for szam in lista:
        osszeg += szam
    return osszeg

szamok = [3, 6, 2]
osszeg = osszegzo(szamok)
print(osszeg)