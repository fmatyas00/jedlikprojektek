from hegycsucsok import Hegycsucsok

class Megoldas:
    _hegycsucsok: list[Hegycsucsok] = []

    def __init__(self, állomány_neve: str) -> None:
        with open(állomány_neve, "r", encoding="utf-8") as file:
            for sor in file.read().splitlines()[1:]:  # [1:] - első sor kihagyása
                self._hegycsucsok.append(Hegycsucsok(sor))


    @property
    def hegycsucsok(self):
        return self._hegycsucsok

    @property
    def atlag_mag(self) -> float:
        a: float = 0
        for i in self._hegycsucsok:
            a += i.magassag
        return a / len(self._hegycsucsok)

    @property
    def legmagasabb_adatok(self) -> str:
        out = ""
        akt_max: int = 0
        for i in self._hegycsucsok:
            if akt_max < i.magassag:
                akt_max = i.magassag
        for i in self._hegycsucsok:
            if akt_max == i.magassag:
                out = f"\n\tnév: {i.hegycsucs_neve}\n\tHegység: {i.hegyseg}\n\tMagasság: {i.magassag}"
        return out
