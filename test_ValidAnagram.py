import unittest
from ValidAnagram import Solution


class test_ValidAnagram(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        s = "anagram"
        t = "nagaram"
        assert solution.isAnagram(s,t) == True

        s = "rat"
        t = "car"
        assert solution.isAnagram(s,t) == False

if __name__ == "__main__":
    unittest.main()
