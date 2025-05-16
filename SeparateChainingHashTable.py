from UniqueLinkedList import UniqueLinkedList

class SeparateChainingHashTable:
    def __init__(self, MINBUCKETS=2, MINLOADFACTOR=0.5, MAXLOADFACTOR=1.5):
        self.MINBUCKETS = MINBUCKETS
        self.MINLOADFACTOR = MINLOADFACTOR
        self.MAXLOADFACTOR = MAXLOADFACTOR
        self.buckets = [UniqueLinkedList() for i in range(MINBUCKETS)]
        self.size = 0

    def __len__(self):
        return self.size
    
    def __setitem__(self, key, value):
        bu_i = hash(key) % len(self.buckets)
        add = self.buckets[bu_i].add(key, value)
        if add:
           self.size += 1
        if self.get_loadfactor() > self.MAXLOADFACTOR:
           raise ValueError("Load factor is too high")

    def __getitem__(self, key):
        bu_in = hash(key) % len(self.buckets)
        return self.buckets[bu_in].get(key)

    def __contains__(self, key):
        bucket_in = hash(key) % len(self.buckets)
        return self.buckets[bucket_in].__contains__(key)

    def pop(self, key):
        bucket_ind = hash(key) % len(self.buckets)
        value = self.buckets[bucket_ind].remove(key)
        if value is not None:
           self.size -= 1
        else:
           raise KeyError("Key not found")
        return value

    def get_loadfactor(self):
        return self.size/len(self.buckets)