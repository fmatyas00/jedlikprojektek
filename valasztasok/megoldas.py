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
            