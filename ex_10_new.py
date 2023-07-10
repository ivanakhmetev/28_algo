class PowerSet:
    def __init__(self):
        self.table = dict()
        self.count = 0

    def size(self):
        return self.count

    def get(self, value):
        item = self.table.get(value)
        if item is not None:
            return True
        return False

        # for i in range(self.count):
        #     if self.table[i] == value:
        #         return True
        # return False
    
    def remove(self, value):
        for i in range(self.count):
            if self.table[i] == value:
                self.table.pop(i)
                self.count -= 1
                return True
        return False
    
    def put(self, value):
        if self.get(value) == False:
            self.table[value] = value
            self.count += 1

        # if self.get(value) == False:
        #     self.table.append(value)
        #     self.count += 1

    def intersection(self, set2):
        i_set = PowerSet()
        values = self.table.values()
        for val in values:
            if set2.get(val) == True:
                i_set.put(val)

        # for i in range(self.count):
        #     if set2.get(self.table[i]) == True:
        #         i_set.put(self.table[i])
        return i_set

    def union(self, set2):
        i_set = PowerSet()
        values = self.table.values()
        for val in values:
            i_set.put(val)
        values = set2.table.values()
        for val in values:
            i_set.put(val)
        # for i in range(self.size()):
        #     i_set.put(self.table[i])
        # for i in range(set2.size()):
        #     i_set.put(set2.table[i])
        return i_set
    
    def difference(self, set2):
        i_set = PowerSet()
        values = self.table.values()
        for val in values:
            if set2.get(val) == False:
                i_set.put(val)
        # for i in range(self.size()):
        #     if set2.get(self.table[i]) == False:
        #         i_set.put(self.table[i])
        return i_set
    
    def issubset(self, set2):
        values = set2.table.values()
        for val in values:
                if self.get(val) == False:
        # for i in range(set2.size()):
        #     if self.get(set2.table[i]) == False:
                    return False
        return True








    
    
