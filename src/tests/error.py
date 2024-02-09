from typing import Any, Callable


class Error:
    def __init__(
        self, expected: Any, actual: Any, callable: Callable[..., Any], *args: Any
    ):
        self._expected = expected
        self._actual = actual
        self._func = callable.__name__
        self._args = args

    def __str__(self) -> str:
        func, args, actual, expected = (
            self._func,
            self._args,
            self._actual,
            self._expected,
        )
        return f"Expected `{func}({', '.join(map(repr, args))})` to return `{repr(expected)}` but got `{repr(actual)}`"

    def __repr__(self) -> str:
        return repr(str(self))
