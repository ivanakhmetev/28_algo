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
        
    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            if self.__ascending and self.compare(value, current.value) < 0:
                return None
            if not self.__ascending and self.compare(value, current.value) > 0:
                return None
            current = current.next
        return None

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        if self.__ascending and self.compare(value, self.head.value) <= 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return            
        if self.__ascending and  self.compare(value, self.tail.value) >= 0:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            return
        if self.__ascending:
            current = self.head
            while current.next and self.compare(value, current.next.value) > 0:
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next = new_node
            return
        if not self.__ascending and self.compare(value, self.head.value) >= 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return 
        if not self.__ascending and self.compare(value, self.tail.value) <= 0:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            return
        if not self.__ascending:
            current = self.head
            while current.next and self.compare(value, current.next.value) < 0:
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next = new_node
            return
        
    def delete(self, val):
        if self.head is None:
            return
        if self.head.value == val and self.head.next is None:
            self.__init__(self.__ascending)
            return
        if self.head.value == val and self.head.next:
            self.head = self.head.next
            self.head.prev = None
            return
        current = self.head
        while current.next:
            if current.next.value == val and current.next.next:
                current.next.next.prev = current
                current.next = current.next.next
                return
            if current.next.value == val and current.next.next is None:
                self.tail = current
                self.tail.next = None
                return
            current = current.next

    def clean(self, asc):
        self.__init__(asc)

    def len(self):
        node = self.head
        i = 0
        while node is not None :
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

    def get_values(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        if v1 > v2:
            return 1