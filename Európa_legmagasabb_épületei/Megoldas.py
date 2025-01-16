from Epulet import Epulet


class Megoldas:
    _epületek: list[Epulet] = []

    @property #dekorator(??), metodust jellemzove alakit, nem lehet a self-en kivul mas parametere, igy amikor hivjuk, nem rakunk ()-et
    def epuletek_szama(self) -> int:
        return len(self._epületek)

    @property
    def emeletek_szama(self) -> int:
        db: int = 0
        for e in self._epületek:
            db += e.emelet
        return db

    @property
    def legmagasabb_épület(self) -> Epulet:
        legmagasabb: Epulet = self._epületek[0]
        for e in self._epületek[1:]:
            if e.magasság > legmagasabb.magasság:
                legmagasabb = e
        return legmagasabb

    @property
    def van_olasz_épület(self) -> bool:
        for e in self._epületek:
            if e.ez_olasz:
                return True
        return False

    @property
    def épületek_száma_666(self) -> int:
        db: int = 0
        for e in self._epületek:
            if e.magassag_láb > 666:
                db += 1
        return db

    @property
    def _ország_statisztika(self) -> dict[str, int]:
        stat: dict[str, int] = {}
        for e in self._epületek:
            if e.ország in stat:
                stat[e.ország] += 1
            else:
                stat[e.ország] = 1
        return stat

    def __init__(self, állomány_neve: str) -> None:
        with open(állomány_neve, "r", encoding="utf-8") as file:
            for sor in file.read().splitlines()[1:]:  # [1:] - első sor kihagyása
                # Az osztálypéldány (objektum) létrehozása: Epulet(sor)
                self._epületek.append(Epulet(sor))
