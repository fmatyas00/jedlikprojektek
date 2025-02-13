from megoldas import Megoldas


def main() -> None:
    # angolabc: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    m: Megoldas = Megoldas("felfedezesek.txt")
    print(f"3. feladat: Elemek száma: {len(m.kemiai_elemek)}")
    print(f"4. feladat: Felfedezések száma az ókorban: {m.okorban_felfedezve}")
    inp: str = str(input("5. feladat: Kérek egy vegyjelet: "))
    while len(inp) > 2 or inp == "" or m.input_formatum_hiba(inp):
        inp: str = str(input("5. feladat: Kérek egy vegyjelet: "))
    print("6. feladat: Keresés")
    if m.elem_adatai(inp) == "kilincs":
        print("\tNincs ilyen elem az adatforrásban")
    else:
        print(m.elem_adatai(inp))


if __name__ == "__main__":
    main()
