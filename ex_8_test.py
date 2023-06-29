import unittest
from ex_8 import HashTable

class HashTableTests(unittest.TestCase):
    def test_initialization(self):
        table = HashTable(10, 3)
        self.assertEqual(table.size, 10)
        self.assertEqual(table.step, 3)
        self.assertEqual(len(table.slots), 10)
        # self.assertEqual(len(table.values), 10)
        # self.assertEqual(len(table.is_deleted), 10)

    def test_hash_function(self):
        table = HashTable(10, 3)
        index = table.hash_fun("key")
        self.assertIsInstance(index, int)
        self.assertGreaterEqual(index, 0)
        self.assertLess(index, table.size)

    def test_seek_slot(self):
        table = HashTable(10, 3)
        index = table.seek_slot("key")
        self.assertIsInstance(index, int)
        self.assertGreaterEqual(index, 0)
        self.assertLess(index, table.size)

    def test_put_and_find(self):
        table = HashTable(10, 3)
        table.put( "value1")
        table.put("value2")
        table.put( "value3")

        value = table.find("value1")
        self.assertEqual(value, "value1")

        value = table.find("value2")
        self.assertEqual(value, "value2")

        value = table.find("value3")
        self.assertEqual(value, "value3")

        value = table.find("nonexistent_key")
        self.assertIsNone(value)

if __name__ == '__main__':
    unittest.main()