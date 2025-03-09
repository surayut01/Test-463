from coe_number.alternating_characters import alternatingCharacters
import unittest

class TestAlternatingCharacters(unittest.TestCase):

    def test_alternating_ABABABAB(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)

    def test_non_alternating_AAABBB(self):
        self.assertEqual(alternatingCharacters("AAABBB"), 4)

    def test_all_same_AAAA(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    def test_single_char(self):
        self.assertEqual(alternatingCharacters("A"), 0)

    def test_empty_string(self):
        self.assertEqual(alternatingCharacters(""), 0)

if __name__ == "__main__":
    unittest.main()
