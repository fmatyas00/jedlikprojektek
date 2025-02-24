from szenhidtratok import Szenhidrat


class Megoldas:
    _szenhidratok: list[Szenhidrat] = []

    def __init__(self, allomany_neve: str) -> None:
        with open(allomany_neve, "r", encoding="utf-8") as file:
            for sor in file.read().splitlines()[1:]:  # [1:] - első sor kihagyása
                self._szenhidratok.append(Szenhidrat(sor))

    @property
    def szenhidratok_hossz(self) -> int:
        return len(self._szenhidratok)

    @property
    def kissebb_mint_01(self) -> int:
        a: int = 0
        for i in self._szenhidratok:
            if i.szenhidrattartalom < 0.1:
                a += 1
        return a

    @property
    def legtobb_szh(self) -> str:
        akt_max: float = 0
        akt_legjobb_nev: str = ""
        for i in self._szenhidratok:
            if i.szenhidrattartalom > akt_max:
                akt_max = i.szenhidrattartalom
                akt_legjobb_nev = i.nev
        return f"\n\tétel neve: {akt_legjobb_nev}\n\tMennyiség: {akt_max}"

    @property
    def edesipar_atlag_szh(self) -> float:
        edesipar_hossz: int = 0
        edesipar_ossz: float = 0
        for i in self._szenhidratok:
            if i.kategoria == "Édesipari termékek":
                edesipar_ossz += i.szenhidrattartalom
                edesipar_hossz += 1
        return edesipar_ossz / edesipar_hossz

    #def kategoriak_hossza(self):
        #kat_hossz: dict[str, int] = {}
        #for i in self._szenhidratok:
        #    kat_hossz.

    def kereses(self, inp: str) -> str:
        out: str = ""
        for i in self._szenhidratok:
            if inp.lower() in i.nev.lower():
                out += f"\n\tNév: {i.nev}\n\tKategória: {i.kategoria}\n\tSzénhidrát: {i.szenhidrattartalom} g"
        if out == "":
            return "kilincs"
        return out

    @property
    def kenyerfelektxt(self) -> str:
        sorok_lista: list[str] = ["Nev;Szenhidrat\n"]
        for i in self._szenhidratok:
            if i.kategoria == "Kenyérfélék":
                sorok_lista.append(f"{i.nev};{i.szenhidrattartalom}\n")
        with open("kenyerfelek.txt", "w", encoding="utf-8") as file:
            file.writelines(sorok_lista)
        return "kenyerfelek.txt"
