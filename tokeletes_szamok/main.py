import time


def ez_tökéletes(vszam: int) -> bool:
    osztokszama = sum(i for i in range(1, vszam) if vszam % i == 0)
    if vszam == osztokszama:
        return True
    else:
        return False


def main() -> None:
    t1 = time.time()
    vszam: int = 0  # keresd meg és ird a képernyőre az első négy tökéletes számot
    for vszam in range(1, 10000):
        if ez_tökéletes(vszam):
            print(f"tökéletes szám: {vszam}")
    print("ennyi! nincs több!")
    t2 = time.time()
    print(f"program lefutásának ideje {round(t2 - t1, 3)}s. :)")


if __name__ == "__main__":
    main()
