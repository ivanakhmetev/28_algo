class NativeDictionary:

    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        h_sum = 0
        h_pow = 1
        m = 10**9 + 9
        p = 31
        for el in key:
            h_sum = (h_sum + (ord(el) - ord('a') + 1)*h_pow) % m
            h_pow = h_pow * p % m
        return h_sum % self.size    

    def put(self, key, value):
        hash_key = self.hash_fun(key)
        self.slots[hash_key] = key
        self.values[hash_key] = value

    def is_key(self, key):
        if key in self.slots:
            return True
        return False

    def get(self, key):
        if self.is_key(key):
            return self.values[self.hash_fun(key)]
        return None
    
    def space_left(self):
        return sum([1 for el in self.values if el is None])

