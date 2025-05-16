from UniqueLinkedList import UniqueLinkedList

class LinearProbingHashTable:
    def __init__(self, MINBUCKETS=2, MINLOADFACTOR=0.1, MAXLOADFACTOR=0.9):
        self.MINLOADFACTOR = MINLOADFACTOR
        self.MAXLOADFACTOR = MAXLOADFACTOR
        self.size = MINBUCKETS
        self.keys = [None]*MINBUCKETS
        self.values = [None]*MINBUCKETS
        self.num_i = 0

    def __len__(self):
        return self.num_i

    def __setitem__(self, key, value):
        index = hash(key) % self.size
        while self.keys[index] is not None and self.keys[index] != key:
            index = (index+1)%self.size
        if self.keys[index] is None:
           self.num_i += 1
        self.keys[index] = key
        self.values[index] = value
        if self.get_loadfactor() > self.MAXLOADFACTOR:
           raise ValueError("Load factor is too high")

    def __getitem__(self, key):
        idx = hash(key) % self.size
        while self.keys[idx] is not None:
             if self.keys[idx] == key:
                return self.values[idx]
             idx = (idx + 1)%self.size
        raise KeyError(key)
    def __contains__(self, key):
        try:
           i = self[key]
           return True
        except KeyError:
           return False

    def pop(self, key):
        ix = hash(key) % self.size
        while self.keys[ix] is not None:
            if self.keys[ix] == key:
               value = self.values[ix]
               self.keys[ix] = None
               self.values[ix] = None
               self.num_i -= 1
               return value
            ix = (ix + 1) % self.size
        raise KeyError(key)

    def get_loadfactor(self):
        return self.num_i / self.size