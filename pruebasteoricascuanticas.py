from Teoriacuanticabasica import *
import unittest


class PruebasFunciones(unittest.TestCase):

    def test1(self):
        self.assertEqual([(22, -2), (7, -4), (10.2, -8.1), (0, -7)],
                         position_transition(V,p,V2))

    def test2(self):
        self.assertEqual([(-6, 4), (-7, -3), (-4.2, 8.1), (0, 3)],
                         observable(X,Y))

    def test3(self):
        self.assertEqual([(12, 21), (0, 0), (13, 13), (12, 8)],
                         dynamic(X,V,n)
