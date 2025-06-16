from fogadasi_fordulo import Fordulo

class Megoldas:
    fordulok: list[Fordulo] = []
    
    def __init__(self, állomány_neve: str) -> None:
        with open("toto.txt", "r", encoding="utf-8") as file:
            for sor in file.read().splitlines()[1:]:  # [1:] - első sor kihagyása
                self.fordulok.append(Fordulo(sor))
                
    @property
    def fordulok_szama(self) -> int:
        return len(self.fordulok)
    
    @property
    def telitalaltos_szelvenyek_db(self) -> int:
        db: int = 0
        for i in self.fordulok:
            db += i.t13p1
        return db
    
    @property
    def nincs_dontetlen_fordulo(self) -> bool:
        for i in self.fordulok:
            if i.nincs_dontetlen:
                return True
        return False