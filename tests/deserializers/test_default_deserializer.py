# pyright: basic
from pytest import raises as assert_raises
from typing import Any, cast

from runtime.serialization import make_serializable, serializable, DefaultDeserializer, BaseSerializer, NotSerializableException
from runtime.serialization.core.base_serializer import serialize, deserialize


from tests.formatter import Formatter

def test_default_deserializer(serializable_types: list[type[Any]], serializables: list[Any]):

    @serializable
    class TestFields1:
        prop1: str
        prop2: int

    @serializable
    class TestFieldsAndProperties:
        def __init__(self):
            self.__prop1 = "Test"

        @property
        def prop1(self) -> str:
            return self.__prop1

        @prop1.setter
        def prop1(self, value: str):
            self.__prop1 = value

    class TestFail:
        def __init__(self):
            self.__prop1 = "Test"

        @property
        def prop1(self) -> str:
            return self.__prop1


    class TestBase:
        def __init__(self, prop1: str, prop2: int):
            self.__prop1 = prop1
            self.__prop2 = prop2

        @property
        def prop2(self) -> int:
            return self.__prop2

        @property
        def prop1(self) -> str:
            return self.__prop1

    class TestBaseFail1(TestBase):
        def __init__(self, prop1: str, prop2: float):
            pass

    class TestBaseFail2(TestBase):
        def __init__(self, prop1: str, prop2: int):
            pass

        @property
        def prop2(self):
            return TestBase.prop2



    class TestArgsFail1(TestBase):
        def __init__(self, arg1: int, *args: Any):
            super().__init__(cast(str, args[0]), cast(int, args[1]))

    class TestArgsFail2(TestBase):
        def __init__(self, *args: Any, **kwargs: Any):
            super().__init__(cast(str, args[0]), cast(int, args[1]))

    class TestArgsFail3(TestBase):
        def __init__(self, *args: Any):
            super().__init__(cast(str, args[0]), cast(int, args[1]))

    class TestKwargsFail2(TestBase):
        def __init__(self, **kwargs: Any):
            super().__init__(cast(str, kwargs["prop1"]), cast(int, kwargs["prop2"]))

    class TestKwargsFail1(TestBase):
        def __init__(self, arg1:int, **kwargs: Any):
            super().__init__(cast(str, kwargs["prop1"]), cast(int, kwargs["prop2"]))

    obj = TestFields1()
    obj.prop1 = "Test"
    obj.prop2 = 457568
    ser = serialize(obj, None, Formatter)
    deser = deserialize(ser, TestFields1, Formatter)
    reser = serialize(deser, None, Formatter)
    assert ser == reser
    assert obj.prop1 == deser.prop1
    assert obj.prop2 == deser.prop2


    obj = TestFieldsAndProperties()
    ser = serialize(obj, None, Formatter)
    deser = deserialize(ser, TestFieldsAndProperties, Formatter)
    reser = serialize(deser, None, Formatter)
    assert ser == reser

    for cls in [TestFail, TestArgsFail1, TestArgsFail2, TestArgsFail3, TestKwargsFail1, TestKwargsFail2]:
        with assert_raises(NotSerializableException):
            make_serializable(cls, deserializer=DefaultDeserializer)

    make_serializable(TestBase, deserializer=DefaultDeserializer)
    serializer = BaseSerializer[TestBase](Formatter)
    obj = TestBase("Test", 35)
    ser = serializer.serialize(obj)
    deser = serializer.deserialize(ser)
    reser = serializer.serialize(deser)
    assert ser == reser


    with assert_raises(NotSerializableException, match = r"Deserializer cannot deserialize type because type of argument .* doesn't match the member type .*"):
        make_serializable(TestBaseFail1, deserializer=DefaultDeserializer, strict=True)


    with assert_raises(NotSerializableException, match = r"Type .* is not serializable: Member .* is not annotated/typed"):
         make_serializable(TestBaseFail2, deserializer=DefaultDeserializer, strict=True)
