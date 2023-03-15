import unittest
import math
from calculator import Calculator

paraList = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
ansAdd = [2, 4, 6, 8, 10]
ansDivide = [1, 1, 1, 1, 1]
ansSqrt = [math.sqrt(1), math.sqrt(2), math.sqrt(3),
           math.sqrt(4), math.sqrt(5)]
ansExp = [math.exp(1), math.exp(2), math.exp(3), math.exp(4), math.exp(5)]


class ApplicationTest(unittest.TestCase):

    def setUp(self):
        self.cal = Calculator()

    def test_add(self):
        for i, element in enumerate(paraList):
            with self.subTest():
                print(f'{element[0]} + {element[1]} = {ansAdd[i]}')
                self.assertEqual(self.cal.add(element[0],
                                 element[1]), ansAdd[i])
        with self.assertRaises(TypeError):
            self.cal.add(str(5), 4)
        pass

    def test_divide(self):
        for i, element in enumerate(paraList):
            with self.subTest():
                print(f'{element[0]} / {element[1]} = {ansDivide[i]}')
                self.assertEqual(self.cal.divide(element[0],
                                 element[1]), ansDivide[i])
        with self.assertRaises(TypeError):
            self.cal.divide(str(5), 4)
        pass

    def test_sqrt(self):
        for i, element in enumerate(paraList):
            with self.subTest():
                print(f'{element[0]} sqrt = {ansSqrt[i]}')
                self.assertEqual(self.cal.sqrt(element[0]), ansSqrt[i])
        with self.assertRaises(TypeError):
            self.cal.sqrt(str(5))
        pass

    def test_exp(self):
        for i, element in enumerate(paraList):
            with self.subTest():
                print(f'{element[0]} exp = {ansExp[i]}')
                self.assertEqual(self.cal.exp(element[0]), ansExp[i])
        with self.assertRaises(TypeError):
            self.cal.exp(str(5))
        pass


if __name__ == '__main__':
    unittest.main()
