from ex_11 import BloomFilter

a = BloomFilter(64)
# print(a.bit_array)
# print(int(a.bit_array[1], 2))
# str1 = 'aaqwea'
# # print(a.hash1(str))
# # print(a.hash2(str))
# # print(a.bit_array)
# a.add(str1)
# # print(a.bit_array)
# print(a.is_value(str1))
# print(a.is_value('aa'))

string = '0123456789'
a.add(string)
for i in range(10):
    str1 = string[i:] + string[:i]
    # a.add(str1)
    print(a.is_value(str1), a._is_value(str1))


# m = 3
# import sys
# print(sys.getsizeof(m))
# a.set_bit(3)
# print(a.bits)
# print(a.bit_representation())
# for i in range(31):
#     a.clear_bit(i)
#     # print(a.bits)
#     print(a.bit_representation())
# m = 2147483648
# print(m.bit_length())

