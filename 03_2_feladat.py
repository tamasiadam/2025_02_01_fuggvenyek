#3.2 Feladat
#Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában, és ezt értékelje ki a függvény! (Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!)

def harommal_oszthatok(szamok):
    db = 0
    for szam in szamok:
        if szam % 3 == 0:
            db += 1
    return db

szamok = []

while True:
    try:
        szam = int(input("Adj meg egy számot(negatív számmal tudsz kilépni): "))
        if szam < 0:
            break
        szamok.append(szam)
    except ValueError:
        print("Kérlek, számot adj meg!")

eredmeny = harommal_oszthatok(szamok)
print(f"hárommal oszthatók száma: {eredmeny}")






























