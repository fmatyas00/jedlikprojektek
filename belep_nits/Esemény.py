class Esemény:
    _azon: str
    _idő: str
    _kód: int

    @property
    def idő(self) -> str:
        return self._idő

    @property
    def ez_menza_esemény(self) -> bool:
        return self._kód == 3

    def __init__(self, adatsor: str) -> None:
        a, i, k = adatsor.split(" ")
        self._azon = a
        self._idő = i
        self._kód = int(k)
