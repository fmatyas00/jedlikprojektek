# Kérj be egy „tól” és egy „ig” értéket!
# A bevitelt ismételt addig, amig nem teljesül az ig-tól>=5 feltétel!
# Ebben az esetben jelenjen meg, hogy „Az ig-tól>=5 feltétel nem teljesül!

# A megadott tartományban írjad ki, hogy az egyes számoknak hány osztója van a következő minta szerint:

# Az 1-6 tartomány osztóinak száma:
# 1 -> Osztók száma: 1
# 2 -> Osztók száma: 2
# 3 -> Osztók száma: 2
# 4 -> Osztók száma: 3
# 5 -> Osztók száma: 2
# 6 -> Osztók száma: 4

# Az osztók számának kiírása után jelenjen meg az összes osztók darabszáma a következő minta szerint:
# Osztók száma összesen: 14db

def main() -> None:
    print("Osztók számának megahtározása")
    tól: int = 0
    ig: int = 0
    while ig - tól < 5:
        tól = int(input("tól = "))
        ig = int(input("ig = "))
        if ig - tól < 5:
            print("Az ig-tól>=5 feltétel nem teljesül!")
    osztók_száma_összesen: int = 0
    for vizsgált_szám in range(tól, ig + 1):
        osztók_száma: int = 0
        for osztó in range(1, vizsgált_szám + 1):
            if vizsgált_szám % osztó == 0:
                osztók_száma += 1
        osztók_száma_összesen += osztók_száma
        print(f"{vizsgált_szám} -> Osztók száma: {osztók_száma}")
        print(f"Osztók száma összesen: {osztók_száma_összesen}db")


if __name__ == "__main__":
    main()
