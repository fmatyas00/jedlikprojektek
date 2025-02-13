class Kemiai_elemek:
    _felfedezes_ev: int
    _nev: str
    _vegyjel: str
    _rendszam: str
    _felfedezo: str

    def __init__(self, sor: str) -> None:
        ev, nev, jel, rszam, felf = sor.split(";")
        if ev == "Ókor":
            self._felfedezes_ev: int = 0
        else:
            self._felfedezes_ev = int(ev)
        self._nev = nev
        self._vegyjel = jel
        self._rendszam = rszam
        self._felfedezo = felf

    @property
    def felfedezes_ev(self) -> int:
        return self._felfedezes_ev

    @property
    def vegyjel(self) -> str:
        return self._vegyjel

    @property
    def nev(self) -> str:
        return self._nev

    @property
    def rendszam(self) -> str:
        return self._rendszam

    @property
    def felfedezo(self) -> str:
        return self._felfedezo
