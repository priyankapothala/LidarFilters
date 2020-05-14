import unittest
from filters.filters import RangeFilter


class TestFilter(unittest.TestCase):
    def test_valid_min_range(self):
        """
        Tests if the range_min is valid
        """
        with self.assertRaises(ValueError):
            RangeFilter(-1.0, 50)

    def test_valid_max_range(self):
        """
        Tests if the range_max is valid
        """
        with self.assertRaises(ValueError):
            RangeFilter(0, -5)

    def test_valid_range(self):
        """
        Tests if the range_max is greater than range_min
        """
        with self.assertRaises(ValueError):
            RangeFilter(5.0, 1.0)

    def test_empty_input(self):
        """
        Test on an empty array
        """
        data = []
        filter = RangeFilter()
        result = filter.update(data)
        self.assertEqual(result, [])

    def test_default_range(self):
        """
        Test with custom range_min and range_max
        """
        data = [0.1, 0.3, 0.02, 12, 67, 23, 50, 51, 0.0]
        filter = RangeFilter()
        result = filter.update(data)
        self.assertEqual(result, [0.1, 0.3, 0.03, 12, 50, 23, 50, 50, 0.03])

    def test_custom_range(self):
        """
        Test if the range filter crops values below range_min and above range_max
        """
        data = [0.1, 0.3, 0.02, 12, 67, 23, 50, 51, 0.0]
        filter = RangeFilter(0.05, 20)
        result = filter.update(data)
        self.assertEqual(result, [0.1, 0.3, 0.05, 12, 20, 20, 20, 20, 0.05])


if __name__ == '__main__':
    unittest.main()
