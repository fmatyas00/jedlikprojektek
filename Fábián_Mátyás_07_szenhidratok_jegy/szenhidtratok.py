class Szenhidrat:
    _nev: str
    _kategoria: str
    _energia_kj: int
    _energia_kcal: int
    _feherje: float
    _zsir: float
    _szenhidrattartalom: float

    def __init__(self, sor: str) -> None:
        n, k, e_kj, e_kcal, f, zs, sz = sor.split(";")
        self._nev = n
        self._kategoria = k
        self._energia_kj = int(e_kj)
        self._energia_kcal = int(e_kcal)
        self._feherje = float(f)
        self._zsir = float(zs)
        self._szenhidrattartalom = float(sz)

    @property
    def szenhidrattartalom(self):
        return self._szenhidrattartalom

    @property
    def nev(self):
        return self._nev

    @property
    def kategoria(self):
        return self._kategoria
