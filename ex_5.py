class Stack:
    def __init__(self):
        self.stack = []

    def __bool__(self):
        return bool(self.stack)

    def push(self, elem):
        if self.stack:
            self.stack.append((elem, min(elem, self.stack[-1][1])))
        else:
            self.stack.append((elem, elem))

    def pop(self):
        return self.stack.pop()[0]
    
    def len(self):
        return len(self.stack)
    
class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, elem):
        self.s1.push(elem)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.push(self.s1.pop())
        return self.s2.pop()
    
    def size(self):
        if self.s1.len() == 0 and self.s2.len() == 0:
            return 0
        if self.s1.len() == 0 and self.s2.len() != 0:
            return self.s2.len()
        if self.s1.len() != 0 and self.s2.len() == 0:
            return self.s1.len()
