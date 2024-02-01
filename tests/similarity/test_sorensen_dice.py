from unittest import TestCase

from tests.error import Error

from string_metric.similarity import sorensen_dice


class SorensenDice(TestCase):
    _COMBINATIONS = (
        ("isole egadi", "egadi isole", 0.8),
        ("karolina", "kathrine", 0.28),
        ("karolin", "kathrin", 0.33),
        ("karolin", "kerstin", 0.16),
        ("kathrin", "kerstin", 0.16),
        ("2173896", "2233796", 0.16),
        ("0000", "1111", 0),
        ("abc", "bac", 0),
        ("abc", "ab", 0.66),
        ("ab", "abc", 0.66),
        ("", "", 1),
    )

    def test_sorensen_dice(self):
        for a, b, expected in self._COMBINATIONS:
            actual = sorensen_dice(a, b)
            self.assertAlmostEqual(
                expected,
                actual,
                delta=0.009,
                msg=Error(expected, actual, sorensen_dice, a, b),
            )
