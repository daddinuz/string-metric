from typing import Iterable, Iterator, Union, override
from collections.abc import Set, Hashable


class Bigrams(Set[str], Hashable):
    __slots__ = "_delegate"

    def __init__(self, s: Union[str, "Bigrams", Iterable[str]]) -> None:
        if isinstance(s, str):
            self._delegate = frozenset(map(lambda i: s[i : i + 2], range(len(s) - 1)))
        elif isinstance(s, Bigrams):
            self._delegate = s._delegate
        elif isinstance(s, frozenset):
            for x in s:
                assert isinstance(x, str) and len(x) == 2, f"invalid bigram: `{x}`"

            self._delegate = s
        elif isinstance(s, Iterable):
            delegate = set()

            for x in s:
                assert isinstance(x, str) and len(x) == 2, f"invalid bigram: `{x}`"
                delegate.add(x)

            self._delegate = frozenset(delegate)
        else:
            raise TypeError(f"unsupported conversion from type: '{type(s)}'")

    def __len__(self) -> int:
        return len(self._delegate)

    def __bool__(self) -> bool:
        return bool(self._delegate)

    def __iter__(self) -> Iterator[str]:
        return iter(self._delegate)

    def __hash__(self) -> int:
        return hash(self._delegate)

    def __contains__(self, value: object) -> bool:
        return value in self._delegate

    @override
    def __and__(self, other: object) -> "Bigrams":
        if not isinstance(other, Bigrams):
            raise TypeError(
                f"unsupported operand type(s) for &: '{type(self)}' and '{type(other)}'"
            )
        return Bigrams(self._delegate & other._delegate)

    @override
    def __xor__(self, other: object) -> "Bigrams":
        if not isinstance(other, Bigrams):
            raise TypeError(
                f"unsupported operand type(s) for ^: '{type(self)}' and '{type(other)}'"
            )
        return Bigrams(self._delegate ^ other._delegate)

    @override
    def __or__(self, other: object) -> "Bigrams":
        if not isinstance(other, Bigrams):
            raise TypeError(
                f"unsupported operand type(s) for |: '{type(self)}' and '{type(other)}'"
            )
        return Bigrams(self._delegate | other._delegate)

    @override
    def __sub__(self, other: object) -> "Bigrams":
        if not isinstance(other, Bigrams):
            raise TypeError(
                f"unsupported operand type(s) for -: '{type(self)}' and '{type(other)}'"
            )
        return Bigrams(self._delegate - other._delegate)

    @override
    def __le__(self, other: object) -> bool:
        if not isinstance(other, Bigrams):
            raise TypeError(
                f"unsupported operand type(s) for <=: '{type(self)}' and '{type(other)}'"
            )
        return self._delegate <= other._delegate

    @override
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Bigrams):
            raise TypeError(
                f"unsupported operand type(s) for <: '{type(self)}' and '{type(other)}'"
            )
        return self._delegate < other._delegate

    @override
    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Bigrams):
            raise TypeError(
                f"unsupported operand type(s) for >=: '{type(self)}' and '{type(other)}'"
            )
        return self._delegate >= other._delegate

    @override
    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Bigrams):
            raise TypeError(
                f"unsupported operand type(s) for >: '{type(self)}' and '{type(other)}'"
            )
        return self._delegate > other._delegate

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Bigrams):
            raise TypeError(
                f"unsupported operand type(s) for ==: '{type(self)}' and '{type(other)}'"
            )
        return self._delegate == other._delegate

    @override
    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Bigrams):
            raise TypeError(
                f"unsupported operand type(s) for !=: '{type(self)}' and '{type(other)}'"
            )
        return self._delegate != other._delegate

    @override
    def isdisjoint(self, other: object) -> bool:
        if not isinstance(other, Bigrams):
            raise TypeError(
                f"unsupported type(s) for isdisjoint: '{type(self)}' and '{type(other)}'"
            )
        return self._delegate.isdisjoint(other._delegate)


def jaccard(a: Union[str, Bigrams], b: Union[str, Bigrams]) -> float:
    x, y = Bigrams(a), Bigrams(b)

    if not x and not y:
        return 1.0

    i = x & y
    return len(i) / (len(x) + len(y) - len(i))


def sorensen_dice(a: Union[str, Bigrams], b: Union[str, Bigrams]) -> float:
    x, y = Bigrams(a), Bigrams(b)

    if not x and not y:
        return 1.0

    i = x & y
    return (2 * len(i)) / (len(x) + len(y))


def szymkiewicz_simpson(a: Union[str, Bigrams], b: Union[str, Bigrams]) -> float:
    x, y = Bigrams(a), Bigrams(b)

    if not x or not y:
        return 1.0

    i = x & y
    return len(i) / min(len(x), len(y))
