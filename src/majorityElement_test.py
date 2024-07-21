import unittest
from majorityElement import Solution

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_majorityElement(self):
        a = 3
        assert a == 3
        solution = Solution()
        res =  solution.majorityElement2([3, 2, 3])
        assert res == 3
    
    def test_majorityElement2(self):
        a = 3
        assert a == 3
        solution = Solution()
        res =  solution.majorityElement2([3, 2, 3])
        assert res == 3


if __name__ == '__main__':
    unittest.main()
