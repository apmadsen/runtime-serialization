# pyright: basic
from pytest import raises as assert_raises
from typing import Any, cast

from runtime.serialization import make_serializable, serializable, KwargsDeserializer, BaseSerializer, NotSerializableException
from runtime.serialization.core.base_serializer import serialize, deserialize


from tests.formatter import Formatter


def test_kwargs_deserializer(serializable_types: list[type[Any]], serializables: list[Any]):

    class TestKwargs1:
        def __init__(self, **kwargs: Any):
            self.prop1 = cast(str, kwargs["prop1"]) if "prop1" in kwargs else "Test"
            self.prop2 = cast(int, kwargs["prop2"]) if "prop2" in kwargs else 65

        prop1: str
        prop2: int
    class TestKwargs2:
        def __init__(self, **kwargs: Any):
            self.prop1 = cast(str, kwargs["prop1"]) if "prop1" in kwargs else "Test"
            self.__prop2 = cast(int, kwargs["prop2"]) if "prop2" in kwargs else 65

        prop1: str
        @property
        def prop2(self) -> int:
            return self.__prop2

    with assert_raises(NotSerializableException):
        make_serializable(TestKwargs2)
    make_serializable(TestKwargs1, deserializer=KwargsDeserializer)

    obj = TestKwargs1()
    obj.prop1 = "Test"
    obj.prop2 = 457568
    ser = serialize(obj, None, Formatter)
    deser = deserialize(ser, TestKwargs1, Formatter)
    reser = serialize(deser, None, Formatter)
    assert ser == reser
    assert obj.prop1 == deser.prop1
    assert obj.prop2 == deser.prop2

