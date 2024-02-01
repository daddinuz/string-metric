from unittest import TestCase

from tests.error import Error

from string_metric.similarity import jaccard


class Jaccard(TestCase):
    _COMBINATIONS = (
        ("isole egadi", "egadi isole", 0.66),
        ("karolina", "kathrine", 0.16),
        ("karolin", "kathrin", 0.2),
        ("karolin", "kerstin", 0.09),
        ("kathrin", "kerstin", 0.09),
        ("2173896", "2233796", 0.09),
        ("0000", "1111", 0),
        ("abc", "bac", 0),
        ("abc", "ab", 0.5),
        ("ab", "abc", 0.5),
        ("", "", 1),
    )

    def test_jaccard(self):
        for a, b, expected in self._COMBINATIONS:
            actual = jaccard(a, b)
            self.assertAlmostEqual(
                expected,
                actual,
                delta=0.009,
                msg=Error(expected, actual, jaccard, a, b),
            )
