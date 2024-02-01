from unittest import TestCase

from tests.error import Error

from string_metric.distance import hamming


class Hamming(TestCase):
    _COMBINATIONS = (
        ("isole egadi", "egadi isole", 10),
        ("karolina", "kathrine", 4),
        ("karolin", "kathrin", 3),
        ("karolin", "kerstin", 3),
        ("kathrin", "kerstin", 4),
        ("2173896", "2233796", 3),
        ("0000", "1111", 4),
        ("abc", "bac", 2),
        ("abc", "ab", None),
        ("ab", "abc", None),
        ("", "", 0),
    )

    def test_hamming(self):
        for a, b, expected in self._COMBINATIONS:
            actual = hamming(a, b)
            self.assertEqual(
                expected, actual, msg=Error(expected, actual, hamming, a, b)
            )
