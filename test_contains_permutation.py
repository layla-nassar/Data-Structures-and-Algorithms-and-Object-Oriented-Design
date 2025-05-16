import unittest 
from contains_permutation import contains_permutation

class TestContains_Permutation(unittest.TestCase):
     def test_contains_permutation(self):
        'tests function contains_permutation'
        self.pattern = 'sit'
        self.input_string = 'patriots'
        self.patternlen = len(self.pattern)
        self.input_stringlen = len(self.pattern)
        self.assertLess(self.patternlen, self.input_stringlen)
        
     def test_appropriate_self(self):
    # Check if the result is correct 
        self.pattern = 'sit'
        self.input_string = 'patriots'
        self.assertTrue(contains_permutation('patriots', 'sit'), "Expected True as 'sit' is a permutation present in 'patriots'")


     def test_input_types(self): 
        #to ensure None is no passed 
        self.pattern = 'sit' 
        self.input_string = 'patriots'
        self.assertNotEqual(self.pattern, None)
        self.assertNotEqual(self.input_string, None)

if __name__ == '__main__':
    unittest.main()



