# pyright: basic
# ruff: noqa
from runtime.serialization import serializable, Deserializer
from typing import Type, TypeVar, Mapping, Any, cast

from tests.classes.test_type1 import TestType1

T = TypeVar('T')

class TestDeserializer(Deserializer):
    __test__ = False
    def __init__(self, cls: Type[Any], *args: Any):
        pass

    def deserialize(self, cls: Type[T], data: Mapping[str, Any]) -> T:
        if cls is TestType3:
            return cast(T, TestType3(**data))
        else:
            raise Exception(f"Unable to deserialize {cls.__name__}")


@serializable(deserializer=TestDeserializer, strict = True)
class TestType3(TestType1):
    __test__ = False
    pass