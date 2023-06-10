from ex_1 import LinkedList, Node

values = [13, 12, 55, 13, 128, 'str', 13, 13, 13]
values_2 = [12, 55, 128, 'str', 11]
s_list = LinkedList()

for el in values:
    n = Node(el)
    s_list.add_in_tail(n)

def test_find(value):
    n = s_list.find(value)
    if n is not None:
        print(n.value)

def test_find_prev(value):
    n = s_list.find_prev(value)
    if n is not None:
        print(n.value)

def test_find_next(value):
    n = s_list.find_next(value)
    if n is not None:
        print(n.value)

def test_delete(value):
    n = s_list.delete(value)
    s_list.print_all_nodes()

def test_delete_all(value):
    a = list(reversed(values))
    # a = values
    r_list = LinkedList()

    for el in a:
        n = Node(el)
        r_list.add_in_tail(n)
    r_list.print_all_nodes() 
    print('....')
    r_list.delete(value, True)
    r_list.print_all_nodes() 

def test_clean():
    s_list.print_all_nodes()
    s_list.clean()
    s_list.print_all_nodes()

def test_find_all():
    for el in values:
        finds = s_list.find_all(el)
        for el in finds:
            print(el.value)

def test_val():
    s_list.add_in_tail(Node(50))
    s_list.add_in_tail(Node(50))
    print('target', 50)
    test_delete(None)
    # s_list.print_all_nodes()
    for el in reversed(values):
        print('target', el)
        test_delete(el)
    print('target', 50)
    test_delete_all(50)
    print('target', 50)
    test_delete(50)
    print('target', None)
    test_delete(None)
    for el in reversed(values):
        print('target', el)
        test_delete(el)

def test_len():
    print(s_list.len())

def test_insert():
    a = Node('kk')
    b = Node('ww')
    c = Node('l')
    d = Node('beg')
    s_list.add_in_tail(a)
    s_list.add_in_tail(b)
    b = s_list.find_prev_node(b)
    s_list.insert(a, c)
    s_list.insert(None, d)
    s_list.print_all_nodes()

    # s_list.insert(s_list.find('aa'), Node(14))
    # s_list.print_all_nodes()

    
test_delete_all(13)
# test_insert()
# test_val()
# test_len()
# test_find_all()
# test_clean()
# print(values.clear())
# test_val()

