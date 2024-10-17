def ez_tökéletes(vszam: int) -> bool:
    for i in range(1, vszam):
        if vszam % i == 0:
            Sum = Sum + i
    if Sum == vszam:
        return True
    else:
        return False

def main() -> None:
    pass  # keresd meg és ird a képernyőre az első négy tökéletes számot


if __name__ == "__main__":
    main()
