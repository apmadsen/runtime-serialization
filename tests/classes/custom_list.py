# pyright: basic
# ruff: noqa
from typing import SupportsIndex, TypeVar, Sequence, Iterable, Any, cast, Union
from collections.abc import Sequence

T = TypeVar('T')

class CustomList(list[T]):

    def append(self, item: T) -> None:
        list.append(self, item)

    def insert(self, index: SupportsIndex, item: T) -> None:
        list.insert(self, index, item)

    def extend(self, items: Iterable[T]) -> None:
        list.extend(self, items)


    def pop(self, index: SupportsIndex = -1) -> T:
        return list.pop(self, index) if index is not None else list.pop(self)


    def remove(self, item: T) -> None:
        try:
            list.remove(self, item)
        except:
            raise Exception("Item was not found in collection")

    def clear(self) -> None:
        list.__delitem__(self, slice(None, None))


    def __add__(self, other: list[T]) -> list[T]:
        return CustomList[T](cast(Sequence[T], list.__add__(self, other)))


    def __setitem__(self, index: SupportsIndex, item: T) -> None:
        list.__setitem__(self, index, item)

    def __delitem__(self, index: SupportsIndex) -> None:
        list.__delitem__(self, index)


class CustomSequence(Sequence[T]):

    def __init__(self, items: list[T]):
        self.__col = items or []

    def __getitem__(self, key: int) -> T:
        return self.__col[key]

    def __len__(self) -> int:
        return len(self.__col)

