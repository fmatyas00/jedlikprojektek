def taj_atalakit(taj: str) -> list[int]:
    list_out: list[int] = []
    for i in taj:
        list_out.append(int(i))
    return list_out

def szorzatok_osszege(taj: list[int]) -> int:
    szorzatosszeg: int = 0
    for i in range(len(taj) - 1):
        if (i + 1) % 2 == 0:
            szorzatosszeg += taj[i] * 7
        else:
            szorzatosszeg += taj[i] * 3
    return szorzatosszeg

def ellenor(szorzatosszeg: int, ellenorzo: int) -> str:
    if szorzatosszeg % 10 == ellenorzo:
        return "Helyes a szám!"
    return "Hibás a szám!"

def main() -> None:
    taj: str = str(input("Kérem a TAJ-számot: "))
    ellenorzo: int = taj_atalakit(taj)[-1]
    print(f"az ellenőrzőszámjegy: {ellenorzo}")
    print(f"a szorzatok összege: {szorzatok_osszege(taj_atalakit(taj))}")
    print(ellenor(szorzatok_osszege(taj_atalakit(taj)), ellenorzo))
if __name__ == "__main__":
    main()
