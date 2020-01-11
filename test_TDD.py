import unittest
import TDD

class testUnitTest(unittest.TestCase) :

    def test_g(self):
        self.assertTrue(True)
    
    def test_f1_1(self):
        w1 = 0
        w2 = TDD.f1(w1)
        self.assertEqual(w1,w2)
   
    def test_f1_2(self):
        w1 = 1
        w2 = TDD.f1(w1)
        self.assertEqual(w1,w2)
    
    def test_f1_3(self):
        w1 = 4
        w2 = TDD.f1(2)
        self.assertEqual(w1,w2)

    def test_f1_4(self):
        w1 = 5
        w2 = TDD.f1(2,1)
        self.assertEqual(w1,w2)

    def test_f1_5(self):
        w1 = 7
        w2 = TDD.f1(2,3)
        self.assertEqual(w1,w2)
        

if __name__ == '__main__':
    unittest.main()
