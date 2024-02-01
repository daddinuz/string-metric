from unittest import TestCase

from tests.error import Error

from string_metric.similarity import szymkiewicz_simpson


class SzymkiewiczSimpson(TestCase):
    _COMBINATIONS = (
        ("isole egadi", "egadi isole", 0.8),
        ("karolina", "kathrine", 0.28),
        ("karolin", "kathrin", 0.33),
        ("karolin", "kerstin", 0.16),
        ("kathrin", "kerstin", 0.16),
        ("2173896", "2233796", 0.16),
        ("0000", "1111", 0),
        ("abc", "bac", 0),
        ("abc", "ab", 1),
        ("ab", "abc", 1),
        ("", "", 1),
    )

    def test_szymkiewicz_simpson(self):
        for a, b, expected in self._COMBINATIONS:
            actual = szymkiewicz_simpson(a, b)
            self.assertAlmostEqual(
                expected,
                actual,
                delta=0.009,
                msg=Error(expected, actual, szymkiewicz_simpson, a, b),
            )
