# pyright: basic
# ruff: noqa
from runtime.serialization import serializable,  Deserializer
from typing import Type, TypeVar, Dict, Mapping, Any, cast
from datetime import datetime

from tests.classes.test_type1 import TestType1

T = TypeVar('T')

class TestDeserializer(Deserializer):
    __test__ = False
    def __init__(self, cls: Type[Any], *args: Any):
        pass

    def deserialize(self, cls: Type[T], data: Mapping[str, Any]) -> T:
        if cls is TestType2:
            return cast(T, TestType2(data["prop1"],data["prop2"],data["prop3"],data["prop4"],data["prop5"]))
        else:
            raise Exception(f"Unable to deserialize {cls.__name__}")


@serializable(namespace="TEST", deserializer=TestDeserializer, strict = True)
class TestType2:
    __test__ = False

    def __init__(self, prop1: float, prop2: datetime, prop3: Dict[str, str], prop4: TestType1, prop5: bytes):
        self.__prop1 = prop1
        self.__prop2 = prop2
        self.__prop3 = prop3
        self.__prop4 = prop4
        self.__prop5 = prop5


    @property
    def prop1(self) -> float:
        return self.__prop1

    @property
    def prop2(self) -> datetime:
        return self.__prop2

    @property
    def prop3(self) -> Dict[str, str]:
        return self.__prop3

    @property
    def prop4(self) -> TestType1:
        return self.__prop4

    @property
    def prop5(self) -> bytes:
        return self.__prop5
