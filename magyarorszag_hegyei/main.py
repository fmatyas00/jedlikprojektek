from megoldas import Megoldas


def main() -> None:
    m: Megoldas = Megoldas("hegyekMo.txt")
    print(f"3. feladat: Hegycsúcsok száma: {len(m.hegycsucsok)} db")
    print(f"4. feladat: Hegycsúcsok átlagos magassága: {m.atlag_mag} m")
    print(f"5. feladat A legmagasabb hegycsúcs adatai:{m.legmagasabb_adatok}")

if __name__ == "__main__":
    main()
