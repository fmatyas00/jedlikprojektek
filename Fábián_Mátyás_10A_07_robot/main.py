def egyszerusit(parancsok: list[int]) -> str:
    E: int = parancsok[0]
    D: int = parancsok[1]
    K: int = parancsok[2]
    N: int = parancsok[3]
    legrovidebb_ut: str = ""
    if K > N:
        legrovidebb_ut += "K" * (K - N)
    elif N > K:
        legrovidebb_ut += "N" * (N - K)
    if E > D:
        legrovidebb_ut += "E" * (E - D)
    elif D > E:
        legrovidebb_ut += "D" * (D - E)
    return legrovidebb_ut


def utasitasok_szama(utasitas: str) -> list[int]:
    E_szam: int = 0
    D_szam: int = 0
    K_szam: int = 0
    N_szam: int = 0
    for i in utasitas.upper():
        if i == "E":
            E_szam += 1
        elif i == "D":
            D_szam += 1
        elif i == "K":
            K_szam += 1
        elif i == "N":
            N_szam += 1
    parancs_lista: list[int] = [E_szam, D_szam, K_szam, N_szam]
    return parancs_lista


def main() -> None:
    utasitas: str = str(input("Kérem a robot parancsait: "))
    print(f"E betűk száma: {utasitasok_szama(utasitas)[0]}")
    print(f"D betűk száma: {utasitasok_szama(utasitas)[1]}")
    print(f"K betűk száma: {utasitasok_szama(utasitas)[2]}")
    print(f"N betűk száma: {utasitasok_szama(utasitas)[3]}")
    print(f"Egy legrövidebb út parancsszava: {egyszerusit(utasitasok_szama(utasitas))}")


if __name__ == "__main__":
    main()
