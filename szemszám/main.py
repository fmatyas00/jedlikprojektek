# Készítsünk személyi azonosító ellenőrzéséhez fgv-t


def kötőjelek_eltávolítása(azon: str) -> str:
    return azon.replace("-", "")


def évszázad(azon: str) -> int:
    első_szám: int = int(azon[0])
    if első_szám in [1, 2, 5, 6]:
        return 1900
    elif első_szám in [3, 4]:
        return 2000
    elif első_szám in [7, 8]:
        return 1800
    else:
        return -1


def szorzatösszeg(évszám: int, azon: str) -> int:
    összeg: int = 0
    for ssz in range(1, 11):
        index = ssz - 1
        szorzó = (
            ssz  # 1997 előtt szorzó 1,2,3,4,5,6,7,8,9,10, de utána 10,9,8,7,6,5,4,3,2,1
        )
        if évszám >= 1997:
            szorzó = 11 - ssz
        összeg += szorzó * int(azon[index])
    return összeg


def ez_Helyes_Személyi_Azonosító(azon: str) -> bool:
    azon = kötőjelek_eltávolítása(azon)
    if len(azon) != 11:
        return False
    születés_éve: int = int(azon[1:3])  # 08
    század: int = évszázad(azon)
    if század == -1:
        return False
    születés_éve += évszázad(azon)  # 2008
    ellenőrző_jegy_számított: int = szorzatösszeg(születés_éve, azon) % 11
    ellenőrző_jegy = int(azon[-1])
    return ellenőrző_jegy == ellenőrző_jegy_számított


def main() -> None:
    azon_input: str = input("adja meg személyi számát: ")
    # azon_fm: str = kötőjelek_eltávolítása("3-080512-0297")
    # azon_nl: str = "16811306218"
    print(ez_Helyes_Személyi_Azonosító(azon_input))


# visszatérés egy true/false, hogy helyes-e
# azonosítóm: 3-080512-0297
# ha 1997 után: 10*3 + 9*0 + 8*8 + 7*0 + 6*5 + 5*1 + 4*2 + 3*0 + 2*2 + 1*9 = 150
# ellenőrző jegy: 150 % 11 = 7
if __name__ == "__main__":
    main()
