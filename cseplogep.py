# Függvény az aratási gép által megtett út kiszámítására
def aratasi_ut(szelesseg: int, hosszusag: int, aratasi_szelesseg: int):
    # Meghatározzuk, hány teljes sort tud a gép végigjárni a megadott szélesség alapján
    sorok_szama = szelesseg // aratasi_szelesseg  # Egész osztás, csak teljes sorokat számolunk
    # // – egész osztás (angolul: floor division)
    # Ez azt mondja meg, hányszor fér bele az osztó egész számként az osztandóba.

    # Mivel a gép fordulásához hely kell, a sor hossza nem a teljes hosszúság, hanem rövidebb
    sor_hossz = hosszusag - aratasi_szelesseg  # A gép eleje nem tud a teljes hosszúságig menni

    # A megtett út:
    # - Minden sorban végigmegy: sorok_szama * sor_hossz
    # - Minden sor végén fordul: (sorok_szama - 1) * aratasi_szelesseg
    megtett_ut = (sorok_szama * sor_hossz) + ((sorok_szama - 1) * aratasi_szelesseg)

    return megtett_ut  # Visszatérünk a kiszámolt értékkel


# Feladat sorszámának és címének kiírása
print('2. feladat: Aratási gép megtett útjának hossza')

# Bekérjük a földterület hosszúságát méterben (egész szám)
hosszusag = int(input("\tAdja meg a terület hosszúságát méterben: "))

# Bekérjük a földterület szélességét méterben (egész szám)
szelesseg = int(input("\tAdja meg a terület szélességét méterben: "))

# Bekérjük a vágóasztal (aratási) szélességét, amit csak 3 és 12 közötti értékre fogadunk el
aratasi_szelesseg = 0
while aratasi_szelesseg < 3 or aratasi_szelesseg > 12:
    aratasi_szelesseg = int(input("\tAdd meg az aratási szélességét méterben (3-12): "))

# Kiírjuk a gép által megtett teljes utat, a visszatérési értéket felhasználva
print(f"\n\tAz aratási gép által megtett teljes út: {aratasi_ut(szelesseg, hosszusag, aratasi_szelesseg)} méter")

# Kiszámoljuk, hogy mekkora terület marad learatatlanul:
# Ez a szélesség osztási maradéka * hosszúság
maradek_terulet = (szelesseg % aratasi_szelesseg) * hosszusag

# Kiírjuk a maradék terület nagyságát négyzetméterben
print(f"\tA maradék terület: {maradek_terulet} m2")
