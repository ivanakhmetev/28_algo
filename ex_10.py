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
            

class PowerSet(HashTable):

    def __init__(self):
        super().__init__(20011, 19)

    def size(self):
        return sum([1 for el in self.slots if el is None])

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        start_slot = slot  
        while self.slots[slot] is not None:
            slot = (slot + self.step) % self.size
            if slot == start_slot:
                return slot
        return slot

    def put(self, value):
        self.slots[self.seek_slot(value)] = value

    def get(self, value):
        return self.slots[self.seek_slot(value)]
        # slot = self.hash_fun(value)
        # start_slot = slot  
        # return False

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        return False

    def intersection(self, set2):
        # пересечение текущего множества и set2
        return None 

    def union(self, set2):
        # объединение текущего множества и set2
        return None

    def difference(self, set2):
        # разница текущего множества и set2
        return None

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        return False