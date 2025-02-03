class Futo:
    _nev: str
    _rajtszam: str
    _kategoria: str
    _versenyido: str
    _tav_szazalek: int

    @property
    def kategoria(self) -> str:
        return self._kategoria

    @property
    def holgy(self) -> bool:
        return self._kategoria == "Noi"

    @property
    def celba_ert(self) -> bool:
        return self._tav_szazalek == 100

    @property
    def nev(self) -> str:
        return self._nev

    @property
    def tav_szazalek(self) -> int:
        return self._tav_szazalek

    def __init__(self, adatsor: str) -> None:
        nev, rsz, kat, vi, tsz = adatsor.split(";")
        self._nev = nev
        self._rajtszam = rsz
        self._kategoria = kat
        self._versenyido = vi
        self._tav_szazalek = int(tsz)

    @property
    def tt_ferfi(self) -> bool:
        return self._tav_szazalek == 100 and self._kategoria == "Ferfi"

    @property
    def versenyido(self) -> float:
        return float(self.ido_oraban)

    @property
    def rajtszam(self) -> str:
        return self._rajtszam

    @property
    def adatok(self) -> str:
        return f"{self._nev} ({self._rajtszam}) - {self._versenyido}"

    @property
    def ido_oraban(self) -> float:
        h, m, s = self._versenyido.split(":")
        return int(h) + int(m) / 60 + int(s) / 3600
