from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.contrib.auth.models import User
from HHPG.domain.entity.haushaltsplan import Haushaltsplan
from HHPG.infrastruktur.haushaltsplan_repository import HaushaltsplanRepository


class HaushaltsplanRepositoryTestCase(TestCase):
    def setUp(self):
        # This method will run before each test method to set up the mock Haushaltsplan object
        self.mock_haushaltsplan = MagicMock(spec=Haushaltsplan)
        self.mock_haushaltsplan.id = 1
        self.mock_haushaltsposten_list = [MagicMock(), MagicMock()]
        self.real_haushaltsplan = Haushaltsplan.objects.create(plan_name='Test Plan', startjahr=2023, studierendenzahl=100)

    def test_create(self):
        # Mock the Haushaltsplan model create method
        with patch.object(Haushaltsplan.objects, 'create', return_value=self.mock_haushaltsplan):
            repository = HaushaltsplanRepository()
            mock_instance = {'plan_name': 'Test Plan', 'startjahr': 2023, 'studierendenzahl': 100}

            # Set the plan_name attribute of the MagicMock object
            self.mock_haushaltsplan.configure_mock(plan_name='Test Plan')
            self.mock_haushaltsplan.configure_mock(startjahr=2023)
            self.mock_haushaltsplan.configure_mock(studierendenzahl=100)

            haushaltsplan = repository.create(None, mock_instance)

            # Check if the Haushaltsplan object is returned correctly
            self.assertIsInstance(haushaltsplan, Haushaltsplan)
            self.assertEqual(haushaltsplan.plan_name, 'Test Plan')
            self.assertEqual(haushaltsplan.startjahr, 2023)
            self.assertEqual(haushaltsplan.studierendenzahl, 100)


    def test_save(self):
        # Mock the Haushaltsplan object save method
        with patch.object(self.mock_haushaltsplan, 'save') as mock_save:
            repository = HaushaltsplanRepository()

            repository.save(None, self.mock_haushaltsplan)

            # Check if the save method is called
            mock_save.assert_called_once()

    def test_delete(self):
        # Mock the Haushaltsplan model filter and delete methods
        with patch.object(Haushaltsplan.objects, 'filter', return_value=MagicMock(delete=lambda: None)):
            repository = HaushaltsplanRepository()
            haushaltsplan_id = 1

            repository.delete(haushaltsplan_id)

            # Check if the delete method is called
            Haushaltsplan.objects.filter.assert_called_once_with(id=haushaltsplan_id)

    # Add other test methods for other repository methods (update_name, get_name, update_standort, get_standort, etc.)
