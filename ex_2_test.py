from ex_2 import Node, LinkedList2

# class Node:
#     def __init__(self, v):
#         self.value = v
#         self.prev = None
#         self.next = None

# class LinkedList2:  
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def add_in_tail(self, item):
#         if self.head is None:
#             self.head = item
#             item.prev = None
#             item.next = None
#         else:
#             self.tail.next = item
#             item.prev = self.tail
#         self.tail = item

#     def find(self, val):
#         return None # здесь будет ваш код

    # def find_all(self, val):
    #     return [] # здесь будет ваш код

# 2.1. Добавьте в класс LinkedList2 метод поиска первого узла по его значению.
# find(val)

values = [1, 1, 2, 1, 2, 3, 'a', 'b', 17, 17]
s_list = LinkedList2()
for el in values:
    s_list.add_in_tail(Node(el))
print('original list:')
s_list.print_all_nodes()


def test_find():
    values_to_find = [1, -2, 3, 20, 17, 'a']
    for el in values_to_find:
        node = s_list.find(el)
        if el in values:
            assert node.value == el
        else:
            assert node == None

def test_find_all():
    values_to_find = [1, -2, 3, 20, 17, 'a']
    for el in values_to_find:
        nodes = s_list.find_all(el)
        if el in values:
            s_node = s_list.head
            while s_node is not None:
                if s_node.value == el:
                    assert s_node in nodes
                s_node = s_node.next
        else:
            assert len(nodes) == 0
        # print('found els', len(nodes))

    # def delete(self, val, all=False):
    #     pass # здесь будет ваш код

def test_delete():
    values_to_del = [1, -2, 3, 20, 17, 'a']
    for el in values_to_del:
        # if el in values:
        #     s_len = s_list.len()
        s_list.delete(el, True)
        # if el in values:
        #     assert s_list.len() == s_len - 1
    print('deleted')
    s_list.print_all_nodes()

        


# test_find()
# test_find_all()
test_delete()