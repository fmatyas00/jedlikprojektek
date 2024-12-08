def doboz_szamlal(targyak: list[int]) -> int:
    dobozok_szama: int = 1
    doboz_akt: int = 0
    for i in targyak:
        if doboz_akt + i <= 20:
            doboz_akt += i
        else:
            doboz_akt = i
            dobozok_szama += 1
    return dobozok_szama


def doboz_tomeg(targyak: list[int]) -> list[str]:
    dobozok_tomege: list[str] = []
    doboz_akt: int = 0
    for i in targyak:
        if doboz_akt + i <= 20:
            doboz_akt += i
        else:
            dobozok_tomege.append(str(doboz_akt))
            doboz_akt = i
    dobozok_tomege.append(str(doboz_akt))
    return dobozok_tomege


def main() -> None:
    targyak: list[int] = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]
    print(f"2. feladat\nA tárgyak tömegének összege: {sum(targyak)}")
    print(
        f"3. feladat\nA dobozok tartalmának tömege (kg): {" ".join(doboz_tomeg(targyak))}"
    )
    print(f"szükséges dobozok száma: {(doboz_szamlal(targyak))}")


if __name__ == "__main__":
    main()
