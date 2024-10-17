def main() -> None:
    print("osztók számának meghatározása")
    tol: int = int(input("minimum = "))
    ig: int = int(input("maximum = "))
    while (ig - tol) < 5:
        print("Az ig-tól>=5 feltétel nem teljesül!")
        tol: int = int(input("minimum = "))
        ig: int = int(input("maximum = "))
    összoszto: int = 0
    for vszam in range(tol, ig + 1):
        osztokszama: int = 0
        for oszto in range(1, vszam + 1):
            if vszam % oszto == 0:
                osztokszama += 1
        összoszto += osztokszama
        print(f"{vszam} -> osztók száma: {osztokszama}")
    print(f"összes osztó összege: {összoszto}")


if __name__ == "__main__":
    main()
