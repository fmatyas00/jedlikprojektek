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

def main() -> None:
#beolvasas, tarolas
    futok: list[Futo] = beolvas("ub2017egyeni.txt")
    print(f"3. feladat: egyéni indulók: {len(futok)} fő")
    print(f"4. feladat: célba érkező női sportolók: {holgyek_a_celban_fo(futok)} fő")
    nev_input = input("5. feladat: kérem a sportoló nevét: ")
    print(f"\tindult egyéniben a sportoló? {indult_egyeniben(futok, nev_input)}")
    print(f"\tteljesítette a teljes távot? {tav_teljesitve(futok, nev_input)}")
if __name__ == "__main__":
    main()
