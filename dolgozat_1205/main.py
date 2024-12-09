# function int CélElérveHete(double ektt, double[] mtt)
def cel_elerve_het(ektt: float, mtt:list[float]) -> int:
    for i in range(len(mtt)):
        if mtt[i] <= ektt:
            return i+1
    return 0

# function string CélElérveSzöveg(double ektt, double[] mtt)
def cel_elerve_szoveg(ektt: float, mtt:list[float]) -> str:
    if cel_elerve_het(ektt, mtt) != 0:
        return f"Mari néni a(z) {cel_elerve_het(ektt, mtt)}. héten érte el a célt."
    return "Sajnos Mari néni nem érte el a célját."

# function int EjnyeBejnyeHetekSzáma(double[] mtt)
def ejnyebejnye(mtt: list[float]) -> int:
    multhet: float = mtt[0]
    ejnye_het: int = 0
    for i in range(len(mtt)):
        if mtt[i] > multhet:
            ejnye_het += 1
        multhet = mtt[i]
    return ejnye_het

def main() -> None:
    # segédváltozók a főprogramban:
    # hetek_száma
    # ektt: az elérni kívánt testsúly
    # mtt: Mari néni testtömege a hetek során (lista)
    ektt: float = 93.5
    mtt: list[float] = [95.5, 94.3, 94.4, 93.3, 93.8, 92.9]
    print(f"Hetek száma=6\nElérni kívánt testtömeg (kg)={ektt}")
    for i in range(6):
        print(f"{i+1}. héten={mtt[i]}")
    print(cel_elerve_szoveg(ektt, mtt))
    print(f"A tömege {ejnyebejnye(mtt)} esetben nőtt egyik hétről a másikra.")
if __name__ == "__main__":
    main()
