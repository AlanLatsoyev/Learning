import unittest
from bowling import get_score


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(get_score('x1254879---284/5/'), 96)  # add assertion here


if __name__ == '__main__':
    unittest.main()
