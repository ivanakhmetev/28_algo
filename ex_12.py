from functools import reduce

class NativeCache:

    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash(self, str1):
        return reduce(self._hash, str1, 0)

    def _hash(self, x, y):
        return (x * 17 + ord(y)) % self.size

    def put(self, key, value):
        idx = self.hash(key)        
        if self.slots[idx] == key:
            self.values[idx] = value
            self.hits[idx] += 1
            return
        if self.is_space() and self.slots[idx] != key:
            free_idx = self.slots.index(None)
            self.slots[free_idx] = key
            self.values[free_idx] = value
            self.hits[free_idx] = 1
            return        
        if not self.is_space() and self.slots[idx] != key:
            min_hits = min(self.hits)
            min_idx = self.hits.index(min_hits)
            self.slots[min_idx] = key
            self.values[min_idx] = value
            self.hits[min_idx] = 1
            return

    def is_key(self, key):
        return bool(self.slots[self.hash(key)] == key)

    def is_space(self):
        return bool(self.slots.count(None))

    def get(self, key):
        if self.is_key(key):
            idx = self.hash(key)
            self.hits[idx] += 1
            return self.values[idx]
        return None


