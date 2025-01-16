from Megoldas import Megoldas


def main() -> None:
    # 2. fel.
    m: Megoldas = Megoldas("legmagasabb.txt")
    print(f"3. feladat: épületek száma: {m.epuletek_szama}db")
    print(f"4. feladat: emeletek száma: {m.emeletek_szama}")
    print("5. feladat: legmagasabb épület adatai:")
    print(m.legmagasabb_épület.épület_adatok)

if __name__ == "__main__":
    main()
