from ex_4 import Stack, is_balanced

st = Stack()

def test_push():
    for i in range(21):
        st.push(i)

# st.stack.print_elements()
def test_peek():
    for i in range(20):
        print(st.peek())

def test_size():
    print(st.size())
    for i in range(20, 30):
        st.push(i)
    print(st.size())

def test_pop():
    # for i in range(30):
    while st.size() > 0:
        print(st.pop())
        print(st.pop())

# test_push()
# test_peek()
# test_size()
# test_pop()
arrays = ['(())', "(()((())()))", "(()()(()", "())(", "))((", "((())"]

for el in arrays:
    print(el)
    print(is_balanced(el))

