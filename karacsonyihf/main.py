import random


def pénzfeldobás() -> str:
    szám: int = random.randint(1, 2)
    if szám == 1:
        return "F"
    else:
        return "I"


def esélyek(hossz: int) -> float:
    össz_db: int = 0
    F_db: int = 0
    for _ in range(hossz):
        dobás: str = pénzfeldobás()
        if dobás == "F":
            F_db += 1
        össz_db += 1
    return (F_db / össz_db) * 100


def listaban_FF(hossz: int) -> int:
    FF_előfordulás: int = 0
    előző_dobás: str = ""
    előző_előtti_dobás: str = ""
    for _ in range(hossz):
        dobás: str = pénzfeldobás()
        if előző_előtti_dobás == "F" and előző_dobás == "F" and dobás == "I":
            FF_előfordulás += 1
        előző_előtti_dobás = előző_dobás
        előző_dobás = dobás
    return FF_előfordulás


def leghosszabb_F_sor(hossz: int) -> list[str]:
    dobások_listája: list[str] = []
    for _ in range(hossz):
        dobások_listája.append(pénzfeldobás())
    return dobások_listája


def leghoszabb_F_sor_hossza(hossz: int) -> int:
    dobások_listája: list[str] = leghosszabb_F_sor(hossz)
    fejek_rekord: list[int] = []
    fejek: int = 0
    for dobás in dobások_listája:
        if dobás == "F":
            fejek += 1
        else:
            fejek_rekord.append(fejek)
            fejek = 0
    return max(fejek_rekord)


def nagylista() -> list[str]:
    szuper_lista: list[str] = []
    for _ in range(1000):
        negyes_dobas: str = ""
        for _ in range(4):
            negyes_dobas += pénzfeldobás()
        szuper_lista.append(negyes_dobas)
    return szuper_lista


def FFFF_szam() -> int:
    szuper_lista: list[str] = nagylista()
    return szuper_lista.count("FFFF")


def FFFI_szam() -> int:
    szuper_lista: list[str] = nagylista()
    return szuper_lista.count("FFFI")


def main() -> None:
    print("1. feladat")
    print(f"A pénzfeldobás eredménye: {pénzfeldobás()}")
    print("2. feladat")
    tipp: str = input("Tippeljen! (F/I)= ")
    találat: str = pénzfeldobás()
    print(f"A tipp {tipp.upper()}, a dobás eredménye {találat} volt.")
    if tipp.upper() == találat:
        print("Ön eltalálta!")
    else:
        print("Ön nem találta el!")
    print("3. feladat")
    print("A kísérlet 10000 elemből állt")
    print("4. feladat")
    print(
        f"A kísérlet során a fej relatív gyakorisága {round(esélyek(10000), 2)}% volt."
    )
    print("5. feladat")
    print(
        f"A kísérlet során {listaban_FF(10000)} alkalommal dobtak pontosan két fejet egymás után"
    )
    print("6. feladat")
    print(
        f"A leghosszabb tisztafej sorozat {leghoszabb_F_sor_hossza(10000)} tagból áll, kezdete a(z). dobás."
    )
    print("7. feladat")
    print(f"FFFF: {FFFF_szam()}, FFFI: {FFFI_szam()}")


if __name__ == "__main__":
    main()
