import os
import random
import time


def diszites(i: int) -> str:
    diszek: list[str] = [
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        "#",
        "@",
        "O",
    ]
    output: str = ""
    for _ in range(i * 2):
        output += random.choice(diszek)
    return output


def main() -> None:
    while True:
        print("*".center(24))
        print("/.\\".center(24))
        for i in range(1, 10):
            print(("/" + diszites(i) + "." + "\\").center(24))
            if i % 2 == 0:
                i -= 1
                print(("/" + ("." * (i * 2 + 3)) + "\\").center(24))
        print(("[_]".center(21, "^")).center(23))
        print("MERRY CHRISTMAS!!".center(24))
        time.sleep(1)
        os.system("cls")

if __name__ == "__main__":
    main()
