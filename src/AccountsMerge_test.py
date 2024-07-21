import unittest
from AccountsMerge import Solution


class AccountsMerge_test(unittest.TestCase):
    def test_case1(self):
        accounts = [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
        solution = Solution()
        res = solution.accountsMerge(accounts)
        ans = [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]

        self.assertSequenceEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
