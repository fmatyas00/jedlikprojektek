class Esemeny:
    _id: str
    _time: str
    _kod: int

    def __init__(self, adatsor: str) -> None:
        i, t, k = adatsor.split(" ")
        self._id = i
        self._time = t
        self._kod = int(k)

    @property
    def time(self) -> str:
        return self._time

    @property
    def kod(self) ->int:
        return self._kod

    @property
    def id(self) -> str:
        return self._id

    @property
    def keso(self) -> bool:
        return self._kod == 1 and self._time > "07:50" and self._time <= "08:15"

    @property
    def ez_menza_esemény(self) -> bool:
        return self._kod == 3

    @property
    def ezKésőTanulóEseménye(self) -> bool:
        return self._kod == 1 and self._time > "07:50" and self._time <= "08:15"

    @property
    def konyvtar_kod(self) -> bool:
        return self._kod == 4

    @property
    def belep(self):
        return self._kod == 1

    @property
    def kilep(self):
        return self._kod == 2

    