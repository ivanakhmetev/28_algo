from ex_10_new import PowerSet

p1 = PowerSet()
p2 = PowerSet()
p3 = PowerSet()
p4 = PowerSet()
p5 = PowerSet()

for i in range(10):
    p1.put(i)

for i in range(10):
    p1.put(i)

for i in range(5, 15):
    p2.put(i)

for i in range(10, 20):
    p3.put(i)

for i in range(2, 4):
    p5.put(i)


print(p1.table)
# i1 = p1.intersection(p2)
print(p1.intersection(p2).table)
print(p1.intersection(p3).table)
print('union')
print(p1.union(p2).table)
print(p1.union(p3).table)
print(p1.union(p4).table)
print('difference')
print(p1.difference(p2).table)
print(p1.difference(p3).table)
print(p1.difference(p1).table)
print('issubset')
print(p1.issubset(p2))
print(p5.issubset(p1))
print(p1.issubset(p1))

