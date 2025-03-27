from Megoldas import Megoldas


def main() -> None:
    m: Megoldas = Megoldas("bedat.txt")
    print(f"elso be: {m.elsoutolso[0]}, utolso ki: {m.elsoutolso[1]}")
    m.kesok_txt("kesok.txt")
    print(f"4. feladat \nA menzán aznap {m.menzan_etkezett} tanuló ebédelt.")
    print(
        f"5. feladat \nAznap {m.konyvtar_kolcsonzes} tanuló kölcsönzött a könyvtárban. \n\
{m.konyvtar_vs_menza}, mint a menzán."
    )
    print(f"erintett tanulok: {m.erintett_tanulok}")
    azon: str = input("tanulo azon = ")
    m.utolso_ki(azon)
    elsobe: str = m.elso_be(azon)
    utolsoki: str = m.utolso_ki(azon)

    if elsobe == "missing" or utolsoki == "missing":
        print("nincs")
    else:
        iskolaban_perc: int = m.szoveg_perc(utolsoki) - m.szoveg_perc(elsobe)
        print(
            f"szeretetminiszteriumban kinvallatas: {iskolaban_perc // 60} ora {iskolaban_perc % 60} perc"
        )


if __name__ == "__main__":
    main()
