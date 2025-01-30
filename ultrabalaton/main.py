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
            osszeg += i.versenyido_float
            fo += 1
    return osszeg / fo


def gyoztes_M_ido_float(futok: list[Futo]) -> float:  # ezt mindet settel is megcsinalom majd ha leulok "örömprogramozni"
    akt_min: float = 9999999999
    for i in futok:
        if i.tt_ferfi and i.ido_oraban < akt_min:
            akt_min = i.ido_oraban
    return akt_min

def gyoztes_F_ido_str(futok: list[Futo]) -> float:
    out = ""
    akt_min: float = 9999999999
    for i in futok:
        if i.tav_szazalek == 100 and i.holgy and i.ido_oraban < akt_min:
            akt_min = i.ido_oraban
    return akt_min

def gyoztes_F_ido_float(futok: list[Futo]) -> float:
    akt_min: float = 9999999999
    for i in futok:
        if i.tav_szazalek == 100 and i.holgy and i.ido_oraban < akt_min:
            akt_min = i.ido_oraban
    return akt_min


def gyoztes_M_nev(futok: list[Futo]) -> str:
    out: str = ""
    for i in futok:
        if gyoztes_M_ido_float(futok) == i.ido_oraban:
            out += i.nev
    return out


def gyoztes_F_nev(futok: list[Futo]) -> str:
    out: str = ""
    for i in futok:
        if gyoztes_F_ido_float(futok) == i.ido_oraban:
            out += i.nev
    return out


def gyoztes_M_rajtszam(futok: list[Futo]) -> str:
    out: str = ""
    for i in futok:
        if gyoztes_M_ido_float(futok) == i.ido_oraban:
            out += i.rajtszam
    return out


def gyoztes_F_rajtszam(futok: list[Futo]) -> str:
    out: str = ""
    for i in futok:
        if gyoztes_F_ido_float(futok) == i.ido_oraban:
            out += i.rajtszam
    return out


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
    print(
        f"8. feladatok: Verseny győztesei:\n\tNők: {gyoztes_F_nev(futok)} ({gyoztes_F_rajtszam(futok)}) - {gyoztes_F_ido_float(futok)}"
    )


if __name__ == "__main__":
    main()
