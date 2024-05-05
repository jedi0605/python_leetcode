import unittest
from MinimumSwapsToGroupAll1Together import Solution


class MinimumSwapsToGroupAll1Together_test(unittest.TestCase):
    def test_case1(self):        
        solution = Solution()
        data = [1,0,1,0,1]
        assert solution.minSwaps(data) == 1
        
        data = [1,0,1,0,1,0,0,1,1,0,1]
        assert solution.minSwaps(data) == 3

if __name__ == "__main__":
    unittest.main()
