from Kemiai_elemek import Kemiai_elemek


class Megoldas:
    _kemiai_elemek: list[Kemiai_elemek] = []

    def __init__(self, állomány_neve: str) -> None:
        with open(állomány_neve, "r", encoding="utf-8") as file:
            for sor in file.read().splitlines()[1:]:  # [1:] - első sor kihagyása
                self._kemiai_elemek.append(Kemiai_elemek(sor))

    @property
    def kemiai_elemek(self):
        return self._kemiai_elemek

    @property
    def okorban_felfedezve(self) -> int:
        a: int = 0
        for i in self._kemiai_elemek:
            if i.felfedezes_ev == 0:
                a += 1
        return a

    def elem_adatai(self, keresett: str) -> str:
        for i in self._kemiai_elemek:
            if keresett.lower() == i.vegyjel.lower():
                return f"\tAz elem vegyjele: {i.vegyjel}\n\tAz elem neve: {i.nev}\
                \n\tRendszáma: {i.rendszam}\n\tFelfedezés éve: {"Ókor" if i.felfedezes_ev == 0 else i.felfedezes_ev}\
                \n\tFelfedező: {i.felfedezo}"
        return "kilincs"

    def input_formatum_hiba(self, inp: str) -> bool:
        for i in inp.upper():
            if i < "A" or i > "Z":
                return True
        return False

    @property
    def _stat(self) -> dict[int, int]:
        stat: dict[int,int] = {}
        for elem in self._kemiai_elemek:
            if elem.felfedezes_ev != 0:
                if elem.felfedezes_ev in stat:
                    stat[elem.felfedezes_ev] += 1
                else:
                    stat[elem.felfedezes_ev] = 1
        return stat

    @property
    def stat_out(self) -> str:
        out: str = ""
        for k, v in self._stat.items():
            if v > 3:
                out += f"\t{k}: {v} db \n"
        return out
