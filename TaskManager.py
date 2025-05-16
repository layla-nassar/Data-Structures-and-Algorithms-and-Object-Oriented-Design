class Entry:
    """Represents an entry in the priority queue."""

    def __init__(self, priority, process_id):
        """Initializes an Entry object with a given priority and process ID."""
        self.priority = priority
        self.process_id = process_id

    def __repr__(self):
        """Returns a string representation of the Entry object."""
        return f"Entry(priority={self.priority}, process_id={self.process_id})"

    ####### Implement all Entry class methods under this line #######
    def __gt__(self, other):
        """Compares the priority of this entry with another entry.
        Returns:bool: True if this entry has higher priority than the other, False otherwise."""
        return self.priority > other.priority
        
    def __eq__(self, other):
        """Checks if this entry is equal to another entry based on priority.
        Returns:bool: True if the priorities are equal, False otherwise."""
        return self.priority == other.priority
        
class MaxHeap:
    """Represents a max heap data structure."""

    def __init__(self):
        """Initializes a MaxHeap object."""
        self._heap = []

    ####### Implement all MaxHeap class methods under this line #######
    def put(self, entry):
        """Inserts an entry into the max heap."""
        self._heap.append(entry)
        
    def remove_max(self):
        """Removes and returns the entry with the maximum priority from the max heap.
        Returns:The process ID that was removed from the queue. raise IndexError if the heap is empty"""
        if self._heap == []:
            raise IndexError
        max_priority = 0
        max_entry = None
        for entry in self._heap:
            if entry.priority > max_priority:
                max_priority = entry.priority
                max_entry = entry
        self._heap.remove(max_entry)
        return max_entry.process_id

    def change_priority(self, process_id, new_priority):
        """Changes the priority of a process in the max heap.
        Returns:bool: True if the priority change was successful, False otherwise."""
        for entry in self._heap:
            if entry.process_id == process_id:
                entry.priority = new_priority
                return True
        return False

    def _upheap(self, index):
        """Performs up-heap operation to maintain heap property after insertion."""
        parent_index = (index - 1) // 2
        while index > 0:
            if self._heap[index] > self._heap[parent_index]:
                self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            else:
                break

    def _downheap(self, index):
        """Performs down-heap operation to maintain heap property after removal."""
        while True:
            Lchild_index = 2 * index + 1
            Rchild_index = 2 * index + 2
            max_index = index
            
            if self._heap[index] < self._heap[Lchild_index]:
                max_index = Lchild_index
            if self._heap[index] < self._heap[Rchild_index]:
                max_index = Rchild_index
            
            if max_index != index:
                self._heap[index], self._heap[max_index] = self._heap[max_index], self._heap[index]
                index = max_index
            else:
                break

    def __len__(self):
        """len is number of items in PQ"""          
        return len(self._heap)

class TaskManager:
    """Manages the execution of processes using a priority queue."""

    def __init__(self):
        """Initializes a TaskManager object."""
        self.processor_queue = MaxHeap()
    
    ####### Implement all TaskManager class methods under this line #######
    def add_process(self, entry):
        """Adds a process to the processor queue."""
        self.processor_queue.put(entry)

    def remove_process(self):
        """Removes and returns the process with the highest priority from the processor queue."""
        return self.processor_queue.remove_max()

