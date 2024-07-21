import unittest
from BoatsSavePeople import Solution
from TreeNode import TreeNode
import TestingTool


class BoatsSavePeople_test(unittest.TestCase):
    def test_case1(self):
        
        solution = Solution()
        
        people = [3,5,3,4]
        limit = 5
        assert solution.numRescueBoats(people,limit) == 4

if __name__ == "__main__":
    unittest.main()
