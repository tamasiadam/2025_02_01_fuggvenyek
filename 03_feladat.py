#3.1 Feladat
#Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is!

def harommal_oszthatok(lista):
    harommal = []
    for szam in lista:
        if szam % 3 == 0:
            harommal.append(szam)
        else:
            continue

    return harommal

szamok = [3, 6, 9, 1, 2, 12, 15]

print(harommal_oszthatok())