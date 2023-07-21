import unittest
from unittest.mock import patch, MagicMock
from HHPG.domain.entity.projekt import Projekt
from HHPG.infrastruktur.projekt_repository import ProjektRepository
from HHPG.domain.entity.haushaltsposten import Haushaltsposten


class TestProjektRepository(unittest.TestCase):
    @patch('HHPG.infrastruktur.projekt_repository.ProjektRepository')
    def test_create_projekt(self, mock_projekt_repository):
        # Test the create method
        # ...

    @patch('HHPG.infrastruktur.projekt_repository.ProjektRepository')
    def test_get_projekt_by_id(self, mock_projekt_repository):
        # Test the get_by_id method
        # ...

    @patch('HHPG.infrastruktur.projekt_repository.ProjektRepository')
    def test_update_projekt_name(self, mock_projekt_repository):
        # Test the update_name method
        # ...

    @patch('HHPG.infrastruktur.projekt_repository.ProjektRepository')
    def test_get_all(self, mock_projekt_repository):
        # Test the get_all method
        # Mock the ProjektRepository to control its behavior
        mock_projekt_repository.get_all.return_value = [
            Projekt(id=1, projekt_name="Projekt1", einnahmen=1000, ausgaben=500, haushaltsposten=Haushaltsposten(id=1)),
            Projekt(id=2, projekt_name="Projekt2", einnahmen=2000, ausgaben=1000, haushaltsposten=Haushaltsposten(id=2)),
        ]

        # Instantiate the concrete implementation of IProjektRepository
        projekt_repo = mock_projekt_repository()

        # Call the get_all method of ProjektRepository
        projekts = projekt_repo.get_all()

        # Check if the returned projekts list is as expected
        self.assertEqual(len(projekts), 2)
        self.assertEqual(projekts[0].projekt_name, "Projekt1")
        self.assertEqual(projekts[1].projekt_name, "Projekt2")

        # Ensure that the get_all method was called
        mock_projekt_repository.get_all.assert_called_once()

    @patch('HHPG.infrastruktur.projekt_repository.ProjektRepository')
    def test_order_by(self, mock_projekt_repository):
        # Test the order_by method
        # Mock the ProjektRepository to control its behavior
        mock_projekt_repository.order_by.return_value = [
            Projekt(id=1, projekt_name="Projekt1", einnahmen=1000, ausgaben=500, haushaltsposten=Haushaltsposten(id=1)),
            Projekt(id=2, projekt_name="Projekt2", einnahmen=2000, ausgaben=1000, haushaltsposten=Haushaltsposten(id=2)),
        ]

        # Instantiate the concrete implementation of IProjektRepository
        projekt_repo = mock_projekt_repository()

        # Call the order_by method of ProjektRepository
        projekts = projekt_repo.order_by(order="projekt_name")

        # Check if the returned projekts list is as expected
        self.assertEqual(len(projekts), 2)
        self.assertEqual(projekts[0].projekt_name, "Projekt1")
        self.assertEqual(projekts[1].projekt_name, "Projekt2")

        # Ensure that the order_by method was called with the correct parameter
        mock_projekt_repository.order_by.assert_called_once_with(order="projekt_name")

    @patch('HHPG.infrastruktur.projekt_repository.ProjektRepository')
    def test_get_count(self, mock_projekt_repository):
        # Test the get_count method
        # ...

    @patch('HHPG.infrastruktur.projekt_repository.ProjektRepository')
    def test_get_all_by_haushaltsposten(self, mock_projekt_repository):
        # Test the get_all_by_haushaltsposten method
        # ...

    @patch('HHPG.infrastruktur.projekt_repository.ProjektRepository')
    def test_update_haushaltsposten(self, mock_projekt_repository):
        # Test the update_haushaltsposten method
        # ...

    @patch('HHPG.infrastruktur.projekt_repository.ProjektRepository')
    def test_update_einnahmen(self, mock_projekt_repository):
        # Test the update_einnahmen method
        # ...

    @patch('HHPG.infrastruktur.projekt_repository.ProjektRepository')
    def test_update_ausgaben(self, mock_projekt_repository):
        # Test the update_ausgaben method
        # ...

    @patch('HHPG.infrastruktur.projekt_repository.ProjektRepository')
    def test_get_gewinn(self, mock_projekt_repository):
        # Test the get_gewinn method
        # ...


if __name__ == '__main__':
    unittest.main()
