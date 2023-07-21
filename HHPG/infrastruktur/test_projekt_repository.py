from unittest import TestCase

from HHPG.domain.entity.projekt import Projekt


class TestProjektRepository(TestCase):
    def setUp(self):
        Projekt.__new__()
    def get_by_id(self):
        self.assertEqual(self,self.get_by_id(self.id()))
