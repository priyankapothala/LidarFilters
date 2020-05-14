import unittest
import numpy as np
from filters.filters import TemporalMedianFilter


class TestFilter(unittest.TestCase):
    def test_empty_input(self):
        """
        Test on an empty array
        """
        data = []
        filter = TemporalMedianFilter()
        result = filter.update(data)
        self.assertEqual(result, [])

    def test_negative_previous_scans(self):
        """
        Tests if the previous scans D is greater than or equal to 0
        """
        with self.assertRaises(ValueError):
            TemporalMedianFilter(-2)

    def test_valid_previous_scan_integer_type(self):
        """
        Tests if the previous scans D is a valid integer
        """
        with self.assertRaises(ValueError):
            TemporalMedianFilter(2.3)

    def test_valid_previous_scan_str(self):
        """
        Tests if the previous scans D is a valid integer
        """
        with self.assertRaises(ValueError):
            TemporalMedianFilter('a')

    def test_no_previous_scans(self):
        """
        Tests the temporal median filter with no previous scans
        """
        filter = TemporalMedianFilter(0)
        arr = [[0.0, 1.0, 2.0, 1.0, 3.0], [1.0, 5.0, 7.0, 1.0, 3.0], [
            2.0, 3.0, 4.0, 1.0, 0.0], [3.0, 3.0, 3.0, 1.0, 3.0], [10.0, 2.0, 4.0, 0.0, 0.0]]
        for i in range(len(arr)):
            result = filter.update(arr[i])
            self.assertEqual(result, arr[i])

    def test_three_previous_scans(self):
        """
        Tests the temporal median filter with 3 previous scans
        """
        filter = TemporalMedianFilter(3)
        input_scan = [[0.0, 1.0, 2.0, 1.0, 3.0], [1.0, 5.0, 7.0, 1.0, 3.0], [
            2.0, 3.0, 4.0, 1.0, 0.0], [3.0, 3.0, 3.0, 1.0, 3.0], [10.0, 2.0, 4.0, 0.0, 0.0]]
        expected_result = [[0.0, 1.0, 2.0, 1.0, 3.0], [0.5, 3.0, 4.5, 1.0, 3.0], [
            1.0, 3.0, 4.0, 1.0, 3.0], [1.5, 3.0, 3.5, 1.0, 3.0], [2.5, 3.0, 4.0, 1.0, 1.5]]
        for i in range(len(input_scan)):
            result = filter.update(input_scan[i])
            self.assertEqual(result, expected_result[i])

    def test_inconsistent_scan_length(self):
        """
        Tests the temporal median filter with inconsistent scan length
        """
        filter = TemporalMedianFilter(3)
        input_scan = [[0.0, 1.0, 2.0, 1.0, 3.0], [1.0, 5.0, 7.0, 1.0]]
        filter.update(input_scan[0])
        with self.assertRaises(ValueError):
            filter.update(input_scan[1])


if __name__ == '__main__':
    unittest.main()
