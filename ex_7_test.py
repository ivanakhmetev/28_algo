from ex_7 import OrderedList, OrderedStringList

# oa_list = OrderedList(True)
# od_list = OrderedList(False)

# for i in range(20):
#     oa_list.add(i)
#     od_list.add(i)

# # for i in range(20):
# #     oa_list.add(i)

# for i in range(3):
#     oa_list.add(5)
#     od_list.add(5)
# # for i in range(20, 0, -1):
# #     oa_list.add(i)
# #     od_list.add(i)


# # ela = oa_list.get_all()
# # for el in ela:
# #     print(el.value)

# eld = od_list.get_all()
# print(len(eld))
# for el in eld:
#     print(el.value)
# print(oa_list[0], oa_list[1])
# print(oa_list.binary_search(1))
# print(od_list.get_all())
# print(oa_list.len())
# print(od_list.len())

ol = OrderedList(True)
ol.add(5)
assert ol.get_values() == [5]

# Проверка добавления элемента в отсортированный список по возрастанию
ol = OrderedList(True)
ol.add(5)
ol.add(3)
ol.add(8)
ol.add(1)
ol.add(7)
print(ol.get_values())
assert ol.get_values() == [1, 3, 5, 7, 8]

# Проверка добавления элемента в отсортированный список по убыванию
ol = OrderedList(False)
ol.add(5)
ol.add(3)
ol.add(8)
ol.add(1)
ol.add(7)
assert ol.get_values() == [8, 7, 5, 3, 1]

# Проверка добавления элемента, который станет новой головой списка
ol = OrderedList(True)
ol.add(5)
ol.add(3)
ol.add(1)
assert ol.get_values() == [1, 3, 5]

# Проверка добавления элемента, который станет новым хвостом списка
ol = OrderedList(False)
ol.add(5)
ol.add(8)
ol.add(10)
assert ol.get_values() == [10, 8, 5]

# Проверка добавления элемента, который будет в середине списка
ol = OrderedList(True)
ol.add(5)
ol.add(7)
ol.add(6)
ol.add(3)
assert ol.get_values() == [3, 5, 6, 7]

print("1 тесты пройдены успешно!")
ol = OrderedList(True)
assert ol.find(5) is None

# Проверка поиска элемента в отсортированном списке по возрастанию
ol = OrderedList(True)
ol.add(1)
ol.add(3)
ol.add(5)
ol.add(7)
ol.add(9)
assert ol.find(5).value == 5
assert ol.find(2) is None
assert ol.find(10) is None

# Проверка поиска элемента в отсортированном списке по убыванию
ol = OrderedList(False)
ol.add(9)
ol.add(7)
ol.add(5)
ol.add(3)
ol.add(1)
print('all v', ol.get_values())
assert ol.find(5).value == 5
assert ol.find(2) is None
assert ol.find(10) is None

# Проверка поиска элемента в списке с повторяющимися значениями
ol = OrderedList(True)
ol.add(1)
ol.add(3)
ol.add(3)
ol.add(5)
ol.add(7)
assert ol.find(3).value == 3

print("2 тесты пройдены успешно!")


# Пример использования класса OrderedStringList
ol = OrderedStringList(True)
ol.add("  apple")
ol.add("banana  ")
ol.add("  cherry  ")

ol = OrderedList(True)
ol.delete(5)
assert ol.get_values() == []

# Проверка удаления элемента из отсортированного списка по возрастанию
ol = OrderedList(True)
ol.add(1)
ol.add(3)
ol.add(5)
ol.add(7)
ol.add(9)
ol.delete(5)
ol.delete(2)
ol.delete(10)
assert ol.get_values() == [1, 3, 7, 9]

# Проверка удаления элемента из отсортированного списка по убыванию
ol = OrderedList(False)
ol.add(9)
print(ol.head.value, ol.tail.value)
ol.delete(9)
print(ol.head, ol.tail)
ol.add(7)
ol.add(5)
ol.add(3)
ol.add(1)
ol.delete(5)
ol.delete(2)
ol.delete(10)
assert ol.get_values() == [ 7, 3, 1]

print("3 тесты пройдены успешно!")

ol = OrderedList(True)  # Создаем упорядоченный список по возрастанию
ol.add(1)  # Добавляем первый элемент
# ol.add(3)  # Добавляем второй элемент, который должен быть больше первого
# ol.add(2)  # Добавляем третий элемент, который нарушает упорядоченность
print(ol.get_values())

ol = OrderedList(False)  # Создаем упорядоченный список по возрастанию
ol.add(1)  # Добавляем первый элемент
ol.add(3)  # Добавляем второй элемент, который должен быть больше первого
ol.add(2)  # Добавляем третий элемент, который нарушает упорядоченность
print(ol.get_values())
print(ol.find(1).prev, ol.find(1).next)
print(ol.head.value, ol.tail.value)
print(ol.head.prev, ol.head.next.value)
print(ol.tail.next, ol.tail.prev.value)