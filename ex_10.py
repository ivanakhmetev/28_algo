class HashTable:
    def __init__(self, sz, stp):
        self.sz = sz
        self.step = stp
        self.slots = [None] * self.sz

    def hash_fun(self, value):
        h_sum = 0
        h_pow = 1
        m = 10**9 + 9
        p = 31
        for el in value:
            h_sum = (h_sum + (ord(el) - ord('a') + 1)*h_pow) % m
            h_pow = h_pow * p % m
        return h_sum % self.sz

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        start_slot = slot  
        while self.slots[slot] is not None:
            slot = (slot + self.step) % self.sz
            if slot == start_slot:
                return None
        return slot

    def put(self, value):
        slot = self.seek_slot(value)
        if slot is not None:
            self.slots[slot] = value
            return slot
        return None

    def find(self, value):
        slot = self.hash_fun(value)
        start_slot = slot  
        while self.slots[slot] is not None:
            if self.slots[slot] == value:
                return slot
            slot = (slot + self.step) % self.sz
            if slot == start_slot:
                return None
            

class PowerSet(HashTable):

    def __init__(self):
        super().__init__(20011, 19)

    def size(self):
        return sum([1 for el in self.slots if el is not None])

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        start_slot = slot  
        while self.slots[slot] is not None:
            slot = (slot + self.step) % self.sz
            if slot == start_slot:
                return slot
        return slot

    def put(self, value):
        if self.get(value):
            return
        self.slots[self.seek_slot(value)] = value

    def get(self, value):
        return bool(self.find(value))

    def remove(self, value):
        slot = self.find(value)
        if slot is not None:
            self.slots[slot] = None
            return True
        return False
    
    def get_all(self):
        return [el for el in self.slots if el is not None]

    def intersection(self, set2):
        new_set = PowerSet()
        elems_1 = self.get_all()
        elems_2 = set2.get_all()
        for el in elems_1:
            if set2.get(el):
                new_set.put(el)
        for el in elems_2:
            if self.get(el):
                new_set.put(el)
        return new_set

    def union(self, set2):
        new_set = PowerSet()
        elems_1 = self.get_all()
        elems_2 = set2.get_all()
        for el in elems_1:
            new_set.put(el)
        for el in elems_2:
            new_set.put(el)
        return new_set

    def difference(self, set2):
        new_set = PowerSet()
        elems_1 = self.get_all()
        for el in elems_1:
            if set2.get(el) == False:
                new_set.put(el)
        return new_set


    def issubset(self, set2):
        elems_2 = set2.get_all()
        for el in elems_2:
            if not self.get(el):
                return False
        return True