import unittest
from BitwiseANDNumbersRange import Solution



class BoatsSavePeople_test(unittest.TestCase):
    def test_case1(self):
        
        solution = Solution()
        assert solution.rangeBitwiseAnd(7,10) == 0
        assert solution.rangeBitwiseAnd(9,10) == 8

if __name__ == "__main__":
    unittest.main()
