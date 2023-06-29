class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        h_sum = 0
        h_pow = 1
        m = 10**9 + 9
        p = 31
        for el in value:
            h_sum = (h_sum + (ord(el) - ord('a') + 1)*h_pow) % m
            h_pow = h_pow * p % m
        return h_sum % self.size

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        start_slot = slot  
        while self.slots[slot] is not None:
            slot = (slot + self.step) % self.size
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
            slot = (slot + self.step) % self.size
            if slot == start_slot:
                return None