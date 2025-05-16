import unittest 
from any_two_sum import any_two_sum

class TestAnyTwoSum(unittest.TestCase):
     def test_any_two_sum(self):
        'tests the function any_two_sum'
        test_sum = any_two_sum([1,3,4,5], 7)
        test_sum_2 = any_two_sum([3,9,6], 14)
        booleen = True 
        self.assertEqual(test_sum, booleen)
        self.assertNotEqual(test_sum_2, booleen)
