def helyes_szo(szo: str) -> bool:
    if len(szo) == 6 and szo not in "öüóőúéáűí":
        return True
    return False

def lanc(elozo_szo: str, szo: str) -> bool:
    if elozo_szo[-1] == szo[0]:
        return True
    return False

def main() -> None:
    print("szólánc játék")
    elozo_szo: str = " "
    helyes_valaszok: int = 0
    sorszam: int = 1
    szo: str = str(input(f"{sorszam}. adja meg a szót:"))
    if helyes_szo(szo):
        sorszam += 1
        szo: str = str(input(f"{sorszam}. adja meg a szót:"))
        elozo_szo = szo
    while helyes_szo(szo) and lanc(elozo_szo, szo):
        sorszam += 1
        szo: str = str(input(f"{sorszam}. adja meg a szót:"))
        elozo_szo = szo
        helyes_valaszok += 1
    if not helyes_szo(szo):
        print("A karakterek száma téves!")
    else:
        print("Nem illeszkedett!")
    print(f"helyes lépések száma: {helyes_valaszok}")
    if helyes_valaszok <= 2:
        print("szint: kezdő")
    elif helyes_valaszok <= 5:
        print("szint: közepes")
    else:
        print("szint: haladó")
if __name__ == "__main__":
    main()
