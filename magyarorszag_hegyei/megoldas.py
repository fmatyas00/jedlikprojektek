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

    def van_e_magasabb_borzsony(self, bevitel: int) -> bool:
        for i in self._hegycsucsok:
            if bevitel > i.magassag and i.hegyseg == "Börzsöny":
                return False
        return True

    def magassag_lab(self, meter: int) -> float:
        return meter * 3.280839895

    @property
    def haromezer_labnal_magasabb(self) -> int:
        counter: int = 0
        for i in self._hegycsucsok:
            if self.magassag_lab(i.magassag) > 3000:
                counter += 1
        return counter

    @property
    def hegystat(self) -> str:
        matra: int = 0
        bukk: int = 0
        borzsony: int = 0
        zemplen: int = 0
        koszeg: int = 0
        for i in self._hegycsucsok:
            if i.hegyseg == "Mátra":
                matra += 1
            elif i.hegyseg == "Bükk-vidék":
                bukk += 1
            elif i.hegyseg == "Börzsöny":
                borzsony += 1
            elif i.hegyseg == "Zempléni-hegység":
                zemplen += 1
            elif i.hegyseg == "Kőszegi-hegység":
                koszeg += 1
        return f"\n\tMátra - {matra} db\n\tBükk-vidék - {bukk} db\n\tBörzsöny - {borzsony} db\n\tZempléni-hegység - {zemplen} db\n\tKőszegi-hegység - {koszeg} db"

    @property
    def sorokiras(self):
        sorok: list[str] = ["Hegycsúcs neve;Magasság láb\n"]
        for i in self._hegycsucsok:
            if i.hegyseg == "Bükk-vidék":
                sorok.append(f"{i.hegycsucs_neve};{self.magassag_lab(i.magassag)}\n")
        return sorok
