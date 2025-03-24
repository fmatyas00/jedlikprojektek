from Esemeny import Esemeny

class Megoldas:
    _esemenyek: list[Esemeny] = []

    def __init__(self, all_nev: str) -> None:
        with open(all_nev, "r", encoding="utf-8") as file:
            for sor in file.read().splitlines():  # [1:] - első sor kihagyása
                self._esemenyek.append(Esemeny(sor))

    @property
    def elsoutolso(self) -> list[str]:
        out: list[str] = [self._esemenyek[0].time, self._esemenyek[-1].time]
        return out

    @property
    def kesok_txt(self) -> None:
        sorok_lista: list[str] = []
        for i in self._esemenyek:
            if i.time > "07:50" or i.time < "08:15" and i.kod == 1:
                sorok_lista.append(f"{i.time} {i.id}\n")
        with open("kesok.txt", "w", encoding="utf-8") as file:
            file.writelines(sorok_lista)
