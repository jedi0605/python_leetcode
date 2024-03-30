import unittest
from typing import List
import InsertDeleteGetRandomDuplicatesallowed 

class InsertDeleteGetRandomDuplicatesallowed_test(unittest.TestCase):
    def test1(self):
        sol = InsertDeleteGetRandomDuplicatesallowed.RandomizedCollection()
        sol.insert(1)
        sol.insert(1)
        sol.insert(2)
        sol.getRandom()
        sol.remove(1)
        
def compare_lists_of_lists(list1: List[List[str]], list2: List[List[str]]) -> bool:
    if len(list1) != len(list2):
        return False

    for sublist1, sublist2 in zip(list1, list2):
        if sublist1 != sublist2:
            return False
    return True


if __name__ == '__main__':
    unittest.main()
