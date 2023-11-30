import unittest

from src.robin_karp import rabin_karp


class TestRabinKarp(unittest.TestCase):
    def test_rabin_karp(self):
        haystack = "abccbbcabACBCBABacb"
        needle = "cb"
        result = rabin_karp(haystack, needle)
        self.assertEqual(result, [3, 17])


if __name__ == '__main__':
    unittest.main()
