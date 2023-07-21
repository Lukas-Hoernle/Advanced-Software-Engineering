from django.test import TestCase
from django.contrib.auth.models import User

from HHPG.domain.entity.haushaltsplan import Haushaltsplan
from HHPG.domain.entity.haushaltsposten import Haushaltsposten
from HHPG.domain.entity.projekt import Projekt
from HHPG.domain.entity.aufwand import Aufwand
from HHPG.infrastruktur.haushaltsplan_repository import HaushaltsplanRepository


class HaushaltsplanRepositoryTestCase(TestCase):
    def setUp(self):
        # Create a test user (replace with actual user creation if needed)
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a Haushaltsplan instance
        self.haushaltsplan = Haushaltsplan.objects.create(
            plan_name='Test Plan',
            standort='Heilbronn',
            startjahr=2023,
            author=self.user,
            studierendenzahl=1000,
        )

        # Create a Haushaltsposten instance associated with the Haushaltsplan
        self.haushaltsposten = Haushaltsposten.objects.create(
            haushaltsplan=self.haushaltsplan,
            posten_name='Test Posten',
        )

        # Create a Projekt instance associated with the Haushaltsposten
        self.projekt = Projekt.objects.create(
            projekt_name='Test Projekt',
            haushaltsposten=self.haushaltsposten,
        )

        # Create an Aufwand instance associated with the Projekt
        self.aufwand = Aufwand.objects.create(
            einnahmen=5000,
            ausgaben=3000,
            projekt=self.projekt,
        )

    def test_get_by_id_including_children(self):
        # Instantiate the HaushaltsplanRepository
        haushaltsplan_repository = HaushaltsplanRepository()

        # Call the method to get the Haushaltsplan including children
        haushaltsplan_id = self.haushaltsplan.id
        haushaltsplan_with_children = haushaltsplan_repository.get_by_id_including_children(haushaltsplan_id)

        # Check if the returned object is a Haushaltsplan instance
        self.assertIsInstance(haushaltsplan_with_children, Haushaltsplan)

        # Check if the Haushaltsplan's haushaltsposten_liste is not empty
        self.assertIsNotNone(haushaltsplan_with_children.haushaltsposten_liste)

        # Check if the Haushaltsplan has the expected attributes and values
        self.assertEqual(haushaltsplan_with_children.plan_name, 'Test Plan')
        self.assertEqual(haushaltsplan_with_children.standort, 'Heilbronn')
        self.assertEqual(haushaltsplan_with_children.startjahr, 2023)
        self.assertEqual(haushaltsplan_with_children.author, self.user)
        self.assertEqual(haushaltsplan_with_children.studierendenzahl, 1000)

        # Check if the Haushaltsposten, Projekt, and Aufwand objects are correctly populated
        haushaltsposten = haushaltsplan_with_children.haushaltsposten_liste[0]
        self.assertEqual(haushaltsposten.posten_name, 'Test Posten')
        self.assertEqual(haushaltsposten.haushaltsplan, self.haushaltsplan)

        projekt = haushaltsposten.projekt_set.first()
        self.assertEqual(projekt.projekt_name, 'Test Projekt')
        self.assertEqual(projekt.haushaltsposten, haushaltsposten)

        aufwand = projekt.aufwand_set.first()
        self.assertEqual(aufwand.einnahmen, 5000)
        self.assertEqual(aufwand.ausgaben, 3000)
        self.assertEqual(aufwand.projekt, projekt)
