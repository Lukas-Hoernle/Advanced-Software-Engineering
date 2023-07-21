from unittest import TestCase

from HHPG.domain.entity.projekt import Projekt


class TestProjektRepository(TestCase):
    def setUp(self):
        a= Projekt.__new__()
    def get_by_id(self,a):
        self.assertEqual(a,self.get_by_id(a.id()))
