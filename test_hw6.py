import unittest
import random
from hw6 import bubble_sort, selection_sort, insertion_sort

class TestSortingAlgorithms(unittest.TestCase):
    def test_bubble_sort(self):
        # Test cases
        test_cases = [
            ([], 0),
            ([1, 2, 3, 4, 5], 0),
            ([5, 4, 3, 2, 1], 10),
            ([3, 2, 5, 1, 4], 5),
        ]
        # Testing
        for arr, expected_swaps in test_cases:
            with self.subTest(arr=arr, expected_swaps=expected_swaps):
                _, swaps = bubble_sort(arr)
                self.assertEqual(swaps, expected_swaps)

    def test_selection_sort(self):
        # Test cases
        test_cases = [
            ([], 0),
            ([1, 2, 3, 4, 5], 0),
            ([5, 4, 3, 2, 1], 4),
            ([3, 2, 5, 1, 4], 3),
        ]
        # Testing
        for arr, expected_swaps in test_cases:
            with self.subTest(arr=arr, expected_swaps=expected_swaps):
                _, swaps = selection_sort(arr)
                self.assertEqual(swaps, expected_swaps)

    def test_insertion_sort(self):
        # Test cases
        test_cases = [
            ([], 0),
            ([1, 2, 3, 4, 5], 0),
            ([5, 4, 3, 2, 1], 10),
            ([3, 2, 5, 1, 4], 3),
        ]
        # Testing
        for arr, expected_swaps in test_cases:
            with self.subTest(arr=arr, expected_swaps=expected_swaps):
                _, swaps = insertion_sort(arr)
                self.assertEqual(swaps, expected_swaps)

if __name__ == '__main__':
    unittest.main()