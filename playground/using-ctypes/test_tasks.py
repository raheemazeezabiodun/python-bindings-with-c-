
import unittest
from tasks import add

class TestTasks(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(5, 5), 10)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)

if __name__ == '__main__':
    unittest.main()