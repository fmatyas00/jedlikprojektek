from unittest import TestCase

from Megoldas import Megoldas


class Testmegoldas(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.megoldas1: Megoldas = Megoldas("szavazatok.txt")

    def test_jeloltek_szama(self) -> None:
        self.assertEqual(self.megoldas1.jeloltek_szama, 40)

    def test_kepviselo_kereses(self) -> None:
        self.assertEqual(self.megoldas1.kereses("Fasirt Ferenc"), 143)
        self.assertEqual(self.megoldas1.kereses("Jedlik Ányos"), -1)
