# keszits fuggvenyt, ami egy listat at 5os lotto lehetseges 5 szamanak ertekevel tolt fel

import random


def lottoszamgenerator() -> list[int]:
    szamok: list[int] = []
    while len(szamok) < 5:
        szam: int = random.randint(1, 90)
        if not szam in szamok:
            szamok.append(szam)
    return szamok


def main() -> None:
    print(lottoszamgenerator())


if __name__ == "__main__":
    main()
