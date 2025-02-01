#2. Feladat
#Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett listaelemek (egész számok) között van páros, ellenkező esetben a visszatérési érték False! A program tartalmazza a függvény hívását is!

# def paros_e(liszt):
#     if any(szam % 2 == 0 for szam in liszt):
#         return True
#     else:
#         return False


def paros_e(liszta):
    for szam in liszta:
        if szam % 2 == 0:
            return True

    return False


szamok = [1, 7, 15, 9]
print(paros_e(szamok))
