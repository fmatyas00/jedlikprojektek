from Futo import Futo


class Megoldas:
    _futok: list[Futo] = []

    @property
    def holgyek_a_celban_fo(self) -> int:
        fo: int = 0
        for f in self._futok:
            if f.holgy and f.celba_ert:
                fo += 1
        return fo

    @property
    def atlag_ora(self) -> float:
        osszeg: float = 0
        fo: int = 0
        for i in self._futok:
            if i.tt_ferfi:
                osszeg += i.versenyido
                fo += 1
        return osszeg / fo

    @property
    def indulok_szama(self) -> int:
        return len(self._futok)

    def indult_egyeniben(self, nev: str) -> str:
        for f in self._futok:
            if f.nev == nev:
                return "igen"
        return "nem"

    def __init__(self, allomany_neve: str) -> None:
        with open(allomany_neve, "r", encoding="utf-8") as file:
            for sor in file.read().splitlines()[1:]:  # [1:] - első sor kihagyása
                self._futok.append(Futo(sor))

    def tav_teljesitve(self, nev: str) -> str:
        for f in self._futok:
            if f.nev == nev and f.tav_szazalek == 100:
                return "igen"
        return "nem"

    def gyoztes_futo(self, kat: str) -> Futo:
        f: list[Futo] = []
        for futo in self._futok:
            if futo.kategoria == kat and futo.celba_ert:
                f.append(futo)
        gyoztes: Futo = f[0]
        for futo in f[1:]:
            if futo.ido_oraban < gyoztes.ido_oraban:
                gyoztes = futo
        return gyoztes
