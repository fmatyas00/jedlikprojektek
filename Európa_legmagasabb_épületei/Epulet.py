class Epulet:
    # Az osztály tagjai:
    # - adattagok (változók)
    # - kódtagok (függvények(metódusok), jellemzők, konstruktorok)
    # Láthatósági szintek:
    # - public: mindenki számára elérhető tag
    # - protected: csak az osztály és leszármazott osztályok számára elérhető (_azonsító)
    # - private: csak az osztály számára elérhető (__azonosító)

    # Az osztály adattagjai:
    _név: str
    _város: str
    _ország: str
    _magasság: float
    _emelet: int
    _épült: int

    @property
    def emelet(self) -> int:
        return self._emelet

    @property
    def épület_adatok(self) -> str:
        vissza: str = f"\t név: {self._név}\n"
        vissza += f"\t város: {self._város}\n"
        vissza += f"\t ország: {self._ország}\n"
        vissza += f"\t magasság: {self._magasság}\n"
        vissza += f"\t emelet: {self._emelet}\n"
        vissza += f"\t épült: {self._épült}\n"
        return vissza

    @property
    def magasság(self) -> float:
        return self._magasság

    # Speciális metódus(függvény): konstruktor
    # Minden kódtagnak a self paraméter kötelző első formális paramétere
    # A self paraméter az osztálytagok elérését szolgálja
    # A konstruktor feladata az osztálypéldány (objektum) inicializálása
    def __init__(self, sor: str) -> None:
        m: list[str] = sor.split(";")
        self._név = m[0]
        self._város = m[1]
        self._ország = m[2]
        self._magasság = float(m[3].replace(",", "."))
        self._emelet = int(m[4])
        self._épült = int(m[5])
