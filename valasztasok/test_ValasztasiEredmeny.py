from unittest import TestCase

from ValasztasiEredmeny import ValasztasiEredmeny


class TestValasztasiEredmeny(TestCase):  # testcase a TestValasztasiEredmeny ozstaly őse
    @classmethod
    def setUpClass(cls) -> None:
        cls.eredmeny1: ValasztasiEredmeny = ValasztasiEredmeny("5 19 Ablak Antal -")
        cls.eredmeny2: ValasztasiEredmeny = ValasztasiEredmeny("1 154 Bors Botond HEP")

    def test_nev(self) -> None:
        self.assertEqual(self.eredmeny1.nev, "Ablak Antal")
        self.assertEqual(self.eredmeny2.nev, "Bors Botond")

    def test_szavazatok(self) -> None:
        self.assertEqual(self.eredmeny1.szavazatok, 19)
        self.assertEqual(self.eredmeny2.szavazatok, 154)

    def test_kerulet(self) -> None:
        self.assertEqual(self.eredmeny1.kerulet, "5")
        self.assertEqual(self.eredmeny2.kerulet, "1")

    def test_partjel(self) -> None:
        self.assertEqual(self.eredmeny1.part, "-")
        self.assertEqual(self.eredmeny2.part, "HEP")

    def test_partnev(self) -> None:
        self.assertEqual(self.eredmeny1.part_nev, "Független jelöltek")
        self.assertEqual(self.eredmeny2.part_nev, "Húsevők Pártja")
