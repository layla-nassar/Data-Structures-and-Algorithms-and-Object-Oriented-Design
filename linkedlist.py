class Node:
    def __init__(self, item, link=None):
        'initialized all variables'
        self.item = item
        self.link = link

    def __eq__(self, node):
        if self.item == node.item:
            return True
        

    def __repr__(self):
        'returns a string node'
        return f'Node({self.item})'
    

class LinkedList(Node):
    def __init__(self, items= None):
        'initializes items '
        self.LL = Node(None)
        self._head = None
        self._tail = None
        self.len = 0
        if items is not None:
            for item in items:
                self.add_last(item)
        
    def __len__(self):
        'returns the length of the list'
        return self.len
    
    def get_head(self):
        'returns 1st item'
        return self._head.item if self._head else None
    
    def get_tail(self):
        'returns last item'
        return self._tail.item if self._tail else None
    
    def add_first(self, item= None):
        'adds a new item to the 1st index'
        #new_node = Node(item)
        #new_node.link = self.head
        #if self.len == 0: 
         #   return None
      #  else:
        self._head = Node(item, self._head)
        if self._tail is None:
            self._tail = self._head
        self.len +=1
        if self.len==1:
            self.tail = self._head

         

    def remove_first(self):
        'remove first item in list'
        if self.len == 0:
            raise RuntimeError
        item = self._head.item
        #save_head = self.head.item
        self._head = self._head.link
        if self._head is None: 
            self._tail = None
        self.len -= 1
        return item
        
       

    def add_last(self, item= None):
        'adds item to end of list'

        if self._head is None:
            self.add_first(item)
        else:
            self._tail.link = Node(item)
            self._tail = self._tail.link
            self.len +=1

  
    def remove_last(self):
        'remove last item in list'
        #if self._head is None:
         #   self.add_first(item)
        if self.len == 0:
            raise RuntimeError
        
        if self._head is self._tail:
            return self.remove_first()
        else:
        #save_last = self.tail.item
            current_node= self._head
            while current_node.link != self._tail:
                current_node = current_node.link
            item = self._tail.item
            self._tail = current_node
            self._tail.link = None
            self.len -= 1
            return item
        

bloop = Node(0)
print(repr(bloop))