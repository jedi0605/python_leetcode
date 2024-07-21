import unittest
from LetterCombinationsofaPhoneNumber import Solution
from ListNode import ListNode


class LetterCombinationsofaPhoneNumber_test(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        digits = "23"
        res = sol.letterCombinations(digits)
        ans = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertSequenceEqual(ans, res)


if __name__ == "__main__":
    unittest.main()
