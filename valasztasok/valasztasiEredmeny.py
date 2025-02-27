class ValasztasiEredmeny:
    _kerulet: int
    _part_szavazatok: int
    _nev: str
    _part: str

    def __init__(self, sor: str) -> None:
        k, sz, vn, kn, p = sor.split(" ")
        self._kerulet = int(k)
        self._part_szavazatok = int(sz)
        self._nev = vn + " " + kn
        self._part = p

    @property
    def nev(self) -> str:
        return self._nev

    @property
    def szavazatok(self) -> int:
        return self._part_szavazatok

    @property
    def part(self) -> str:
        return self._part

    @property
    def part_szavazatok(self) -> int:
        return self._part_szavazatok
