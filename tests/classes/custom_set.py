# pyright: basic
# ruff: noqa
from typing import SupportsIndex, TypeVar, Sequence, Iterable, Any, cast, Union

T = TypeVar('T')

class CustomSet(set[T]):

    def append(self, item: T) -> None:
        set.add(self, item)

    def remove(self, item: T) -> None:
        try:
            set.remove(self, item)
        except:
            raise Exception("Item was not found in collection")

    def clear(self) -> None:
        set.clear(self)


