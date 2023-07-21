from unittest import TestCase
from HHPG.domain.entity.projekt import Projekt


class TestProjektRepository(TestCase):
    def setUp(self):
        self.projekt = Projekt.objects.create(projekt_name="Testprojekt")

    def test_get_by_id(self):
        retrieved_projekt = Projekt.objects.get_by_id(self.projekt.get_id)

        self.assertEqual(self.projekt, retrieved_projekt)
