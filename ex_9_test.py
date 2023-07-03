from ex_9 import NativeDictionary

d = NativeDictionary(10)

for i in range(15):
    i = str(i)
    print(d.space_left())
    print(d.is_key(i))
    print(d.get(i))
    d.put(i, 'element' + i)
    print(d.get(i))
    print(d.space_left())
    print(d.is_key(i))


def test_added():
    d = NativeDictionary(10)
    print(d.space_left())
    print(d.is_key('el1'))
    d.put('el1', 'elem1')
    print(d.is_key('el1'))
    d.put('el1', 'elem1')
    print(d.is_key('el1'))
    print(d.space_left())


