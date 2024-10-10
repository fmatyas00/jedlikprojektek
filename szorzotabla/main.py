import random
import time


def main() -> None:
    print("szorzótábla gyakorlás")
    feladvanyok_szama: int = int(input("feladványok száma (5-25): "))
    while feladvanyok_szama < 5 or feladvanyok_szama > 25:
        feladvanyok_szama: int = int(input("feladványok száma (5-25): "))
    # irjuk ki a feladványt pl: 5 * 5 = (input), ha jo akkor dicsérjük meg, véletlenszerűen 3 különbőző szöveggel,
    # de hibás válasz esetén sajnálkozás után írjuk ki a helyes megoldást
    # feladványok végén: írjuk ki a %os teljesítményt és írjuk ki a megoldásra felhasznált időt
    jovalasz: int = 0
    rosszvalasz: int = 0
    start = time.time()
    for _ in range(feladvanyok_szama):
        a: int = int(random.randint(1, 10))
        b: int = int(random.randint(1, 10))
        ans: int = int(input(f"{a} * {b} = "))
        dicseret = ["Gratulálok!", "Ügyes!", "Szép volt!"]
        if a * b == ans:
            print(f"{random.choice(dicseret)}")
            jovalasz += 1
        else:
            print(f"Ez nem sikerült. :( a helyes válasz {a * b}")
            rosszvalasz += 1
    end = time.time()
    length = end - start
    helyesszazalek = jovalasz / (jovalasz + rosszvalasz) * 100
    print(f"Ennyi idő alatt oldottad meg a feladványokat: {round(length, 2)}s.\n a válaszaid {helyesszazalek}% százaléka volt helyes :)")
if __name__ == "__main__":
    main()
