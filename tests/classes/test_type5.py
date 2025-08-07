# pyright: basic
# ruff: noqa
from runtime.serialization import serializable


@serializable( strict = True)
class TestType5:
    __test__ = False

    prop1: str
    prop2: int
    prop3: float

    def __init__(self, prop1: str = "Test", prop2: int = 4568, prop3: float = 78833.5, prop4: bool = True, prop5: bytes = b'\x13\0\0\0\x08\0'):
        self.prop1 = prop1
        self.prop2 = prop2
        self.prop3 = prop3
        self.__prop4 = prop4
        self.__prop5 = prop5


    @property
    def prop4(self) -> bool:
        return self.__prop4
    @prop4.setter
    def prop4(self, value: bool):
        self.__prop4 = value

    @property
    def prop5(self) -> bytes:
        return self.__prop5
    @prop5.setter
    def prop5(self, value: bytes):
        self.__prop5 = value
