from Futo import Futo


def beolvas(forras: str) -> list[Futo]:
    f: list[Futo] = []
    with open(forras, "r", encoding="utf-8") as file:
        for sor in file.read().splitlines()[1:]:  # [1:] - első sor kihagyása
            f.append(Futo(sor))
    return f


def holgyek_a_celban_fo(futok: list[Futo]) -> int:
    fo: int = 0
    for f in futok:
        if f.holgy and f.celba_ert:
            fo += 1
    return fo


def indult_egyeniben(futok: list[Futo], nev: str) -> str:
    for f in futok:
        if f.nev == nev:
            return "igen"
    return "nem"


def tav_teljesitve(futok: list[Futo], nev: str) -> str:
    for f in futok:
        if f.nev == nev and f.tav_szazalek == 100:
            return "igen"
    return "nem"


def atlag_ora(futok: list[Futo]) -> float:
    osszeg: float = 0
    fo: int = 0
    for i in futok:
        if i.tt_ferfi:
            osszeg += i.versenyido
            fo += 1
    return osszeg / fo


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
    futok: list[Futo] = beolvas("ub2017egyeni.txt")
    print(f"3. feladat: egyéni indulók: {len(futok)} fő")
    print(f"4. feladat: célba érkező női sportolók: {holgyek_a_celban_fo(futok)} fő")
    nev_input = input("5. feladat: kérem a sportoló nevét: ")
    indult_egyeniben_seged: str = indult_egyeniben(futok, nev_input)
    print(f"\tindult egyéniben a sportoló? {indult_egyeniben_seged}")
    if indult_egyeniben_seged == "igen":
        print(f"\tteljesítette a teljes távot? {tav_teljesitve(futok, nev_input)}")
    print(
        f"7. feladat: Átlagos idő: {str(round(atlag_ora(futok), 12)).replace(".", ",")} óra"
    )
    print(f"8. feladatok: Verseny győztesei:\n\tNők: {gyoztes_futo(futok, "Noi").adatok}")
    print(f"\tFérfiak: {gyoztes_futo(futok, "Ferfi").adatok}")


if __name__ == "__main__":
    main()
