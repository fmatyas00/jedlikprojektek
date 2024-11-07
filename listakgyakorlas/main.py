# keszits fuggvenyt, ami egy listat at 5os lotto lehetseges 5 szamanak ertekevel tolt fel

from itertools import count
import random


def lottoszamgenerator() -> list[int]:
    szamok: list[int] = []
    while len(szamok) < 5:
        szam: int = random.randint(1, 90)
        if not szam in szamok:
            szamok.append(szam)
    return szamok


def max_keresese(t: list[int]) -> int:
    aktualis_max: int = t[0]
    for e in t[
        1:
    ]:  # masodik elemtol indulva keressuk hogy van-e nagyobb elem (mert felesleges a 0. indexhez hasonlítani)
        if e > aktualis_max:
            aktualis_max = e  # ha van nagyobb, akkor az lesz a maximum ertekunk
    return aktualis_max


# 1. adatszerkezet inicializalasa, feltoltese 91 db 0-val
# 2. 1000 huzas generalasa, stat listaban a kihuzott szam db szamanak novelese
# 3. hanyszor huztak ki a legtobbszor kihuzott szamot
def main() -> None:
    stat: list[int] = [0] * 91
    for het in range(1000):
        szamok: list[int] = lottoszamgenerator()
        for szam in szamok:
            stat[szam] += 1
    # maxdarab: int = max(stat) #helyes de tanarur nem (biztos h) engedi mert tudnunk kell magunktol is
    maxdarab: int = max_keresese(stat)
    print(f"A legtöbbször, {maxdarab}x kihúzott szám(ok):")
    for index, ertek in enumerate(stat):
        if ertek == maxdarab:
            print(f"{index}")
    # 4. van-e olyan szám, amit egyszer se huztak ki?
    # 5. melyek azok?
    stat[0] = -1
    if stat.count(0) != 0:
        print("van olyan szám amit nem huztak ki")
        print("azok a számok, amiket nem húztak ki:")
    else:
        print("nincs olyan szám amit nem huztak ki")
    NincsIlyenSzam: bool = True
    for index, ertek in enumerate(stat[1:]):
        if ertek == 0:
            print(index)
        NincsIlyenSzam = False
    if NincsIlyenSzam:
        print("nincs ilyen szám, mindent kihúztak")

#HF.:
#melyiket huzták ki a legkevesebbszer + db szám
    #volt-e olyan hét, amikor minden kihúzott szám páratlan volt (igen/nem)
    # Melyik volt az első olyan hét, amikor a számok összege a legnagyobb volt
    # Melyik volt az első olyan hét, amikor a számok összege a legnagyobb volt
if __name__ == "__main__":
    main()
