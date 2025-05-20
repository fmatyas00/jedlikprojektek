class RelaciosKifejezes:
    _num1: int
    _rel: str
    _num2: int

    def __init__(self, sor: str) -> None:
        n1, r, n2 = sor.split(" ")
        self._num1 = int(n1)
        self._rel = r
        self._num2 = int(n2)

    @property
    def rel(self):
        return self._rel
    
    @property
    def num1(self):
        return self._num1
    
    @property
    def num2(self):
        return self._num2