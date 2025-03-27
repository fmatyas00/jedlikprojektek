from Megoldás import Megoldás


def main() -> None:
    mo: Megoldás = Megoldás("bedat.txt")

    print("2. feladat")
    print(f"Az első tanuló {mo.első_belépés}-kor lépett be a főkapun.")
    print(f"Az utolsó tanuló {mo.utolsó_belépés}-kor lépett ki a főkapun.")

    # HF: 4, 5 feladatok


if __name__ == "__main__":
    main()
