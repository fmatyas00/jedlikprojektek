class Esemeny:
    _id: str
    _time: str
    _kod: int

    def __init__(self, adatsor: str) -> None:
        i, t, k = adatsor.split(" ")
        self._id = i
        self._time = t
        self._kod = int(k)
