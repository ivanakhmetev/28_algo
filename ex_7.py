class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        if v1 > v2:
            return 1
        
    # def binary_search(self, value):
    #     left = 0
    #     right = self.len() - 1
    #     print(left, right)
    #     while left < right:
    #         middle = (left + right) / 2
    #         compare = self.compare(self[middle], value) 
    #         if compare == 0:
    #             return middle
    #         if compare < 0:
    #             right = middle - 1
    #         if compare > 0:
    #             left = middle + 1
    #     return None
        
    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        if self.__ascending:
            node = self.head
            while node.next is not None and self.compare(node.value, value) == -1:
                node = node.next
            if node.next == None:
                node.next = new_node
                new_node.prev = node.next
                self.tail = new_node
                return
            if node.next != None:
                new_node.prev = node
                new_node.next = node.next
                node.next.prev = new_node
                node.next = new_node
                return

        if not self.__ascending:
            node = self.tail
            while node.prev is not None and self.compare(node.value, value) == -1:
                node = node.prev
            if node.prev == None:
                node.prev = new_node
                new_node.next = node
                self.head = new_node
                return
            if node.prev != None:
                new_node.prev = node
                new_node.next = node.next
                node.next.prev = new_node
                node.next = new_node
                return


    def find(self, val):
        return None # здесь будет ваш код

    def delete(self, val):
        pass # здесь будет ваш код

    def clean(self, asc):
        self.__init__(asc)

    def __getitem__(self, idx):
        i = 0
        node = self.head
        while i != idx and node is not None:
            node = node.next
            i += 1
        if node is None:
            raise IndexError("Index out of range!")
        return node.value

    def len(self):
        node = self.head
        i = 0
        if self.head == self.tail:
            return 1
        while node.next is not None :
            node = node.next
            i += 1
        return i

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        # переопределённая версия для строк
        return 0