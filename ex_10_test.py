from ex_10 import PowerSet, HashTable

# h = HashTable(200, 15)
# t = 5
# # print(t.size)
# print(h.size)

p = PowerSet()
# print(type(p))
# p.size()
# print(p.size())
# for i in range(10):
#     p.put(str(i))
#     print(p.size())

# # for i in range(11):
# #     print(p.get(str(i)))

# # for i in range(3, 7):
# #     print(p.get(str(i)))
# #     print(p.remove(str(i)))
# #     print(p.get(str(i)))

# # for i in range(20):
# #     print(p.remove(str(i)))

# for i in range(11):
#     print(p.get(str(i)))
# # print(p.get_all())
p = PowerSet()
p2 = PowerSet()

for i in range(10):
    p.put(str(i))
print(p.get_all())

for i in range(5, 18):
    # print(i)
    p2.put(str(i))
print(p2.get_all())

p3 = p.intersection(p2)
print(p3.get_all())
p4 = p.union(p2)
print(p4.get_all())
p5 = p.difference(p2)
print(p5.get_all())
print(p.issubset(p5))