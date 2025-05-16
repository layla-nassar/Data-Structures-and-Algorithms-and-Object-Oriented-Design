import unittest 
from remove_characters import remove_characters 

class TestRemoveCharacters(unittest.TestCase):
    def test_remove_characters(self): 
        'tests the function remove_characters'
        test_remove = remove_characters('reilly', 'l')
        rem_str = 'reiy'
        self.assertEqual(test_remove, rem_str)