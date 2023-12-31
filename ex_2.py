class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        rtn = []
        node = self.head
        while node is not None:
            if node.value == val:
                rtn.append(node)
            node = node.next
        return rtn

    def delete(self, val, all=False):
        if self.head is None:
            return
        while self.head.value == val:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return
            else:
                self.head = self.head.next
                self.head.prev = None
                if not all:
                    return
        
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value == val:
                if curr_node.prev is not None and curr_node.next is not None:
                    curr_node.prev.next = curr_node.next
                    curr_node.next.prev = curr_node.prev
                if curr_node == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                curr_node = curr_node.next
                if not all:
                    return
            else:
                curr_node = curr_node.next



    def clean(self):
        self.__init__()

    def len(self):
        s_len = 0
        node = self.head
        while node is not None:
            s_len += 1
            node = node.next
        return s_len

    def insert(self, afterNode, newNode):
        if afterNode == None:
            if self.head == None:
                self.add_in_head(newNode)
            else:
                self.add_in_tail(newNode)
        else:
            if afterNode == self.tail:
                self.add_in_tail(newNode)
            else:
                newNode.prev = afterNode
                newNode.next = afterNode.next
                afterNode.next.prev = newNode
                afterNode.next = newNode        

    def add_in_head(self, newNode):
        if self.head == None:
            newNode.prev = None
            newNode.next = None
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            newNode.prev = None
        self.head = newNode