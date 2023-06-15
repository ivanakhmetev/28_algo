class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class DummyNode(Node):
    def __init__(self):
        super().__init__(None)


class DummyLinkedList2():
    def __init__(self):
        dummy = DummyNode()
        self.head = dummy
        self.tail = dummy
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, newNode):
        newNode.prev = self.tail.prev
        newNode.next = self.tail
        self.tail.prev.next = newNode
        self.tail.prev = newNode

    def add_in_head(self, newNode):
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode

    def print_all_nodes(self):
        node = self.head.next
        while not isinstance(node, DummyNode):
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head.next
        while not isinstance(node, DummyNode):
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        rtn = []
        node = self.head.next
        while not isinstance(node, DummyNode):
            if node.value == val:
                rtn.append(node)
            node = node.next
        return rtn
    
    def delete(self, val, all=False):
        node = self.head.next
        while not isinstance(node, DummyNode):
            if node.value == val and not all:
                node.prev.next = node.next
                node.next.prev = node.prev
                return
            if node.value == val and all:
                node.prev.next = node.next
                node.next.prev = node.prev
            node = node.next

    def clean(self):
        self.__init__()

    def len(self):
        s_len = 0
        node = self.head.next
        while not isinstance(node, DummyNode):
            s_len += 1
            node = node.next
        return s_len
        
    def insert(self, afterNode, newNode):
        if afterNode is None and isinstance(self.head.next, DummyNode):
            self.add_in_head(newNode)
        if afterNode is None and not isinstance(self.head.next, DummyNode):
            self.add_in_tail(newNode)
        if afterNode is not None:
            newNode.prev = afterNode
            newNode.next = afterNode.next
            afterNode.next.prev = newNode
            afterNode.next = newNode  
