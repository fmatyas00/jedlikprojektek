from megoldas import Megoldas

def main() -> None:
    print("3. feladat: toto\n3.1 feladat: adatok beolvasása és tárolása")
    m: Megoldas = Megoldas("toto.txt")
    print(f"3.2: fordulok szama: {m.fordulok_szama}")
    print(f"3.3: telitalalatos szelvenyek szama {m.telitalaltos_szelvenyek_db} db")
    if m.nincs_dontetlen_fordulo:
        print("Volt döntetlen mentes forduló!")
    else:
        print("Nem volt döntetlen mentes forduló!")
if __name__ == "__main__":
    main()
