from unittest import TestCase

from ValasztasiEredmeny import ValasztasiEredmeny


class TestValasztasiEredmeny(TestCase):  # testcase a TestValasztasiEredmeny ozstaly őse
    @classmethod
    def setUpClass(cls) -> None:
        cls.eredmeny1: ValasztasiEredmeny = ValasztasiEredmeny("5 19 Ablak Antal -")
        cls.eredmeny2: ValasztasiEredmeny = ValasztasiEredmeny("1 154 Bors Botond HEP")
        cls.eredmeny3: ValasztasiEredmeny = ValasztasiEredmeny("6 73 Birs Helga GYEP")
        cls.eredmeny4: ValasztasiEredmeny = ValasztasiEredmeny("1 199 Petrezselyem Petra ZEP")
        cls.eredmeny5: ValasztasiEredmeny = ValasztasiEredmeny("7 129 Sajt Hajnalka TISZ")

    def test_nev(self) -> None:
        self.assertEqual(self.eredmeny1.nev, "Ablak Antal")
        self.assertEqual(self.eredmeny2.nev, "Bors Botond")
        self.assertEqual(self.eredmeny3.nev, "Birs Helga")
        self.assertEqual(self.eredmeny4.nev, "Petrezselyem Petra")
        self.assertEqual(self.eredmeny5.nev, "Sajt Hajnalka")

    def test_szavazatok(self) -> None:
        self.assertEqual(self.eredmeny1.szavazatok, 19)
        self.assertEqual(self.eredmeny2.szavazatok, 154)
        self.assertEqual(self.eredmeny3.szavazatok, 73)
        self.assertEqual(self.eredmeny4.szavazatok, 199)
        self.assertEqual(self.eredmeny5.szavazatok, 129)

    def test_kerulet(self) -> None:
        self.assertEqual(self.eredmeny1.kerulet, "5")
        self.assertEqual(self.eredmeny2.kerulet, "1")
        self.assertEqual(self.eredmeny3.kerulet, "6")
        self.assertEqual(self.eredmeny4.kerulet, "1")
        self.assertEqual(self.eredmeny5.kerulet, "7")

    def test_partjel(self) -> None:
        self.assertEqual(self.eredmeny1.part, "-")
        self.assertEqual(self.eredmeny2.part, "HEP")
        self.assertEqual(self.eredmeny3.part, "GYEP")
        self.assertEqual(self.eredmeny4.part, "ZEP")
        self.assertEqual(self.eredmeny5.part, "TISZ")

    def test_partnev(self) -> None:
        self.assertEqual(self.eredmeny1.part_nev, "Független jelöltek")
        self.assertEqual(self.eredmeny2.part_nev, "Húsevők Pártja")
        self.assertEqual(self.eredmeny3.part_nev, "Gyümölcsevők Pártja")
        self.assertEqual(self.eredmeny4.part_nev, "Zöldségevők Pártja")
        self.assertEqual(self.eredmeny5.part_nev, "Tejivók Szövetsége")
