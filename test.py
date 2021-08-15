import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_LBBT_tax(self):
        test_param = 145000
        result = main.LBBT_tax(test_param)
        self.assertEqual(result, 0)

    def test_LBBT_tax1(self):
        test_param = 250000
        result = main.LBBT_tax(test_param)
        self.assertEqual(result, 2100)

    def test_LBBT_tax2(self):
        test_param = 300000
        result = main.LBBT_tax(test_param)
        self.assertEqual(result, 4600)

    def test_LBBT_tax3(self):
        test_param = 485000
        result = main.LBBT_tax(test_param)
        self.assertEqual(result, 21850)

    def test_LBBT_tax4(self):
        test_param = 850000
        result = main.LBBT_tax(test_param)
        self.assertEqual(result, 60350)

    def test_LBBT_tax5(self):
        test_param = ''
        result = main.LBBT_tax(test_param)
        self.assertEqual(result, 'please enter number')

    def test_LBBT_tax6(self):
        test_param = 0
        result = main.LBBT_tax(test_param)
        self.assertEqual(result, 'please enter number')

    def test_LBBT_tax7(self):
        test_param = None
        result = main.LBBT_tax(test_param)
        self.assertEqual(result, 'please enter number')

    def test_LBBT_tax8(self):
        test_param = '_egv45_'
        result = main.LBBT_tax(test_param)
        self.assertTrue(isinstance(result, TypeError))

if __name__ == '__main__':
    unittest.main()