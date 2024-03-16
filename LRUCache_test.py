import unittest
from LRUCache import DoubleNode, LRUCache


class test_LRUCache(unittest.TestCase):
    def test_case1(self):
        tmp = LRUCache(2)
        tmp.put(1, 1)
        tmp.printNodes()
        tmp.put(2, 2)
        tmp.printNodes()
        value = tmp.get(1)
        tmp.printNodes()
        tmp.put(3, 3)
        tmp.printNodes()
        value = tmp.get(2)
        tmp.printNodes()
        
    def test_case2(self):
        tmp = LRUCache(2)
        tmp.put(2, 1)
        tmp.printNodes()
        tmp.put(2, 2)
        tmp.printNodes()
        value = tmp.get(2)
        tmp.printNodes()
        tmp.put(1, 1)
        tmp.printNodes()
        tmp.put(4, 1)
        tmp.printNodes()
        value = tmp.get(2)
        tmp.printNodes()
            
if __name__ == "__main__":
    unittest.main()
