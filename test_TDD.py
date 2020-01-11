import unittest
import TDD
import random

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

    def test_f2_1(self):
        w1 = "a"
        w2 = TDD.f2("ala")
        self.assertEqual(w1,w2)

    def test_f2_2(self):
        w1 = 1
        w2 = TDD.f2([1,2,3])
        self.assertEqual(w1,w2)

    def test_f2_3(self):
        w1 = "BUUUUM"
        w2 = TDD.f2()
        self.assertEqual(w1, "BUUUUM")

    def test_f3_1(self):
        w1 = "jeden"
        w2 = TDD.f3(1)
        self.assertEqual(w1,w2)

    def test_f3_2(self):
        w1 = "dwa"
        w2 = TDD.f3(2)
        self.assertEqual(w1,w2)

    def test_f3_3(self):
        w1 = "trzy"
        w2 = TDD.f3(3)
        self.assertEqual(w1,w2)

    def test_f3_4(self):
        w1 = "other"
        w2 = TDD.f3(random.choice(range(4,1000)))
        self.assertEqual(w1,w2)

    def test_f4_1(self):
        w1 = "ala ma kota"
        w2 = TDD.f4("ala")
        self.assertEqual(w1,w2)

    def test_f4_2(self):
        w1 = "kot ma kota"
        w2 = TDD.f4("kot")
        self.assertEqual(w1,w2)
    
    def test_f4_3(self):
        w1 = "kot ma kota i psa"
        w2 = TDD.f4("kot","psa")
        self.assertEqual(w1,w2)

if __name__ == '__main__':
    unittest.main()
