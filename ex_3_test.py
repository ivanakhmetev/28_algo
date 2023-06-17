from ex_3 import DynArray


    # def insert(self, i, itm):
    #     pass
    #     # добавляем объект itm в позицию i, начиная с 0

    # def delete(self, i):
    #     pass        # удаляем объект в позиции i

da = DynArray()
for i in range(64):
    da.append(i)

def test_insert():
    itm = 'el'
    idx_where_insert = [-1,10, 0,  2,  4, 6, 100]
    da.resize(22)
    for idx in idx_where_insert:
        try:
            print(da.capacity)
            print('inserting el to', idx)
            da.insert(idx, itm)
            print('value at idx', da[idx])
            print(da.capacity)
        except:
            pass
        # if da.capacity > len(da):
        #     da.insert(idx, itm)
        # if da.capacity == len(da):
        #     # da.resize(da.capacity * 2)
        #     da.insert(idx, itm)



def test_delete():
    idx_where_delete = [-1,10, 0,  2,  4, 6, 100]
    # da.resize(18)
    for idx in range(60):
        try:
            print(da.capacity)
            print('deleting el from', 1)
            da.delete(1)
            print('value at idx', da[1])
            print(da.capacity)
        except:
            pass


da = DynArray()
for i in range(70):
    da.append(i)
    # print (da[i]) 

# test_insert()
# da.print_elements()
test_delete()
da.print_elements()

# сложность обоих методов - О(n)

