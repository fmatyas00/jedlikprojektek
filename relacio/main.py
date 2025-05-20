from megoldas import Megoldas

def main() -> None:
    m: Megoldas = Megoldas("relacios.txt")
    print(f"2.feladat: kifejezések száma: {m.hanykifejezes}")
    print(f"3. feladat: kifejezések egyenlőség vizsgálattal: {m.hanyegyenloseg}")
    print(f"4. feladat: {"Van ilyen kifejezés!" if m.oszthato7 else "Nincs ilyen kifejezés!"}")
    print(f"5. feladat: statisztika\n {m.statprint}")
    inp = ""
    while True:
        inp = input("Kérek egy relációs kifejezést (pl.: 5 > 2): ")
        if inp == "vége":
            break
        else:
            print(f"\t{inp} = {m.relvizsgalat(inp)}")
    print(f"8. feladat: eredmenyek.txt {m.eredmenyektxt}")
if __name__ == "__main__":
    main()
