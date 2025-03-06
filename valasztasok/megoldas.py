from ValasztasiEredmeny import ValasztasiEredmeny


class Megoldas:
    _eredmenyek: list[ValasztasiEredmeny] = []

    def __init__(self, állomány_neve: str) -> None:
        with open(állomány_neve, "r", encoding="utf-8") as file:
            for sor in file.read().splitlines():
                self._eredmenyek.append(ValasztasiEredmeny(sor))

    @property
    def jeloltek_szama(self) -> int:
        return len(self._eredmenyek)

    def kereses(self, inp: str) -> int:
        for i in self._eredmenyek:
            if inp == i.nev:
                return i.szavazatok
        return -1

    @property
    def szavazatok_szama(self) -> int:
        a: int = 0
        for i in self._eredmenyek:
            a += i.szavazatok
        return a

    def szavazok_szazaleka(self, szav: int) -> float:
        return szav / 12345 * 100

    @property
    def part_szavazatok(self) -> dict[str, int]:
        stat: dict[str, int] = {}
        for i in self._eredmenyek:
            if i.part_nev in stat:
                stat[i.part_nev] += i.szavazatok
            else:
                stat[i.part_nev] = i.szavazatok
        return stat

    @property
    def eredmeny_stat(self) -> str:
        out: str = ""
        szav: int = self.szavazatok_szama
        for k, v in self.part_szavazatok.items():
            out += f"\t{k}= {(v/szav):.2%}\n"
        return out

    @property
    def gyoztes_kepviselok(self) -> str:
        out: str = ""
        akt_max: int = 0
        for i in self._eredmenyek:
            if i.szavazatok > akt_max:
                akt_max = i.szavazatok
                out = f"\n{i.nev} {i.part}\n"
        for i in self._eredmenyek:
            if i.szavazatok == akt_max and i.nev not in out:
                out += f"{i.nev} {i.part}\n"
        out.replace("-", "Független")
        return out

    @property
    def kerulet_gyoztes(self) -> None:
        ker_gyoztes: dict[int, str] = {}
        for i in self._eredmenyek:
            if i.kerulet not in ker_gyoztes.items():
                gyoztes: str = ""
                akt_max: int = 0
                for j in self._eredmenyek:
                    if i.kerulet == j.kerulet and j.szavazatok > akt_max:
                        akt_max = j.szavazatok
                        gyoztes = j.nev + " " + j.part
                ker_gyoztes.update({int(i.kerulet): gyoztes.replace("-", "Független")})
        sorok_lista: list[str] = []
        for k, v in dict(sorted(ker_gyoztes.items())).items():
            sorok_lista.append(f"{k}. kerület: {v}\n")
        with open("kepviselok.txt", "w", encoding="utf-8") as file:
            file.writelines(sorok_lista)
