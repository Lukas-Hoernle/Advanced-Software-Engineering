from unittest import TestCase


class TestProjektRepository(TestCase):
    def test_get_by_id(self):
        self.test_get_by_id()
    def test_get_count(self):
        self.test_get_count()

    def test_get_all_by_haushaltsposten(self):
        self.test_get_all_by_haushaltsposten()

    def test_get_all_by_haushaltsposten_including_children(self):
        self.test_get_all_by_haushaltsposten_including_children()

    def test_get_all_by_name(self):
        self.test_get_all_by_name()

    def test_get_all_by_einnahmen(self):
        self.test_get_all_by_einnahmen()

    def test_get_haushaltsposten(self):
        self.test_get_haushaltsposten()

    def test_get_name(self):
        self.test_get_name()

    def test_get_einnahmen(self):
        self.test_get_einnahmen()

    def test_get_ausgaben(self):
        self.test_get_ausgaben()

