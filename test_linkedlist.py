import unittest
from linkedlist import Node, LinkedList

class TestNode(unittest.TestCase):
    def test_init(self):
        node1 = Node('Jake')
        self.assertEqual(node1.item, 'Jake')
        self.assertEqual(node1.link, None)

    def test_repr(self):
        node_repr = Node('Bob')
        self.assertEqual(repr(node_repr), 'Node(Bob)')
        self.assertEqual(repr(Node(0)), 'Node(0)')


class TestLinkedList(unittest.TestCase):
    def test_init(self):
        L_L = LinkedList()
        self.assertEqual(len(L_L), 0)
        self.assertEqual(L_L.get_head, None)
        self.assertEqual(L_L.get_tail, None)
        LL1 = LinkedList(['a', 'b', 'c'])
        self.assertEqual(len(LL1), 3)
        self.assertEqual(LL1.get_head(), 'a')
        self.assertEqual(LL1.get_tail,'c')

    
    def testadd_last(self):
        L_L1 = LinkedList()
        for i in range(len(L_L1)):
            L_L1.append(i)
            self.assertEqual(len(L_L1), i+1)
            self.assertEqual(self.get_head(), L_L1[i])
            self.assertEqual(self.get_tail(), L_L1[-1-i])



    def testadd_first(self):
        L_L2 = LinkedList()
        for i in range(len(L_L2)):
            L_L2.append(i)
            self.assertEqual(len(L_L2), len(L_L2)-1)
            self.assertEqual(self.get_head(), L_L2[i])
            self.assertEqual(self.get_tail(), L_L2[-1])


    def testremove_first(self):
        ll = LinkedList([1,9,0,8,8,7])
        for i in range(len(ll)):
            ll.remove_first()
            self.assertEqual(ll.remove_first(), ll[i])
            self.assertEqual(len(ll), 6-(i+1))
            self.assertEqual(ll.get_head(), ll[i])
            self.assertEqual(ll.get_tail(), ll[-1-i])

    

    def testremove_last(self):
        ll = LinkedList([1,9,0,8,8,7])
        for i in range(len(ll)):
            ll.remove_last()
            self.assertEqual(ll.remove_last(), ll[-1])
            self.assertEqual(len(ll), 6-(i+1))
            self.assertEqual(ll.get_head(), ll[i])
            self.assertEqual(ll.get_tail(), ll[-1-i])