class ValasztasiEredmeny:
    _kerulet: int
    _szavazatok: int
    _nev: str
    _part: str

    def __init__(self, sor: str) -> None:
        k, sz, vn, kn, p = sor.split(" ")
        self._kerulet = int(k)
        self._szavazatok = int(sz)
        self._nev = vn + " " + kn
        self._part = p
