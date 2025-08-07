from typing import  Any
from enum import Enum

from runtime.serialization import serializable, resolvable, resolve_as, KwargsDeserializer

class SubType(Enum):
    T1 = 1
    T2 = 2
    T3 = 3

@serializable
@resolvable
class ResolvableBase:
    def __init__(self, subtype: SubType):
        self.__subtype = subtype

    @property
    def subtype(self) -> SubType:
        return self.__subtype

@serializable
class ResolvableDerived(ResolvableBase):
    def __init__(self, subtype: SubType):
        self.__subtype = subtype

    @property
    def subtype(self) -> SubType:
        return self.__subtype

@resolve_as(ResolvableBase, lambda base: base.subtype == SubType.T1)
@serializable(deserializer=KwargsDeserializer)
class T1(ResolvableBase):
    def __init__(self, **kwargs: Any):
        super().__init__(SubType.T1)
        self.__prop1 = kwargs["prop1"]

    @property
    def prop1(self) -> str:
        return self.__prop1

@resolve_as(ResolvableBase, lambda base: base.subtype == SubType.T2)
@serializable(deserializer=KwargsDeserializer)
class T2(ResolvableBase):
    def __init__(self, **kwargs: Any):
        super().__init__(SubType.T2)
        self.__prop1 = kwargs["prop1"]

    @property
    def prop1(self) -> int:
        return self.__prop1


@resolve_as(ResolvableBase, lambda base: base.subtype == SubType.T3)
@serializable(deserializer=KwargsDeserializer)
class T3(ResolvableDerived):
    def __init__(self, **kwargs: Any):
        super().__init__(SubType.T3)
        self.__prop1 = kwargs["prop1"]

    @property
    def prop1(self) -> str:
        return self.__prop1