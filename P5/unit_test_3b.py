import unittest
from Region3b_pt2v import *

class Unittest_3b(unittest.TestCase):
    def setUp(self):
        print('set up!')
        self.P = (50,80)
        self.T = (710,750)
        self.V = ()
        
    def tearDown(self):
        print('tear down!')
        del self.P
        del self.T
        
    def test_3b_pt2v(self):
        print('test1')
        self.V = (Region3b_pt2v(self.P[0],self.T[0])._Backward3_v_PT(),
                  Region3b_pt2v(self.P[1],self.T[1])._Backward3_v_PT())
        self.assertAlmostEqual(self.V[0],0.002204728587)
        self.assertAlmostEqual(self.V[1],0.001973692940)
    
    def test_inregion3b(self):
        self.P = (50,80)
        self.T = (630,670)
        print('test2')
        try:
            Region3b_pt2v(self.P[0],self.T[0])._Backward3_v_PT()
        except Exception as e:
            print('RegionError:',e)
        
        try:
            Region3b_pt2v(self.P[1],self.T[1])._Backward3_v_PT()
        except Exception as e:
            print('RegionError:',e)

    
    
if __name__ == '__main__':
    unittest.main() 