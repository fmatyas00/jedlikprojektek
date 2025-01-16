from Megoldas import Megoldas


def main() -> None:
    # 2. fel.
    m: Megoldas = Megoldas("legmagasabb.txt")
    print(f"3. feladat: épületek száma: {m.epuletek_szama}db")
    print(f"4. feladat: emeletek száma: {m.emeletek_szama}")
    print("5. feladat: legmagasabb épület adatai:")
    print(m.legmagasabb_épület.épület_adatok)
    print(
        f"6. feladat: {'van' if m.van_olasz_épület else "nincs"} olasz épület az adatok közt."
    )
    print(f"666 lábnál magasabb épületek száma: {m.épületek_száma_666}")
    print("8. feladat: Ország statisztika")

if __name__ == "__main__":
    main()
