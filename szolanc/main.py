def hossz_ok(szo: str) -> bool:
    return len(szo) == 6

def karakter_ok(szo: str) -> bool:
    for k in szo.lower():
        if k < "a" or k > "z":
            return False
    return True

def lanc(elozo_szo: str, szo: str) -> bool:
    if elozo_szo[-1] == szo[0]:
        return True
    return False


def main() -> None:
    print("szólánc játék")
    elozo_szo: str = ""
    helyes_valaszok: int = 0
    sorszam: int = 1
    folytat: bool = True
    while folytat:
        akt_szo: str = input(f"{sorszam}. szó: ")
        if not hossz_ok(akt_szo):
            print("hibás hossz!")
            folytat = False
        if elozo_szo != "" and not lanc(elozo_szo, akt_szo):
            print("nem illeszkedett!")
            folytat = False
        if not karakter_ok(akt_szo):
            print("helytelen karakter(ek)!")
            folytat = False
        if folytat:
            elozo_szo = akt_szo
            sorszam += 1
    print(f"helyes lépések száma: {helyes_valaszok}")
    if helyes_valaszok <= 2:
        print("szint: kezdő")
    elif helyes_valaszok <= 5:
        print("szint: közepes")
    else:
        print("szint: haladó")


if __name__ == "__main__":
    main()
