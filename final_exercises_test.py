import unittest
import exercises

class Test(unittest.TestCase):

    def setUp(self):
        pass

    #tests
    def test_triple_max(self):
        self.assertEqual(exercises.triple_max(0, 0, 0), 0)
        self.assertEqual(exercises.triple_max(-1, 50, 9), 50)
        self.assertEqual(exercises.triple_max(1, 0.1, 0.01), 1)
        self.assertEqual(exercises.triple_max(-1, -12, -50), -1)

    def test_reverse_list(self):
        self.assertEqual(exercises.reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(exercises.reverse_list([2, 3, 4, 1, 5, "a"]), ["a", 5, 1, 4, 3, 2])

    def test_de_duplicate_list(self):
        self.assertEqual(exercises.de_duplicate_list([1, 1, 1, 1]), [1])
        self.assertEqual(exercises.de_duplicate_list([1, 2, 1, 2]), [1, 2])
        self.assertEqual(exercises.de_duplicate_list(["a", 2, "b", 2]), ["a", 2, "b"])
        self.assertEqual(exercises.de_duplicate_list(["rawr", "roar", "rrr", "rawr"]), ["rawr", "roar", "rrr"])

    def test_map_to_list(self):
        self.assertEqual(exercises.map_to_list([1, 0, 1, 0, 1], -1), [-1, 0, -1, 0, -1])
        self.assertEqual(exercises.map_to_list([1, 0, 1, 0, 1], 0), [0, 0, 0, 0, 0])
        self.assertEqual(exercises.map_to_list([2, 4, 8], 2), [4, 8, 16])

    def test_list_contains_part_of(self):
        self.assertEqual(exercises.list_contains_part_of(["aaple", "pear", "aaa"], "aa"),
            ["aaple", "aaa"])
        self.assertEqual(exercises.list_contains_part_of(["aaple", "pear", "aaa"], "e"),
            ["aaple", "pear"])
        self.assertEqual(exercises.list_contains_part_of(["aaple", "pear", "aaa"], "X"),
            [])

    def test_longest_word(self):
        self.assertEqual(exercises.longest_word(['googleplex', 'bike', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'TeamLeada']), 'pneumonoultramicroscopicsilicovolcanoconiosis')

    def test_pangram(self):
        self.assertEqual(exercises.is_pangram("tom marvolo riddle"), False)
        self.assertEqual(exercises.is_pangram("the quick brown fox jumps over the lazy dog"), True)


    def test_is_anagram(self):
        self.assertEqual(exercises.is_anagram("tom marvolo riddle", "i am lord voldemort"), True)
        self.assertEqual(exercises.is_anagram("the quick brown fox jumps over the lazy dog", "the cute brown fox"), False)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
