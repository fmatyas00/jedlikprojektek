class Hegycsucsok:
    _hegycsucs_neve: str
    _hegyseg: str
    _magassag: int

    def __init__(self, sor: str) -> None:
        nev, hegyseg, mag = sor.split(";")
        self._hegycsucs_neve = nev
        self._hegyseg = hegyseg
        self._magassag = int(mag)

    @property
    def hegycsucs_neve(self):
        return self._hegycsucs_neve

    @property
    def magassag(self):
        return self._magassag

    @property
    def hegyseg(self):
        return self._hegyseg
