def szokoev_listazo(ev1: int, ev2: int) -> str:
    szokoevek: list[int] = []
    szoko_str = ""
    for i in range(min(ev1, ev2), max(ev1, ev2) + 1):
        if i % 400 == 0 or i % 100 != 0 and i % 4 == 0:
            szokoevek.append(i)
    for i in szokoevek:
        szoko_str += f"{i}; "
    return szoko_str[:-2]


def main() -> None:
    print("1. feladat: Kisebb-nagyobb meghatározása")
    a: int = int(input("Kérem az első számot: "))
    b: int = int(input("Kérem a második számot: "))
    if a != b:
        print(f"a nagyobb szám {max(a, b)}, a kisebb {min(a, b)}.")
    else:
        print("A Két szám egyenlő")

    print("2. feladat: Szökőév listázó")
    ev1: int = int(input("Kérem az egyik évszámot: "))
    ev2: int = int(input("Kérem a másik évszámot: "))
    if szokoev_listazo(ev1, ev2):
        print(f"szökőévek: {szokoev_listazo(ev1, ev2)}")
    else:
        print("Nincs szökőév a megadott tartományban!")


if __name__ == "__main__":
    main()
