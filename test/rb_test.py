import unittest

from src.rabin_karp import rabin_karp


class TestRabinKarp(unittest.TestCase):

    def test_empty_haystack(self):
        result = rabin_karp("", "needle")
        self.assertEqual(result, [])

    def test_empty_needle(self):
        result = rabin_karp("haystack", "")
        self.assertEqual(result, [])

    def test_one_match(self):
        result = rabin_karp("kdjvnwjrjvo", "vn")
        self.assertEqual(result, [3])

    def test_few_matches(self):
        result = rabin_karp("ababab", "ab")
        self.assertEqual(result, [0, 2, 4])

    def test_no_match(self):
        result = rabin_karp("abcdefg", "kh")
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
