import unittest
from MinimumGeneticMutation import Solution


class MinimumGeneticMutation_test(unittest.TestCase):
    def test_case1(self):
        startGene =       "AACCGGTT"
                        # "AACCGGTA"
                        # "AAACGGTA"
        endGene =         "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        solution = Solution()
        assert solution.minMutation(startGene,endGene,bank) == 2


if __name__ == "__main__":
    unittest.main()
