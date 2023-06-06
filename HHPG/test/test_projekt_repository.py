import os
import unittest

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dein_projekt.settings')

django.setup()

from django.test import TestCase
from HHPG.domain.entity.projekt import Projekt

class TestProjektRepository(TestCase):
    def test_something(self):
        # Test-Code hier
        pass

    def setUp(self):
        super().setUp()
        settings.configure(
            SECRET_KEY='test-secret-key',
            DEBUG=True,
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': 'db.sqlite3',
                }
            },
            INSTALLED_APPS=[
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'HHPG.apps.HhpgConfig',
            ],
            ROOT_URLCONF='ASE.urls',
            TEMPLATES=[
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'APP_DIRS': True,
                },
            ],
            STATIC_URL='/static/',
            USE_I18N=True,
            USE_TZ=True,
        )
        self.repository = ProjektRepository()

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
        self.repository.update_aufwand(projekt.id, 800)
        updated_projekt = self.repository.get_by_id(projekt.id)
        self.assertEqual(updated_projekt.ausgaben, 800)

    def test_delete_projekt(self):
        projekt = self.repository.create(name="Testprojekt", einnahmen=1000, ausgaben=500)
        self.repository.delete(projekt.id)
        deleted_projekt = self.repository.get_by_id(projekt.id)
        self.assertIsNone(deleted_projekt)


if __name__ == '__main__':
    unittest.main()