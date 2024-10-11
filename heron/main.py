import random
import math
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
    for i in range(n):
        a: float = round(random.uniform(1, 100), 2)
        b: float = round(random.uniform(1, 100), 2)
        c: float = round(random.uniform(1, 100), 2)
        while a + b < c or a + c < b or b + c < a:
            a: float = round(random.uniform(1, 100), 2)
            b: float = round(random.uniform(1, 100), 2)
            c: float = round(random.uniform(1, 100), 2)
        k: float = a + b + c
        s: float = k / 2
        t: float = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"{i + 1}. háromszög ({a}, {b}, {c}): t = {round(t, 2)} , k = {round(k, 2)}")


if __name__ == "__main__":
    main()
