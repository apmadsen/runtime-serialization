# pyright: basic
from typing import Any, Callable, TypeVar, cast, overload
from datetime import datetime, date, time
from enum import Enum
from decimal import Decimal
from typingutils import issubclass_typing

from tests.classes.test_type1 import TestType1
from tests.classes.test_type2 import TestType2
from tests.classes.test_type3 import TestType3
from tests.classes.test_type4 import TestType4
from tests.classes.test_type5 import TestType5
from tests.classes.test_type6 import TestType6
from tests.classes.test_type7_8 import TestType7, TestType8, CustomList

from runtime.serialization import SerializerAttributes, is_serializable, serializable
from runtime.serialization.core.base_formatter import CONTEXT

T = TypeVar("T")

class SerializerProto:
    @overload
    @staticmethod
    def __call__(obj: Any) -> str:
        ...
    @overload
    @staticmethod
    def __call__(obj: Any, base: type[Any]) -> str:
        ...
    @staticmethod
    def __call__(obj: Any, base: type[Any] | None = None) -> str:
        ...

class DeserializerProto:
    @overload
    @staticmethod
    def __call__(text: str) -> Any:
        ...
    @overload
    @staticmethod
    def __call__(text: str, base: type[T]) -> T:
        ...
    @staticmethod
    def __call__(text: str, base: type[T] | None = None) -> T | Any:
        ...

class TestBase():
    __test__ = False
    def __init__(self, type_str: str, testpath: str, serializer: SerializerProto, deserializer: DeserializerProto):
        self.type = type_str
        self.testpath = testpath
        self.serialize = serializer
        self.deserialize = deserializer
        self.serializables: dict[type[Any], Any] = {
            TestType1: TestType1(),
            TestType2: TestType2(456.32, datetime.now(), {'asghdfj':'yhhd'}, TestType1(), b'CA0F'),
            TestType3: TestType3(),
            TestType4: TestType4(),
            TestType5: TestType5(),
            TestType6: TestType6("Test", 3457, 436.65),
            TestType7: TestType7(CustomList([TestType8(4568569)]))
        }
        self.serializations: dict[type[Any], Any] = {}
        self.serializations_untyped: dict[type[Any], Any] = {}
        self.deserializations: dict[type[Any], Any] = {}


        for cls, obj in self.serializables.items():
            self.serializations[cls] = self.serialize(obj)

        for cls, obj in self.serializables.items():
            self.deserializations[cls] = self.deserialize(self.serializations[cls], cls)


    def test_base_serialization(self):
        @serializable
        class DerivedClass(TestType1):
            ...

        obj = DerivedClass()
        ser1 = self.serialize(obj)
        ser2 = self.serialize(obj, TestType1)


    def test_untyped_serialization(self):
        for cls, _ in self.serializables.items():
            serialized = self.serializations[cls]
            deserialized = self.deserialize(serialized)
            reserialized = self.serialize(deserialized)

            assert serialized == reserialized

    def test_deserialization(self):
        for cls, obj in self.serializables.items():
            deserialized = self.deserializations[cls]

            assert isinstance(deserialized, cls)

            self._test_deserialization(cls, obj, deserialized)

    def _test_deserialization(self, cls: type[Any], obj: Any, deserialized: Any, path: str = ""):
        root = SerializerAttributes.get(cls)
        for property in root.members:
            property_path = f"{path}.{property.name}" if path else f"{cls.__name__}.{property.name}"

            value = property.get_value(obj)
            value_comparison = property.get_value(deserialized)

            if is_serializable(type(value)) and not is_encodable(type(value)):
                self._test_deserialization(type(value), value, value_comparison, property_path)
            elif isinstance(value, list):
                for i in range(len(cast(list[Any], value))):
                    item = cast(Any, value[i])
                    item_comparison = cast(list[Any], value_comparison)[i]

                    if is_serializable(type(item)) and not is_encodable(type(item)):
                        self._test_deserialization(type(item), item, item_comparison, property_path + f"[{i}]")
                    elif hasattr(item, "__eq__"):
                        # print(f"Testing property '{property_path}[{i}]' value {item}")
                        assert item == item_comparison

            elif isinstance(value, dict):
                for key, item in cast(dict[Any, Any], value).items():
                    item_comparison = cast(dict[Any, Any], value_comparison)[key]

                    if is_serializable(type(item)) and not is_encodable(type(item)):
                        self._test_deserialization(type(item), item, item_comparison, property_path + f".{key}")
                    elif hasattr(item, "__eq__"):
                        # print(f"Testing property '{property_path}.{key}' value {item}")
                        assert item == item_comparison
            else:
                # print(f"Testing property '{property_path}' value {value}")
                value = property.get_value(obj)

                if isinstance(value, Decimal):
                    value = value.normalize(CONTEXT) # decimals are normalized when encoded, so that's necessary to be done here as

                assert value == value_comparison


def is_encodable(obj: object | type) -> bool:
    obj_type = obj if isinstance(obj, type) else type(obj)
    return issubclass_typing(obj_type, (bool, int, float, str, bytes, date, time, datetime, Enum, tuple, list, set, dict, Decimal))
