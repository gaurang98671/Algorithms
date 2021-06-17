import unittest

class Test(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(1+2+3, 6, "Should be six")

    def test_sum2(self):
        self.assertEqual(1+2, 5, "Should be 3")

if __name__ == '__main__':
    unittest.main()