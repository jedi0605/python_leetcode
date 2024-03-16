import unittest
from LengthOfLastWord import Solution


class Test_LengthOfLastWord(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        assert solution.lengthOfLastWord("Hello World") == 5
        assert solution.lengthOfLastWord("   fly me   to   the moon  ") == 4
        assert solution.lengthOfLastWord("luffy is still joyboy") == 6


if __name__ == "__main__":
    unittest.main()
