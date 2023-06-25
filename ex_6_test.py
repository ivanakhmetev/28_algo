from ex_6 import Deque
import collections

d2 = collections.deque()

deq = Deque()
# deq.addFront("f1")
# deq.addTail("t1")
# deq.addFront("f2")
# deq.addTail("t2")
# while deq.size() > 0:
#     print(deq.removeFront())
#     print(deq.removeTail())


RANGE = 3000

def test_af():
    for el in range(RANGE):
        is_flag = el in deq.array
        size = deq.size()        
        deq.addFront(el)
        assert size + 1 == deq.size()
        assert (is_flag) != (el in deq.array)

def test_af2():
    for el in range(RANGE):
        is_flag = el in d2
        size = len(d2)      
        d2.appendleft(el)
        assert size + 1 == len(d2)
        assert (is_flag) != (el in d2)

def test_at():
    for el in range(RANGE):
        is_flag = el in deq.array
        size = deq.size()        
        deq.addTail(el)
        assert size + 1 == deq.size()
        assert (is_flag) != (el in deq.array)

def test_at2():
    for el in range(RANGE):
        is_flag = el in d2
        size = len(d2)      
        d2.append(el)
        assert size + 1 == len(d2)
        assert (is_flag) != (el in d2)


def test_rt():
    for el in reversed(range(RANGE)):
        is_flag = el in deq.array
        size = deq.size()        
        deq.removeTail()
        assert size - 1 == deq.size()
        assert (is_flag) != (el in deq.array)

def test_rt2():
    for el in reversed(range(RANGE)):
        is_flag = el in d2
        size = len(d2)     
        d2.pop()
        assert size - 1 == len(d2)
        assert (is_flag) != (el in d2)

def test_rf():
    for el in range(RANGE):
        is_flag = el in deq.array
        size = deq.size()        
        deq.removeFront()
        assert size - 1 == deq.size()
        assert (is_flag) != (el in deq.array)

def test_rf2():
    for el in reversed(range(RANGE)):
        is_flag = el in d2
        size = len(d2)     
        d2.popleft()
        assert size - 1 == len(d2)
        assert (is_flag) != (el in d2)

def is_palindrome(text: str):
    d1 = Deque()
    d2 = Deque()
    for el in text:
        d1.addFront(el)
        d2.addTail(el)
    for i in range(len(text)):
        if d1.removeTail() != d2.removeTail():
            return False
    return True

print(is_palindrome('alkla'))

# test_af2()
# test_at2()
# test_rt()
# test_rf2()
# test_rt2()
# print(1 != 0 in [0])


