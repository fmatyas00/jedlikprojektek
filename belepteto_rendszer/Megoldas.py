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

    def kesok_txt(self, allomany: str) -> None:
        sorok_lista: list[str] = []
        for i in self._esemenyek:
            if i.keso:
                sorok_lista.append(f"{i.time} {i.id}\n")
        with open(allomany, "w", encoding="utf-8") as file:
            file.writelines(sorok_lista)

    @property
    def menzan_etkezett(self) -> int:
        out: int = 0
        for i in self._esemenyek:
            if i.ez_menza_esemény:
                out += 1
        return out

    @property
    def konyvtar_kolcsonzes(self) -> int:
        out: list[str] = []
        for i in self._esemenyek:
            if i.konyvtar_kod and i.id not in out:
                out.append(i.id)
        return len(out)

    @property
    def konyvtar_vs_menza(self) -> str:
        if self.menzan_etkezett > self.konyvtar_kolcsonzes:
            return "Többen voltak"
        return "Nem voltak többen"

    @property
    def _tanulok_ki_be(self) -> dict[str, int]:
        egyenleg: dict[str, int] = {}
        for i in self._esemenyek:
            if i.belep:
                if i.id not in egyenleg:
                    egyenleg[i.id] = 1
                else:
                    egyenleg[i.id] += 1
            if i.kilep:
                egyenleg[i.id] -= 1
        return egyenleg

    @property
    def erintett_tanulok(self) -> str:
        erintettek : str = ""
        for k, v in self._tanulok_ki_be.items():
            if v != 0:
                erintettek += f"{k} "
        return erintettek

    def elso_be(self, azon: str) -> str:
        for i in self._esemenyek:
            if i. id == azon:
                return i.time
        return "missing"

    def utolso_ki(self, azon: str) -> str:
        for i in range(len(self._esemenyek) - 1, 0, -1):
            if self._esemenyek[i].kilep and self._esemenyek[i].id == azon:
                return self._esemenyek[i].time
        return "missing"

    def szoveg_perc(self, ido: str) -> int:
        ora = int(ido.split(":")[0])
        perc = int(ido.split(":")[1])
        return ora * 60 + perc
