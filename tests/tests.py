from app.helper import multiply
import unittest

class TestMyFunc(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2,3), 6)

if __name__ == '__main__':
    unittest.main()

