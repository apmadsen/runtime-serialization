# pyright: basic
# ruff: noqa
from runtime.serialization import serializable

@serializable(strict=True)
class UntypedStrict:

    def __init__(self, prop1, prop2):
        self.__prop1 = prop1
        self.__prop2 = prop2

    @property
    def prop1(self):
        return self.__prop1

    @property
    def prop2(self):
        return self.__prop2

@serializable
class Untyped1:

    def __init__(self, prop1, prop2):
        self.__prop1 = prop1
        self.__prop2 = prop2

    @property
    def prop1(self):
        return self.__prop1

    @property
    def prop2(self):
        return self.__prop2

@serializable
class Untyped2:

    def __init__(self, prop1: list, prop2: set, prop3: dict, prop4: tuple):
        self.__prop1 = prop1
        self.__prop2 = prop2
        self.__prop3 = prop3
        self.__prop4 = prop4

    @property
    def prop1(self) -> list:
        return self.__prop1

    @property
    def prop2(self) -> set:
        return self.__prop2

    @property
    def prop3(self) -> dict:
        return self.__prop3

    @property
    def prop4(self) -> tuple:
        return self.__prop4

class Untyped3:

    def __init__(self, prop1: str):
        self.__prop1 = prop1

    @property
    def prop1(self) -> str:
        return self.__prop1

@serializable
class Untyped4:

    def __init__(self, prop1):
        self.__prop1 = prop1

    @property
    def prop1(self):
        return self.__prop1



