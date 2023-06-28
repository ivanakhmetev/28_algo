from ex_7 import OrderedList, OrderedStringList

oa_list = OrderedList(True)
od_list = OrderedList(False)

for i in range(20):
    oa_list.add(i)
    od_list.add(i)

# for i in range(20):
#     oa_list.add(i)

for i in range(3):
    oa_list.add(5)
    od_list.add(5)
# for i in range(20, 0, -1):
#     oa_list.add(i)
#     od_list.add(i)


# ela = oa_list.get_all()
# for el in ela:
#     print(el.value)

eld = od_list.get_all()
print(len(eld))
for el in eld:
    print(el.value)
# print(oa_list[0], oa_list[1])
# print(oa_list.binary_search(1))
# print(od_list.get_all())
# print(oa_list.len())
# print(od_list.len())

