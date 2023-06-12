import os
import unittest

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HHPG.settings')

django.setup()

from django.test import TestCase
from HHPG.repository.projekt_repository import ProjektRepository
from HHPG.domain.entity.projekt import Projekt


class TestProjektRepository(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.repository = ProjektRepository()

    def test_create_projekt(self):
        projekt = self.repository.create(name="Testprojekt", einnahmen=1000, ausgaben=500)
        self.assertIsInstance(projekt, Projekt)
        self.assertEqual(projekt.name, "Testprojekt")
        self.assertEqual(projekt.einnahmen, 1000)
        self.assertEqual(projekt.ausgaben, 500)

    def test_get_projekt_by_id(self):
        projekt = self.repository.create(name="Testprojekt", einnahmen=1000, ausgaben=500)
        retrieved_projekt = self.repository.get_by_id(projekt.id)
        self.assertEqual(retrieved_projekt, projekt)

    def test_update_projekt_name(self):
        projekt = self.repository.create(name="Testprojekt", einnahmen=1000, ausgaben=500)
        self.repository.update_name(projekt.id, "Updated Projekt")
        updated_projekt = self.repository.get_by_id(projekt.id)
        self.assertEqual(updated_projekt.name, "Updated Projekt")

    def test_update_projekt_einnahmen(self):
        projekt = self.repository.create(name="Testprojekt", einnahmen=1000, ausgaben=500)
        self.repository.update_einnahmen(projekt.id, 1500)
        updated_projekt = self.repository.get_by_id(projekt.id)
        self.assertEqual(updated_projekt.einnahmen, 1500)

    def test_update_projekt_ausgaben(self):
        projekt = self.repository.create(name="Testprojekt", einnahmen=1000, ausgaben=500)
        self.repository.update_ausgaben(projekt.id, 800)
        updated_projekt = self.repository.get_by_id(projekt.id)
        self.assertEqual(updated_projekt.ausgaben, 800)

    def test_delete_projekt(self):
        projekt = self.repository.create(name="Testprojekt", einnahmen=1000, ausgaben=500)
        self.repository.delete(projekt.id)
        deleted_projekt = self.repository.get_by_id(projekt.id)
        self.assertIsNone(deleted_projekt)


if __name__ == '__main__':
    unittest.main()
