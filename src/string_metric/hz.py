from typing import Dict


def frequencies(s: str) -> Dict[str, int]:
    hz: Dict[str, int] = {}
    for c in s:
        hz[c] = hz.get(c, 0) + 1
    return hz
