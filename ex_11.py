from functools import reduce#, map

class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        # self.bit_array = self._gen_array0(f_len)
        self.bits = 9223372036854775807
        list(map(self.clear_bit, range(self.filter_len)))

    def hash1(self, str1):
        return reduce(self._hash1, str1, 0)

    def _hash1(self, x, y):
        return (x * 17 + ord(y)) % self.filter_len

    # def _gen_array0(self, len):
    #     return [bin(0)] * len

    def hash2(self, str1):
        return reduce(self._hash2, str1, 0)

    def _hash2(self, x, y):
        return (x * 223 + ord(y)) % self.filter_len

    # def _replace_bit(self, pos):
    #     self.bit_array[pos] = bin(1)

    def add(self, str1):
        # self._replace_bit(self.hash1(str1))
        # self._replace_bit(self.hash2(str1))
        self.set_bit(self.hash1(str1))
        self.set_bit(self.hash2(str1))

    # def _is_value(self, str1):
    #     if self.bit_array[self.hash1(str1)] == bin(1) and self.bit_array[self.hash2(str1)] == bin(1):
    #         return True
    #     return False
    
    def is_value(self, str1):
        pos1 = self.hash1(str1)
        pos2 = self.hash2(str1)
        if self.get_bit(pos1) == 1 and self.get_bit(pos2) == 1:
            return True
        return False
    
    def set_bit(self, bit):
        self.bits = self.bits | (1 << bit)

    def clear_bit(self, bit):
        self.bits = self.bits & ~(1 << bit)

    def get_bit(self, pos):
        rep = self.bit_representation()
        return rep[pos]

    def bit_representation(self):
        rep = []
        num = self.bits
        while num != 0:
            rep.append(num % 2)
            num = num // 2
        return rep

