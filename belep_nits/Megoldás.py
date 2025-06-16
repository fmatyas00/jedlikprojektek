from Esemény import Esemény


class Megoldás:
    _események: list[Esemény] = []

    @property
    def első_belépés(self) -> str:
        return self._események[0].idő

    @property
    def utolsó_belépés(self) -> str:
        utolsó_index: int = len(self._események) - 1
        return self._események[utolsó_index].idő
        # vagy:
        # return self._események[-1].idő

    def __init__(self, állomány_neve: str) -> None:
        with open(állomány_neve, "r", encoding="utf-8") as file:
            for sor in file.read().splitlines():  # [1:] - első sor kihagyása
                self._események.append(Esemény(sor))
