from ex_12 import NativeCache

cache = NativeCache(3)
cache.put("key1", "value1")
cache.put("key2", "value2")
cache.put("key3", "value3")
print(cache.get("key1"))  # Output: value1
print(cache.get("key2"))  # Output: value2
print(cache.get("key3"))  # Output: value3

cache.put("key4", "value4")  # key1 будет вытеснен, так как имеет наименьшее количество обращений
print(cache.get("key1"))  # Output: None
print(cache.get("key4"))  # Output: value4
for i in range(4):
    cache.put('key' + str(i), 'val' + str(i + 10))
print(cache.slots)
print(cache.values)
for i in range(4):
    print(cache.get('key' + str(i)))
    # cache.put('key' + str(i), 'val' + str(i + 10))