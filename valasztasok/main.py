from megoldas import Megoldas


def main() -> None:
    m: Megoldas = Megoldas("szavazatok.txt")
    print(f"2. feladat:\nA helyhatósági választáson {m.jeloltek_szama} képviselőjelölt indult.")
    inp: str = str(input(("3. feladat:\nadja meg egy képviselő nevét! ")))
    if m.kereses(inp) != -1:
        print(f"{inp} {m.kereses(inp)} szavazatot kapott.")
    else:
        print("Ilyen nevű képviselő nem szerepel a nyilvántartásban!")
    print(f"4. feladat:\nA választáson {m.szavazatok_szama} állampolgár, a jogosultak {round(m.szavazok_szazaleka(m.szavazatok_szama), 2)}%-a vett részt")
    print(f"5. feladat\n{m.part_szavazatok}")
if __name__ == "__main__":
    main()
