# pyright: basic
# ruff: noqa
from __future__ import annotations
from runtime.serialization import serializable

from tests.classes.custom_list import CustomList
from tests.classes.custom_dict import CustomDict


@serializable
class TestItem:
    __test__ = False
    def __init__(self):
        self.__prop1 = "Test"

    @property
    def prop1(self) -> str:
        return self.__prop1
    @prop1.setter
    def prop1(self, value: str):
        self.__prop1 = value

@serializable
class TestType4:
    __test__ = False
    def __init__(self):
        self.__list = CustomList[str](["Item1", "Item2", "Item3"])
        self.__list1 = CustomList[TestItem]([TestItem()])
        self.__dict = CustomDict[str, str]({"Key1": "Value1"})


    @property
    def list(self) -> CustomList[str]:
        return self.__list
    @list.setter
    def list(self, value: CustomList[str]):
        self.__list = value


    @property
    def list1(self) -> CustomList[TestItem]:
        return self.__list1
    @list1.setter
    def list1(self, value: CustomList[TestItem]):
        self.__list1 = value


    @property
    def dict(self) -> CustomDict[str, str]:
        return self.__dict
    @dict.setter
    def dict(self, value: CustomDict[str, str]):
        self.__dict = value
