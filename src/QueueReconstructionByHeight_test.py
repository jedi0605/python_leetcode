import unittest
import TestingTool
from QueueReconstructionByHeight import Solution


class QueueReconstructionByHeight_test(unittest.TestCase):
    def test_case1(self):
        people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
        sol = Solution()
        res =sol.reconstructQueue(people)
        ans  =[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
        assert TestingTool.compare_lists_of_lists(res,ans) == True


if __name__ == "__main__":
    unittest.main()
