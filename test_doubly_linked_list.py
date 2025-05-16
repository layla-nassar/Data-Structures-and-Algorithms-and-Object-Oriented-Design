import unittest
from doublylinkedlist import Node, DoublyLinkedList

class TestNode(unittest.TestCase):
    def test_init(self):
        node = Node(1)
        self.assertEqual(node.data, 1)
        self.assertIsNone(node.prev)
        self.assertIsNone(node.next)

    def test_eq(self):
        self.assertEqual(Node(1), Node(1))

    def test_repr(self):
        self.assertEqual(repr(Node(1)), "Node(1)")

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.empty_list = DoublyLinkedList()
        self.list_with_initial_values = DoublyLinkedList(range(10))

    def test_init_empty(self):
        self.assertIsNone(self.empty_list.head)
        self.assertIsNone(self.empty_list.tail)
        self.assertEqual(len(self.empty_list), 0)

    def test_init_starting_vals(self):
        self.assertEqual(len(self.list_with_initial_values), 10)
        self.assertEqual(self.list_with_initial_values.head.data, 0)
        self.assertEqual(self.list_with_initial_values.tail.data, 9)

    def test_add_first(self):
        self.empty_list.add_first(1)
        self.assertEqual(self.empty_list.head.data, 1)
        self.assertEqual(self.empty_list.tail.data, 1)
        self.assertEqual(len(self.empty_list), 1)

    def test_add_last(self):
        self.empty_list.add_last(1)
        self.assertEqual(self.empty_list.head.data, 1)
        self.assertEqual(len(self.empty_list), 1)

    def test_remove_first(self):
        self.list_with_initial_values.remove_first()
        self.assertEqual(len(self.list_with_initial_values), 9)
        self.assertEqual(self.list_with_initial_values.head.data, 1)

    def test_remove_last(self):
        self.list_with_initial_values.remove_last()
        self.assertEqual(len(self.list_with_initial_values), 9)
        self.assertEqual(self.list_with_initial_values.tail.data, 8)

    def test_add_remove_combination(self):
        self.empty_list.add_first(1)
        self.empty_list.add_last(2)
        self.assertEqual(self.empty_list.remove_first(), 1)
        self.assertEqual(len(self.empty_list), 1)
        self.empty_list.remove_last()
        self.assertEqual(len(self.empty_list), 0)

    def test_errors(self):
        with self.assertRaises(Exception) as context:
            self.empty_list.remove_first()
        self.assertTrue('List is empty' in str(context.exception))
        
        with self.assertRaises(Exception) as context:
            self.empty_list.remove_last()
        self.assertTrue('List is empty' in str(context.exception))

if __name__ == '__main__':
    unittest.main()

