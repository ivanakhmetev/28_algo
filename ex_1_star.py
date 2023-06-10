def sum_lists(linked1, linked2):
    l1 = linked1.len()
    l2 = linked2.len()
    if l1 != l2:
        return

    rtn = LinkedList()
    node1 = linked1.head
    node2 = linked2.head
    while node1 is not None:
        rtn.add_in_tail(Node(node1.value + node2.value))
        node1 = node1.next
        node2 = node2.next
    return rtn
    

class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
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
        node = self.head
        nodes = []
        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

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
                if not all:
                    return
        
        prev_node = None
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value == val:
                if curr_node == self.tail:
                    self.tail = prev_node
                if prev_node is not None:
                    prev_node.next = curr_node.next
                curr_node = curr_node.next
                if not all:
                    return
            else:
                prev_node = curr_node
                curr_node = curr_node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        list_len = 0
        node = self.head
        while node is not None:
            list_len += 1
            node = node.next
        return list_len

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None:
                self.add_in_tail(newNode)
            else:
                newNode.next = self.head
                self.head = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
            if afterNode == self.tail:
                self.tail = newNode

