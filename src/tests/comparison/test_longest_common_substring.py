from unittest import TestCase

from tests.error import Error

from string_metric.comparison import longest_common_substring


class LongestCommonSubstring(TestCase):
    _COMBINATIONS = (
        ("isole egadi", "egadi isole", "egadi"),
        ("karolina", "kathrine", "ka"),
        ("karolin", "kathrin", "ka"),
        ("karolin", "kerstin", "in"),
        ("kathrin", "kerstin", "in"),
        ("2173896", "2233796", "96"),
        ("0000", "1111", ""),
        ("abc", "bac", "b"),
        ("abc", "ab", "ab"),
        ("ab", "abc", "ab"),
        ("", "", ""),
    )

    def test_longest_common_substring(self):
        for a, b, expected in self._COMBINATIONS:
            actual = longest_common_substring(a, b)
            self.assertEqual(
                expected,
                actual,
                msg=Error(expected, actual, longest_common_substring, a, b),
            )
