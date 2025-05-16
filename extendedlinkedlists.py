from linkedlist import Node, LinkedList # get linkedlist.py from lab
 
# Create the classes for this assignment below.
class ReversableLinkedList(LinkedList):
    def reverse(self):
        """This functions goal is to reverse a linked list."""
        old_head = self._head
        prev_node = None
        curr_node = self._head
        next_node = None
        while curr_node is not None:
            next_node = curr_node.link
            curr_node.link = prev_node
            prev_node = curr_node
            curr_node = next_node
        self._head = prev_node
        self._tail = old_head
        self._tail.link = None
class SortedLinkedList(LinkedList):
    def add_first(self, item):
        """This functions objective overwrites the add_first method from the parent class to raise an error."""
        raise NotImplementedError(f"Useadd_sorted({item})instead")
   
    def add_last(self, item):
        """This function will overwrite the add_last method from the parent class to raise an error."""
        raise NotImplementedError(f"Useadd_sorted({item})instead")
   
    def add_sorted(self, item):
        """This function adds items to a linked list in sorted order."""
        new_node = Node(item)
        if self._head is None or self._head.item > item:
            new_node.link = self._head
            self._head = new_node
            self._len += 1
        else:
            current_node = self._head
            while current_node.link is not None and current_node.link.item < item:
                current_node = current_node.link
            new_node.link = current_node.link
            current_node.link = new_node
            self._len += 1
       
class UniqueLinkedList(LinkedList):
    def remove_dups(self):
        """This function will remove duplicate items from a linked list and returns a dictionary representing how many copies of each item were removed."""
        items = {}
        current_node = self._head
        prev_node = None
        while current_node is not None:
            if current_node.item not in items:
                items[current_node.item] = 0
                prev_node = current_node
                current_node = current_node.link
            else:
                items[current_node.item] += 1
                prev_node.link = current_node.link
                current_node = current_node.link
                self._len -= 1
        return items
       
test = SortedLinkedList()
test.add_sorted(5)
test.add_sorted(3)
test.add_sorted(2)
test.add_sorted(1)
test.add_sorted(4)
test.add_sorted(6)
test.add_sorted(10)
test.add_sorted(8)
test.add_sorted(0)
test.add_sorted(9)
test.add_sorted(7)
while test:
    print(test.remove_first())