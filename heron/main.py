import random


def main() -> None:
    # kérjük be a haromszogek számát (n)
    # addig ismeteljuk ameddig nem teljesül a 5 <= n <= 100 felt.
    # háromszög oldalait generáljuk véletlenszerűen 1 es 100 között
    # bármely 2 oldal összege nagyobb mint a 3.
    # határozzuk meg a kerületeket és területeket
    # output minta:
    # 1. háromszög(a,b,c): t = , k =
    # 2. háromszög(a,b,c): t = , k =
    # ...
    # n. háromszög(a,b,c): t = , k =

    print("héron képlet")
    n: int = int(input("háromszögek száma: "))
    while n < 5 or n > 100:
        n: int = int(input("háromszögek száma (5 <= n <= 100): "))
    a: float = random.uniform(1, 100)
    b: float = random.uniform(1, 100)
    c: float = random.uniform(1, 100)


if __name__ == "__main__":
    main()
