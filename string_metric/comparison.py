from functools import lru_cache


@lru_cache
def longest_common_substring(a: str, b: str, s: str = "") -> str:
    if not (a and b):
        return s

    if a[0] == b[0]:
        s = longest_common_substring(a[1:], b[1:], s + a[0])

    return max(
        s,
        longest_common_substring(a[1:], b, ""),
        longest_common_substring(a, b[1:], ""),
        key=len,
    )


@lru_cache
def longest_common_subsequence(a: str, b: str) -> str:
    if not (a and b):
        return ""

    if a[0] == b[0]:
        return a[0] + longest_common_subsequence(a[1:], b[1:])

    return max(
        longest_common_subsequence(a[1:], b),
        longest_common_subsequence(a, b[1:]),
        key=len,
    )
