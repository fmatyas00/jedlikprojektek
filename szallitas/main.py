def dobozok(targyak: list[int]) -> list[str]:
    dobozok_tomege: list[str] = []
    doboz_akt: int = 0
    for targy in targyak:
        if doboz_akt + targy <= 20:
            doboz_akt += targy
        else:
            dobozok_tomege.append(str(doboz_akt))
            doboz_akt = targy
    dobozok_tomege.append(str(doboz_akt))
    return dobozok_tomege


def main() -> None:
    targyak: list[int] = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]
    print(f"2. feladat\nA tárgyak tömegének összege: {sum(targyak)}")
    print(
        f"3. feladat\nA dobozok tartalmának tömege (kg): {" ".join(dobozok(targyak))}"
    )
    print(f"szükséges dobozok száma: {len((dobozok(targyak)))}")


if __name__ == "__main__":
    main()
