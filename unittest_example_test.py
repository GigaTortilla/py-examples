import unittest
import unittest_example as ute

class UnitTestMathOperations(unittest.TestCase):
    def test_math_addition(self):
        '''
        Mathematische Addition testen
        '''

        # einfache Addition
        result = ute.math_addition(2, 2)
        self.assertEqual(result, 4, "Die Addtion sollte 4 ergeben")

    
    def test_math_division(self):
        '''
        Mathematische Division testen
        '''

        # einfache Division
        result = ute.math_division(6, 2)
        self.assertEqual(result, 3.0, "Die Division sollte 3 ergeben")

        # Division durch 0 testen
        with self.assertRaises(ValueError) as ve:
            ute.math_division(10, 0)


if __name__ == '__main__':
    unittest.main()