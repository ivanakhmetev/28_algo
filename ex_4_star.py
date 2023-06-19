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
        

class Stack:
    def __init__(self):
        self.stack = DynArray()

    def size(self):
        return len(self.stack)

    # def pop(self):
    #     if self.size() == 0:
    #         return None
    #     top_element = self.stack[self.stack.count - 1]
    #     self.stack.delete(self.stack.count - 1)
    #     return top_element

    def pop(self):
        if self.size() == 0:
            return None
        top_element = self.stack[0]
        self.stack.delete(0)
        return top_element

    # def push(self, value):
    #     self.stack.append(value)

    def push(self, value):
        self.stack.insert(0, value)

    # def peek(self):
    #     if self.size() == 0:
    #         return None
    #     return self.stack[self.stack.count - 1]

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[0]

BRACES = ['(())', "(()((())()))", "(()()(()", "())(", "))((", "((())"]

def is_balanced(braces: str):
    if len(braces) % 2 != 0:
        return False
    stack = Stack()
    for brace in braces:
        if brace == '(':
            stack.push(brace)
        try:
            last_element = stack.peek()
        except:
            last_element = None
        if brace == ')' and last_element == '(':
            stack.pop()
        if last_element is None:
            return False
    return True
    
# EXP = '1 2 + 3 * ='
EXP = '8 2 + 5 * 9 + = '

def parse_postfix(expression: str):
    src_stack = Stack()
    for el in expression[::-1]:
        if el.isdigit():
            src_stack.push(el)
        if el == ' ':
            pass
        if el == '+':
            src_stack.push('+')
        if el == '*':
            src_stack.push('*')
        if el == '=':
            src_stack.push('=')
    return src_stack

def ex_postfix(expression: str):
    src_stack = parse_postfix(expression)
    ex_stack = Stack()
    while src_stack.size() > 0:
        el = src_stack.pop()
        if el == '=':
            print(ex_stack.peek())
        if el == '*':
            ex_stack.push(ex_stack.pop() * ex_stack.pop())
        if el == '+':
            ex_stack.push(ex_stack.pop() + ex_stack.pop())
        if el.isdigit():
            ex_stack.push(int(el))        

ex_postfix(EXP)

