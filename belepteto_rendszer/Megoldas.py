from Esemeny import Esemeny

class Megoldas:
    _esemenyek: list[Esemeny] = []

    def __init__(self, all_nev: str) -> None:
        with open(all_nev, "r", encoding="utf-8") as file:
            for sor in file.read().splitlines():  # [1:] - első sor kihagyása
                self._esemenyek.append(Esemeny(sor))
