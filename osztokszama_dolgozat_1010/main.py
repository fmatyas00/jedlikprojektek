def main() -> None:
    # Kérj be egy „tól” és egy „ig” értéket!
    # A bevitelt ismételt addig, amig nem teljesül az ig-tól>=5 feltétel!
    # Ebben az esetben jelenjen meg, hogy „Az ig-tól>=5 feltétel nem teljesül!
    tol: int = int(input("minimum = "))
    ig: int = int(input("maximum = "))
    # A megadott tartományban írjad ki, hogy az egyes számoknak hány osztója van a következő minta szerint:
    while (ig - tol) < 5:
        print("Az ig-tól>=5 feltétel nem teljesül!")
        tol: int = int(input("minimum = "))
        ig: int = int(input("maximum = "))

    for vszam in range(tol, ig + 1):
        osztokszama: int = 0
        for oszto in range(1, vszam + 1):
            if vszam % oszto == 0:
                osztokszama += 1
    print(f"Az {tol}-{ig} tartomány osztóinak száma:")



# Az 1-6 tartomány osztóinak száma:
# 1 -> Osztók száma: 1
# 2 -> Osztók száma: 2
# 3 -> Osztók száma: 2
# 4 -> Osztók száma: 3
# 5 -> Osztók száma: 2
# 6 -> Osztók száma: 4

# Az osztók számának kiírása után jelenjen meg az összes osztók darabszáma a következő minta szerint:
# Osztók száma összesen: 14db


if __name__ == "__main__":
    main()
