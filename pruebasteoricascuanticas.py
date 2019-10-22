from Teoriacuanticabasica import *
import unittest


class PruebasFunciones(unittest.TestCase):
    #Posicion y transicion
    def test1(self):
        self.assertEqual(0.05263157894736842   (0.36842105263157887, 0.31578947368421045),
                         Teoriacuanticabasica.position_transition([(-3,-1),
                                                (0,-2),
                                                (0,1),
                                                (2,0)],   2 ,[(-3,-1),
                                                               (0,-2),
                                                               (0,1),
                                                                (2,0)]))
        
        
    #Media y Varianza
    def test2(self):
        self.assertEqual(2.5,0.25,Teoriacuanticabasica.observable([[(1,0),(0,-1)],
                                  [(0,1),(2,0)]],[((2**(1/2))/2,0),
                                                     (0,(2**(1/2))/2)]))
        
        
        
        
    #Valores propios,vetores propios,Transicion
    def test3(self):
        self.assertEqual([[-1  ,1] [-1,  1]],[[[-0.70710678,  0.70710678]
                                                                            [ 0.70710678 , 0.70710678]]

                                                                            [[ 0,         1        ]
                                                                            [ 1,          0        ]]],(0,-0.9999999999999998)),
        Teoriacuanticabasica.propios([(0,-1),
                                     (1,0)],    [(1,0),
                                                   (0,-1)],)
        
        

    #Sistema dinamico
    def test3(self):
        self.assertEqual([[0.0], 
                          [0.0], 
                          [0.0], 
                          [0.16666666666666666],
                          [0.16666666666666666],
                          [0.3333333333333333],
                          [0.16666666666666666],
                          [0.16666666666666666]],
                         
Teoriacuanticabasica.dynamic(     [[0, 0, 0, 0, 0, 0, 0, 0], 
                                  [0.5, 0, 0, 0, 0, 0, 0, 0], 
                                  [0.5, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0.3333333333333333, 0, 1, 0, 0, 0, 0],
                                  [0, 0.3333333333333333, 0, 0, 1, 0, 0, 0],
                                  [0, 0.3333333333333333, 0.3333333333333333, 0, 0, 1, 0, 0],
                                  [0, 0, 0.3333333333333333, 0, 0, 0, 1, 0],
                                  [0, 0, 0.3333333333333333, 0, 0, 0, 0, 1]],
                                                 
                                  [[1],[0],[0],[0],[0],[0],[0],[0]],       2))



if __name__ == '__main__':
    unittest.main()
