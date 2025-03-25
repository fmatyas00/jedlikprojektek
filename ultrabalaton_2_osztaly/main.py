from Futo import Futo

from megoldas import Megoldas

m: Megoldas = Megoldas("ub2017egyeni.txt")

def beolvas(forras: str) -> list[Futo]:
    f: list[Futo] = []
    with open(forras, "r", encoding="utf-8") as file:
        for sor in file.read().splitlines()[1:]:  # [1:] - első sor kihagyása
            f.append(Futo(sor))
    return f



def gyoztes_futo(futok: list[Futo], kat: str) -> Futo:
    f: list[Futo] = []
    for futo in futok:
        if futo.kategoria == kat and futo.celba_ert:
            f.append(futo)
    gyoztes: Futo = f[0]
    for futo in f[1:]:
        if futo.ido_oraban < gyoztes.ido_oraban:
            gyoztes = futo
    return gyoztes


def main() -> None:
    # beolvasas, tarolas
    # chfutok: list[Futo] = beolvas("ub2017egyeni.txt")
    print(f"3. feladat: egyéni indulók: {m.indulok_szama} fő")
    print(f"4. feladat: célba érkező női sportolók: {m.holgyek_a_celban_fo} fő")
    nev_input = input("5. feladat: kérem a sportoló nevét: ")
    indult_egyeniben_seged: str = m.indult_egyeniben(nev_input)
    print(f"\tindult egyéniben a sportoló? {indult_egyeniben_seged}")
    if indult_egyeniben_seged == "igen":
        print(f"\tteljesítette a teljes távot? {m.tav_teljesitve(nev_input)}")
    print(
        f"7. feladat: Átlagos idő: {str(round(m.atlag_ora, 12)).replace(".", ",")} óra"
    )
    gyoztes = m.gyoztes_futo2("Noi")
    if gyoztes is None:
        print("Nincs női győztes")
    else:
        print(f"8. feladatok: Verseny győztesei:\n\tNők: {gyoztes.adatok}")
    gyoztes = m.gyoztes_futo2("Ferfi")
    if gyoztes is None:
        print("Nincs férfi győztes")
    else:
        print(f"\tFérfiak: {gyoztes.adatok}")


if __name__ == "__main__":
    main()
