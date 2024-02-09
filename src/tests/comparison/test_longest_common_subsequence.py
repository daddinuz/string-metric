from unittest import TestCase

from tests.error import Error

from string_metric.comparison import longest_common_subsequence


class LongestCommonSubsequence(TestCase):
    _COMBINATIONS = (
        ("isole egadi", "egadi isole", "egadi"),
        ("karolina", "kathrine", "karin"),
        ("karolin", "kathrin", "karin"),
        ("karolin", "kerstin", "krin"),
        ("kathrin", "kerstin", "krin"),
        ("2173896", "2233796", "2396"),
        ("0000", "1111", ""),
        ("abc", "bac", "bc"),
        ("abc", "ab", "ab"),
        ("ab", "abc", "ab"),
        ("", "", ""),
    )

    def test_longest_common_subsequence(self):
        for a, b, expected in self._COMBINATIONS:
            actual = longest_common_subsequence(a, b)
            self.assertEqual(
                expected,
                actual,
                msg=Error(expected, actual, longest_common_subsequence, a, b),
            )
