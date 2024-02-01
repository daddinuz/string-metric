from unittest import TestCase

from tests.error import Error

from string_metric.distance import damerau_levenshtein


class DamerauLevenshtein(TestCase):
    _COMBINATIONS = (
        ("isole egadi", "egadi isole", 10),
        ("karolina", "kathrine", 4),
        ("karolin", "kathrin", 3),
        ("karolin", "kerstin", 3),
        ("kathrin", "kerstin", 4),
        ("2173896", "2233796", 3),
        ("0000", "1111", 4),
        ("abc", "bac", 1),
        ("abc", "ab", 1),
        ("ab", "abc", 1),
        ("", "", 0),
    )

    def test_damerau_levenshtein(self):
        for a, b, expected in self._COMBINATIONS:
            actual = damerau_levenshtein(a, b)
            self.assertEqual(
                expected, actual, msg=Error(expected, actual, damerau_levenshtein, a, b)
            )
