import random


def lotto_gen(db: int, minimum: int, maximum: int) -> set[int]:
    lotto: set[int] = set()
    while len(lotto) < db:
        lotto.add(random.randint(minimum, maximum))
    return lotto


def main() -> None:
    My_numbers: set[int] = {54, 3, 37, 10, 20}
    stat: list[int] = [0] * 6
    for _ in range(85 * 52):  # minden heten egy huzas 85 even at
        szamok: set[int] = lotto_gen(6, 1, 90)
        Talalatok_szama: int = len(szamok.intersection(My_numbers))
        stat[Talalatok_szama] += 1
    for i in range(6):
        print(f"{i} találat: {stat[i]}db")


if __name__ == "__main__":
    main()
