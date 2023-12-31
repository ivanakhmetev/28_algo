import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        new_array = self.make_array(self.capacity)
        for idx in range(i):
            new_array[idx] = self.array[idx]
        new_array[i] = itm
        for idx in range(i, self.count):
            new_array[idx + 1] = self.array[idx]
        self.array = new_array
        self.count += 1

    def print_elements(self):
        for i in range(self.count):
            print(self.array[i])
        
    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        if self.count - 1 < self.capacity / 2 and int(self.capacity / 1.5) < 16:
            self.resize(16)
        if self.count - 1 < self.capacity / 2 and int(self.capacity / 1.5) >= 16:
            self.resize(int(self.capacity / 1.5))
        new_array = self.make_array(self.capacity)
        for idx in range(i):
            new_array[idx] = self.array[idx]
        for idx in range(i + 1, self.count ):
            new_array[idx - 1] = self.array[idx]
        self.array = new_array
        self.count -= 1
        
