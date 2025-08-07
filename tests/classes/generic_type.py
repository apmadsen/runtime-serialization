# pyright: basic
# ruff: noqa
from typing import Generic, TypeVar

T = TypeVar("T")

class GenericType(Generic[T]):
    def __init__(self, prop1: T):
        self.__prop1 = prop1

    @property
    def prop1(self) -> T:
        return self.__prop1