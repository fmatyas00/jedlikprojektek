def main() -> None:
    print("adj meg 3 számot, én pedig eldöntom, hogy melyik a legnagyobb!")
    a: int = int(input("a: "))
    b: int = int(input("b: "))
    c: int = int(input("c: "))

    while a == b or a == c or b == c:
        print("add meg újra a 3 számot, ne legyenek egyenlőek!")
        a: int = int(input("a: "))
        b: int = int(input("b: "))
        c: int = int(input("c: "))
    if a > b > c:
        print(f"A legnagyobb szám a(z) {a}, a középső a(z) {b}, a legkisebb pedig a(z) {c}. :)")
    elif a > c > b:
        print(f"A legnagyobb szám a(z) {a}, a középső a(z) {c}, a legkisebb pedig a(z) {b}. :)")
    elif b > a > c:
        print(f"A legnagyobb szám a(z) {b}, a középső a(z) {a}, a legkisebb pedig a(z) {c}. :)")
    elif b > c > a:
        print(f"A legnagyobb szám a(z) {b}, a középső a(z) {c}, a legkisebb pedig a(z) {a}. :)")
    elif c > a > b:
        print(f"A legnagyobb szám a(z) {c}, a középső a(z) {a}, a legkisebb pedig a(z) {b}. :)")
    else:
        print(f"A legnagyobb szám a(z) {c}, a középső a(z) {b}, a legkisebb pedig a(z) {a}. :)")
    input("--press enter to exit--")
if __name__ == "__main__":
    main()
