from relacios import RelaciosKifejezes


class Megoldas:
    relacio: list[RelaciosKifejezes] = []

    def __init__(self, állomány_neve: str) -> None:
        with open(állomány_neve, "r", encoding="utf-8") as file:
            for sor in file.read().splitlines():  # [1:] - első sor kihagyása
                self.relacio.append(RelaciosKifejezes(sor))

    @property
    def hanykifejezes(self) -> int:
        return len(self.relacio)
    
    @property
    def hanyegyenloseg(self) -> int:
        a: int = 0
        for i in self.relacio:
            if i.rel == "==":
                a += 1
        return a
    
    @property
    def oszthato7(self) -> bool:
        for i in self.relacio:
            if i.num1 % 7 == 0 and i.num2 % 7 == 0:
                return True
        return False
    
    @property
    def statisztika(self):
        a: int = 0
        b: int = 0
        c: int = 0
        d: int = 0
        e: int = 0
        f: int = 0
        for i in self.relacio:
            if i.rel == "!=":
                a += 1
            elif i.rel == ">=":
                b += 1
            elif i.rel == "==":
                c += 1
            elif i.rel == "<=":
                d += 1
            elif i.rel == ">":
                e += 1
            elif i.rel == "<":
                f += 1
        vissza = {"!=": a, ">=": b, "==": c, "<=": d, ">": e, "<": f}
        return vissza
    
    @property
    def statprint(self) -> str:
        out: str = ""
        for k, v in self.statisztika.items():
            out += "\t" + k + " -> " + str(v) + " db\n"
        return out
    
    def relvizsgalat(self, input1: str) -> str:
        if input1 == "vége":
            return ""
        inp: RelaciosKifejezes = RelaciosKifejezes(input1)
        if inp.rel == "!=":
            if inp.num1 != inp.num2:
                return "Igaz"
            return "Hamis"
        elif inp.rel == ">=":
            if inp.num1 >= inp.num2:
                return "Igaz"
            return "Hamis"
        elif inp.rel == "==":
            if inp.num1 == inp.num2:
                return "Igaz"
            return "Hamis"
        elif inp.rel == "<=":
            if inp.num1 <= inp.num2:
                return "Igaz"
            return "Hamis"
        elif inp.rel == ">":
            if inp.num1 > inp.num2:
                return "Igaz"
            return "Hamis"
        elif inp.rel == "<":
            if inp.num1 < inp.num2:
                return "Igaz"
            return "Hamis"
        return "Hibás relációs operátor!"
    
    @property
    def eredmenyektxt(self) -> None:
        sorok_lista: list[str] = []
        for i in self.relacio:
            a: str = str(i.num1) + " " + i.rel + " " + str(i.num2)
            sorok_lista.append(a + " = " + self.relvizsgalat(a) + "\n")
        with open("eredmenyek.txt", "w", encoding="utf-8") as file:
            file.writelines(sorok_lista)