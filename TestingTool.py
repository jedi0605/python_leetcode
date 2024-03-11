
from typing import List

def compare_lists_of_lists(list1: List[List[str]], list2: List[List[str]]) -> bool:
    if len(list1) != len(list2):
        return False

    for sublist1, sublist2 in zip(list1, list2):
        if sublist1 != sublist2:
            return False
    return True