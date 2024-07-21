import unittest
from DesignAddAndSearchWordsDataStructure import WordDictionary


class DesignAddAndSearchWordsDataStructure_test(unittest.TestCase):
    def test_case1(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")
        assert wordDictionary.search("pad") == False# return False
        wordDictionary.search("bad")# return True
        wordDictionary.search(".ad")# return True
        wordDictionary.search("b..")# return True
        
if __name__ == "__main__":
    unittest.main()
