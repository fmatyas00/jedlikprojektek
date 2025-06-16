class Fordulo:
    ev: int
    het: int
    fordulo: int
    t13p1: int
    ny13p1: int
    eredmenyek: str
    
    @property
    def nincs_dontetlen(self) -> bool:
        return self.eredmenyek.find("X") == -1
    
    def __init__(self, adatsor: str) -> None:
        é, h, f, t, ny, e = adatsor.split(";")
        self.ev = int(é)
        self.het = int(h)
        self.fordulo = int(f)
        self.t13p1 = int(t)
        self.ny13p1 = int(ny)
        self.eredmenyek = e