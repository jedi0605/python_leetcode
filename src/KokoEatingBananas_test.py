import unittest
from KokoEatingBananas import Solution



class KokoEatingBananas_test(unittest.TestCase):
    def test_case1(self):
        piles = [3,6,7,11]
        h = 8
        solution =Solution()
        
        assert solution.minEatingSpeed(piles,h) ==4


if __name__ == "__main__":
    unittest.main()
