import math


def main() -> None:
    print("Másodfokú egyenlet gyökei")
    print("a * x^2 + b * x + c = 0")
    print("kérem az együtthatókat")
    a: float = float(input("a= "))
    b: float = float(input("b= "))
    c: float = float(input("c= "))
    if a != 0:
        D: float = math.pow(b, 2) - 4 * a * c
        if D > 0:
            print("Két gyök")
            x1: float = (-b + math.sqrt(D)) / (2 * a)
            x2: float = (-b - math.sqrt(D)) / (2 * a)
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
        elif D == 0:
            print("egy gyök")
            x = -b / (2 * a)
            print(f"x = {x}")
        else:
            print("nincs megoldás a valós számok halmazában")
    else:
        print("az egyenlet nem másodfokú")
        if b != 0:
            x = -c / b
        else:
            if c != 0:
                print("ellentmondás")
            else:
                print("azonosság")
if __name__ == "__main__":
    main()
