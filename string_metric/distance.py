from typing import Optional
from functools import lru_cache


def hamming(a: str, b: str) -> Optional[int]:
    if len(a) != len(b):
        return None
    return sum(map(lambda t: t[0] != t[1], zip(a, b)))


@lru_cache
def levenshtein(a: str, b: str) -> int:
    if not a:
        return len(b)

    if not b:
        return len(a)

    if a[0] == b[0]:
        return levenshtein(a[1:], b[1:])  # noop

    return 1 + min(
        levenshtein(a, b[1:]),  # insertion
        levenshtein(a[1:], b),  # deletion
        levenshtein(a[1:], b[1:]),  # substitution
    )


@lru_cache
def damerau_levenshtein(a: str, b: str) -> int:
    if not a:
        return len(b)

    if not b:
        return len(a)

    if a[0] == b[0]:
        return damerau_levenshtein(a[1:], b[1:])  # noop

    if len(a) > 1 and len(b) > 1 and a[0] == b[1] and a[1] == b[0]:
        return 1 + min(
            damerau_levenshtein(a, b[1:]),  # insertion
            damerau_levenshtein(a[1:], b),  # deletion
            damerau_levenshtein(a[1:], b[1:]),  # substitution
            damerau_levenshtein(a[2:], b[2:]),  # transposition
        )

    return 1 + min(
        damerau_levenshtein(a, b[1:]),  # insertion
        damerau_levenshtein(a[1:], b),  # deletion
        damerau_levenshtein(a[1:], b[1:]),  # substitution
    )
