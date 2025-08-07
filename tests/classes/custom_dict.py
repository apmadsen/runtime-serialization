# pyright: basic
# ruff: noqa
from typing import TypeVar, Iterator, cast
from collections.abc import Mapping

Tkey = TypeVar('Tkey')
Tvalue = TypeVar('Tvalue')

class CustomDict(dict[Tkey, Tvalue]):

    def append(self, key: Tkey, item: Tvalue) -> None:
        dict.__setitem__(self, key, item)


    def remove(self, key: Tkey) -> None:
        old_item = cast(Tvalue, dict.__getitem__(self, key))
        dict.__delitem__(self, old_item)


    def __setitem__(self, key: Tkey, item: Tvalue) -> None:
        dict.__setitem__(self, key, item)



    def __delitem__(self, key: Tkey) -> None:
        dict.__delitem__(self, key)

class CustomMapping(Mapping[Tkey, Tvalue]):

    def __init__(self, items: dict[Tkey, Tvalue]):
        self.__dict = items or {}

    def __getitem__(self, key: Tkey) -> Tvalue:
        return self.__dict[key]

    def __iter__(self) -> Iterator[Tkey]:
        return iter(self.__dict)

    def __len__(self) -> int:
        return len(self.__dict)
