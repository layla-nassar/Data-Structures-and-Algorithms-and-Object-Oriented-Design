import unittest
from SeparateChainingHashTable import SeparateChainingHashTable
from LinearProbingHashTable import LinearProbingHashTable

class TestHashTableFactory:
    def create_hash_table(self):
        raise NotImplementedError("create_hash_table method not implemented.")

    def run_tests(self, hash_table):
        hash_table[1] = 'one'
        hash_table[2] = 'two'

        self.assertEqual(hash_table[1], 'one')
        self.assertEqual(hash_table[2], 'two')
        self.assertTrue(1 in hash_table)
        self.assertTrue(2 in hash_table)
        self.assertFalse(3 in hash_table)

        self.assertEqual(hash_table.pop(1), 'one')
        self.assertFalse(1 in hash_table)
        with self.assertRaises(KeyError):
            hash_table.pop(1)

        self.assertEqual(hash_table.get_loadfactor(), 0.5)

class TestSeparateChainingHashTable(TestHashTableFactory, unittest.TestCase):
    def create_hash_table(self):
        return SeparateChainingHashTable()

    def test_separate_chaining_hash_table(self):
        hash_table = self.create_hash_table()
        self.run_tests(hash_table)

class TestLinearProbingHashTable(TestHashTableFactory, unittest.TestCase):
    def create_hash_table(self):
        return LinearProbingHashTable()

    def test_linear_probing_hash_table(self):
        hash_table = self.create_hash_table()
        self.run_tests(hash_table)

if __name__ == '__main__':
    unittest.main()