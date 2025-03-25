from megoldas import Megoldas


def main() -> None:
    m: Megoldas = Megoldas("hegyekMo.txt")
    print(f"3. feladat: Hegycsúcsok száma: {len(m.hegycsucsok)} db")
    print(f"4. feladat: Hegycsúcsok átlagos magassága: {m.atlag_mag} m")
    print(f"5. feladat A legmagasabb hegycsúcs adatai:{m.legmagasabb_adatok}")
    bevitel: int = int(input("Kérek egy magasságot: "))
    if m.van_e_magasabb_borzsony(bevitel):
        print(f"van {bevitel}m-nél magasabb hegycsúcs a Börzsönyben!")
    else:
        print(f"nincs {bevitel}m-nél magasabb hegycsúcs a Börzsönyben!")
    print(f"7. feladat: 3000 labnal magasabb hegycsucsok szama: {m.haromezer_labnal_magasabb}")
    print(f"8. feladat: Hegység statisztika {m.hegystat}")
    with open("bukk-videk.txt", "w", encoding="utf-8") as file:
        file.writelines(m.sorokiras)
    print("9. feladat: bukk-videk.txt")
if __name__ == "__main__":
    main()
