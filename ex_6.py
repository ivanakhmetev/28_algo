class Deque:
    def __init__(self):
        self.count = 0
        self.array = []

    def addFront(self, item):
        self.array.append(item)
        self.count += 1

    def addTail(self, item):
        self.array.insert(0, item)
        self.count += 1
        
    def removeFront(self):
        if self.count == 0:
            return None
        self.count -= 1
        return self.array.pop()

    def removeTail(self):
        if self.count == 0:
            return None
        self.count -= 1
        return self.array.pop(0)

    def size(self):
        return self.count