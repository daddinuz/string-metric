from unittest import TestCase

from tests.error import Error

from string_metric.hz import frequencies


class Frequencies(TestCase):
    _COMBINATIONS = [
        ("kitten", {"k": 1, "i": 1, "t": 2, "e": 1, "n": 1}),
        ("0000", {"0": 4}),
        ("abc", {"a": 1, "b": 1, "c": 1}),
        ("", {}),
    ]

    def test_frequencies(self):
        for s, expected in self._COMBINATIONS:
            actual = frequencies(s)
            self.assertDictEqual(
                expected,
                actual,
                msg=Error(expected, actual, frequencies, s),
            )
