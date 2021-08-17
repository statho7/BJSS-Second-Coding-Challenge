import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_low_band(self):
        test_param = 145000
        result = main.LBBT_tax(test_param)
        self.assertEqual(result, 0)

    def test_second_band(self):
        test_param = 250000
        result = main.LBBT_tax(test_param)
        self.assertEqual(result, 2100)

    def test_third_band(self):
        test_param = 300000
        result = main.LBBT_tax(test_param)
        self.assertEqual(result, 4600)

    def test_fourth_band(self):
        test_param = 485000
        result = main.LBBT_tax(test_param)
        self.assertEqual(result, 21850)

    def test_upper_band(self):
        test_param = 850000
        result = main.LBBT_tax(test_param)
        self.assertEqual(result, 60350)

    def test_empty_string_input(self):
        test_param = ''
        result = main.LBBT_tax(test_param)
        self.assertEqual(result, 'please enter number')

    def test_zero_value_input(self):
        test_param = 0
        result = main.LBBT_tax(test_param)
        self.assertEqual(result, 'please enter number')

    def test_None_input(self):
        test_param = None
        result = main.LBBT_tax(test_param)
        self.assertEqual(result, 'please enter number')

    def test_string_input(self):
        test_param = '_egv45_'
        result = main.LBBT_tax(test_param)
        self.assertTrue(isinstance(result, TypeError))

if __name__ == '__main__':
    unittest.main()