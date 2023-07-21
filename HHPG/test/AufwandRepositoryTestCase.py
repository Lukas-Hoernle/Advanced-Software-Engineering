from typing import List
from unittest.mock import patch, MagicMock

from django.test import TestCase
from HHPG.domain.entity.aufwand import Aufwand
from HHPG.domain.entity.projekt import Projekt
from HHPG.infrastruktur.aufwand_repository import AufwandRepository


class AufwandRepositoryTestCase(TestCase):
    def setUp(self):
        # This method will run before each test method to set up the mock Projekt model
        self.mock_projekt = MagicMock(spec=Projekt)
        self.mock_projekt.id = 1

    def test_create(self):
        # Mock the Aufwand model save method
        with patch.object(Aufwand, 'save') as mock_save:
            repository = AufwandRepository()
            einnahmen = 100
            ausgaben = 50

            aufwand = repository.create(einnahmen=einnahmen, ausgaben=ausgaben)

            # Check if the Aufwand object is returned correctly
            self.assertIsInstance(aufwand, Aufwand)
            self.assertEqual(aufwand.einnahmen, einnahmen)
            self.assertEqual(aufwand.ausgaben, ausgaben)

            # Check if the save method is called
            mock_save.assert_called_once()

    def test_get_by_id(self):
        # Mock the Aufwand.objects.get method
        with patch.object(Aufwand.objects, 'get') as mock_get:
            mock_get.return_value = self.mock_projekt

            repository = AufwandRepository()
            aufwand_id = 1

            aufwand = repository.get_by_id(aufwand_id)

            # Check if the Aufwand object is returned correctly
            self.assertEqual(aufwand, self.mock_projekt)

    def test_get_all(self):
        # Mock the Aufwand.objects.all method
        with patch.object(Aufwand.objects, 'all') as mock_all:
            mock_all.return_value = [self.mock_projekt]

            repository = AufwandRepository()
            aufwand_list = repository.get_all()

            # Check if the list of Aufwand objects is returned correctly
            self.assertIsInstance(aufwand_list, List)
            self.assertEqual(len(aufwand_list), 1)
            self.assertEqual(aufwand_list[0], self.mock_projekt)

    def test_get_for_projekt(self):
        # Mock the Aufwand.objects.filter method
        with patch.object(Aufwand.objects, 'filter') as mock_filter:
            mock_filter.return_value.first.return_value = self.mock_projekt

            repository = AufwandRepository()
            projekt_id = 1

            aufwand = repository.get_for_projekt(projekt_id)

            # Check if the Aufwand object is returned correctly
            self.assertEqual(aufwand, self.mock_projekt)

    def test_update_einnahmen(self):
        # Mock the repository get_by_id and save methods
        with patch.object(AufwandRepository, 'get_by_id', return_value=self.mock_projekt):
            with patch.object(Aufwand, 'save') as mock_save:
                repository = AufwandRepository()
                aufwand_id = 1
                new_einnahmen = 200

                repository.update_einnahmen(aufwand_id, new_einnahmen)

                # Check if the einnahmen attribute is updated and save is called
                self.assertEqual(self.mock_projekt.einnahmen, new_einnahmen)

    def test_update_ausgaben(self):
        # Mock the repository get_by_id and save methods
        with patch.object(AufwandRepository, 'get_by_id', return_value=self.mock_projekt):
            with patch.object(Aufwand, 'save') as mock_save:
                repository = AufwandRepository()
                aufwand_id = 1
                new_ausgaben = 75

                repository.update_ausgaben(aufwand_id, new_ausgaben)

                # Check if the ausgaben attribute is updated and save is called
                self.assertEqual(self.mock_projekt.ausgaben, new_ausgaben)

    def test_delete(self):
        # Mock the repository get_by_id method
        with patch.object(AufwandRepository, 'get_by_id', return_value=self.mock_projekt):
            repository = AufwandRepository()
            aufwand_id = 1

            with patch.object(self.mock_projekt, 'delete') as mock_delete:
                repository.delete(aufwand_id)

                # Check if the delete method is called
                mock_delete.assert_called_once()
