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
    def part_szavazatok(self) -> dict[str, float]:
        out: dict[str, float] = {}
        for i in self._eredmenyek:
            if i.part not in out:
                out.update({i.part: i.part_szavazatok})
            else:
                for k, v in out.items():
                    if k == i.part:
                        v += i.part_szavazatok
        for k, v in out.items():
            out[v] = v / self.szavazatok_szama * 100
        out["Független jelöltek"] = out.pop("-")
        out["Gyümolcsevők Pártja"] = out.pop("GYEP")
        out["Tejivók szövetsége"] = out.pop("TISZ")
        out["Zöldségevők pártja"] = out.pop("ZEP")
        out["Húsevők pártja"] = out.pop("HEP")
        return out
