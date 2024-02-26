import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test2(self):
        self.assertFalse(True)


if __name__ == '__main__':
    unittest.main()
