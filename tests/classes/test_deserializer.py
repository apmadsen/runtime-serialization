# pyright: basic
from runtime.serialization import Deserializer
from typing import Mapping, Any, TypeVar, Type, cast

from tests.classes import test_type1, test_type2, test_type3

T = TypeVar('T')

class TestDeserializer(Deserializer):
    __test__ = False
    def __init__(self, cls: Type[Any], *args: Any):
        pass

    def deserialize(self, cls: Type[T], data: Mapping[str, Any]) -> T:
        if cls is test_type1.TestType1:
            return cast(T, test_type1.TestType1(**data))
            #return TestType1(data["prop1"],data["prop2"],data["prop3"])
        elif cls is test_type2.TestType2:
            return cast(T, test_type2.TestType2(data["prop1"],data["prop2"],data["prop3"],data["prop4"],data["prop5"]))
        elif cls is test_type3.TestType3:
            return cast(T, test_type3.TestType3(**data))
        else:
            raise Exception(f"Unable to deserialize {cls.__name__}")