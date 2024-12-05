def irany_szam(input1: str, irany: str) -> int:
    if len(input1) == 0:
        raise ValueError("A parancs nem tartalmaz utasításokat!")
    if len(input1) > 200:
        raise ValueError("A parancs túllépit a 200 karakteres korlátot!")
    if len(input1) != input1.count("E") + input1.count("D") + input1.count(
        "K"
    ) + input1.count("N"):
        raise ValueError("Hibás karakter van a parancsban!")
    db: int = 0
    for elem in input1:
        if elem == irany:
            db += 1
    return db


def egyszerusit(E: int, D: int, K: int, N: int) -> str:
    output: str = ""
    if E > D:
        output += "E" * (E - D)
    if D > E:
        output += "D" * (D - E)
    if K > N:
        output += "K" * (K - N)
    if N > K:
        output += "N" * (N - K)
    return output


def main() -> None:
    print("Robot")
    input1: str = str(input("Kérem a robot parancsait: "))
    észak = irany_szam(input1, "E")
    dél = irany_szam(input1, "D")
    kelet = irany_szam(input1, "K")
    nyugat = irany_szam(input1, "N")
    print(f"E betűk száma: {észak}")
    print(f"D betűk száma: {dél}")
    print(f"K betűk száma: {kelet}")
    print(f"N betűk száma: {nyugat}")
    print(
        f"Egy legrövidebb út paracsszava: {egyszerusit(észak, dél, kelet, nyugat)}"
    )


if __name__ == "__main__":
    main()
