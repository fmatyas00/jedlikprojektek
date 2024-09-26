def main() -> None:
    print("másodfokú egyenlet gyökei")
    a: int = int(input("a: "))
    b: int = int(input("b: "))
    c: int = int(input("c: "))
    x = -b / 2 * a
    if a != 0:
        if b * b >= 4 * a * c:
            print("két gyök")
        else: 
            print(f"egy gyök: {x}")
if __name__ == "__main__":
    main()
