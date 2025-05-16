import unittest
from magicsort import MagicCase, linear_scan, reverse_list, magic_insertionsort, magic_mergesort, magic_quicksort, magicsort

class TestLinearScan(unittest.TestCase):

    def test_sorted_list(self):
        input_list = [1, 2, 3, 4, 5]
        expected_output = MagicCase.SORTED
        result = linear_scan(input_list)
        self.assertEqual(result, expected_output)

    def test_reverse_sorted_list(self):
        input_list = [5, 4, 3, 2, 1]
        expected_output = MagicCase.REVERSE_SORTED
        result = linear_scan(input_list)
        self.assertEqual(result, expected_output)

    def test_constant_num_inversions_list(self):
        input_list = [20, 12, 3, 2, 4, 7, 6, 0, 11, 9, 5]
        expected_output = MagicCase.CONSTANT_NUM_INVERSIONS
        result = linear_scan(input_list)
        self.assertEqual(result, expected_output)


class TestReverseList(unittest.TestCase):

    def test_reverse_list(self):
        # Test reverse_list function with a sample input
        input_list = [1, 2, 3, 4, 5]
        expected_output = [5, 4, 3, 2, 1]
        result = reverse_list(input_list)
        self.assertEqual(result, expected_output)


class TestMagicInsertionSort(unittest.TestCase):

    def test_magic_insertionsort(self):
        # Test magic_insertionsort function with different input lists
        input_lists = [
            ([4, 3, 2, 1], [1, 2, 3, 4]),
            ([5, 2, 7, 1, 3], [1, 2, 3, 5, 7]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([], [])
        ]
        for input_list, expected_output in input_lists:
            result = magic_insertionsort(list(input_list), 0, len(input_list))
            self.assertEqual(result, expected_output)


class TestMagicMergeSort(unittest.TestCase):

    def test_magic_mergesort(self):
        # Test magic_mergesort function with different input lists
        input_lists = [
            ([4, 3, 2, 1], [1, 2, 3, 4]),
            ([5, 2, 7, 1, 3], [1, 2, 3, 5, 7]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([], [])
        ]
        for input_list, expected_output in input_lists:
            result = magic_mergesort(list(input_list), 0, len(input_list))
            self.assertEqual(result, expected_output)


class TestMagicQuickSort(unittest.TestCase):

    def test_magic_quicksort(self):
        # Test magic_quicksort function with different input lists
        input_lists = [
            ([4, 3, 2, 1], [1, 2, 3, 4]),
            ([5, 2, 7, 1, 3], [1, 2, 3, 5, 7]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([], [])
        ]
        for input_list, expected_output in input_lists:
            result = magic_quicksort(input_list, 0, len(input_list))
            self.assertEqual(input_list, expected_output)


class TestMagicSort(unittest.TestCase):

    def test_magicsort(self):
        # Test magicsort function with different input lists
        input_lists = [
            ([4, 3, 2, 1], [1, 2, 3, 4]),
            ([5, 2, 7, 1, 3], [1, 2, 3, 5, 7]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([], [])
        ]
        for input_list, expected_output in input_lists:
            result = magicsort(list(input_list))
            self.assertEqual(result, set())

# Run the tests
if __name__ == '__main__':
    unittest.main()