from megoldas import Megoldas

def main() -> None:
    m: Megoldas = Megoldas("szenhidratok.txt")
    print(f"3. feladat: Élelmiszerek száma: {m.szenhidratok_hossz} db")
    print(f"4. feladat: találatok száma: {m.kissebb_mint_01} db")
    print(f"5. feladat: a legnagyobb szénhidráttartalom: {m.legtobb_szh}")
    print(f"6. feladat: Édesipari termékek átlagos szénhidráttartalma:\nÁtlag: {m.edesipar_atlag_szh} g")
    inp: str = str(input("7. feladat: kérek egy karakterlancot: "))
    if m.kereses(inp) == "kilincs":
        print("nincs találat!")
    else:
        print(m.kereses(inp))
    print(f"9. feladat: {m.kenyerfelektxt}")
if __name__ == "__main__":
    main()
