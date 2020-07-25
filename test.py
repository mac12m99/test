import unittest

class t(unittest.TestCase):
    def test_a(self):
        self.assertTrue(True)
    def test_b(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
