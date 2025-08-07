# pyright: basic
# ruff: noqa
from runtime.serialization import serializable
from typing import List, Dict, Optional, Set, Tuple
from datetime import datetime, date, time
from decimal import Decimal
from enum import Enum, IntFlag

#[str, int, float, bool, bytes, date, datetime, time, list, dict, List, Dict, Set, Enum, type]
class TestEnum(Enum):
    __test__ = False
    T1 = 1
    T2 = 2
    T3 = 3

class TestFlag(IntFlag):
    __test__ = False
    T1 = 1
    T2 = 2
    T3 = 4
    T4 = 8

@serializable(strict = True)
class TestType1:
    __test__ = False
    def __init__(self,
                 prop01: str = "Test",
                 prop02: int = 3465,
                 prop03: float = 35.64,
                 prop04: bool = True,
                 prop05: bytes = b'\x13\0\0\0\x08\0',
                 prop06: date = date(2010, 7, 15),
                 prop07: datetime = datetime(2017, 11, 3, 17, 45, 11),
                 prop08: time = time(9, 18, 27),
                 prop11: List[str] = [ "a", "b", "c"],
                 prop12: Dict[str, int] = { "a" : 1, "b" : 2, "c" : 3 },
                 prop13: str | None = "Test2",
                 prop14: TestEnum = TestEnum.T3,
                 prop15: TestFlag = TestFlag.T1 | TestFlag.T3,
                 prop16: Set[int] = { 7, 14, 21 },
                 prop17: Tuple[str, int] = ("test", 55),
                 prop18: Decimal = Decimal(32.65668),
                 prop19: Tuple[str, ...] = ("test", "abc"),
    ):
        self.__prop01 = prop01
        self.__prop02 = prop02
        self.__prop03 = prop03
        self.__prop04 = prop04
        self.__prop05 = prop05
        self.__prop06 = prop06
        self.__prop07 = prop07
        self.__prop08 = prop08
        self.__prop11 = prop11
        self.__prop12 = prop12
        self.__prop13 = prop13
        self.__prop14 = prop14
        self.__prop15 = prop15
        self.__prop16 = prop16
        self.__prop17 = prop17
        self.__prop18 = prop18
        self.__prop19 = prop19


    @property
    def prop01(self) -> str:
        return self.__prop01
    @prop01.setter
    def prop01(self, value: str):
        self.__prop01 = value

    @property
    def prop02(self) -> int:
        return self.__prop02
    @prop02.setter
    def prop02(self, value: int):
        self.__prop02 = value

    @property
    def prop03(self) -> float:
        return self.__prop03
    @prop03.setter
    def prop03(self, value: float):
        self.__prop03 = value

    @property
    def prop04(self) -> bool:
        return self.__prop04
    @prop04.setter
    def prop04(self, value: bool):
        self.__prop04 = value

    @property
    def prop05(self) -> bytes:
        return self.__prop05
    @prop05.setter
    def prop05(self, value: bytes):
        self.__prop05 = value

    @property
    def prop06(self) -> date:
        return self.__prop06
    @prop06.setter
    def prop06(self, value: date):
        self.__prop06 = value

    @property
    def prop07(self) -> datetime:
        return self.__prop07
    @prop07.setter
    def prop07(self, value: datetime):
        self.__prop07 = value

    @property
    def prop08(self) -> time:
        return self.__prop08
    @prop08.setter
    def prop08(self, value: time):
        self.__prop08 = value

    @property
    def prop11(self) -> List[str]:
        return self.__prop11
    @prop11.setter
    def prop11(self, value: List[str]):
        self.__prop11 = value

    @property
    def prop12(self) -> Dict[str, int]:
        return self.__prop12
    @prop12.setter
    def prop12(self, value: Dict[str, int]):
        self.__prop12 = value

    @property
    def prop13(self) -> str | None:
        return self.__prop13
    @prop13.setter
    def prop13(self, value: str):
        self.__prop13 = value

    @property
    def prop14(self) -> TestEnum:
        return self.__prop14
    @prop14.setter
    def prop14(self, value: TestEnum):
        self.__prop14 = value

    @property
    def prop15(self) -> TestFlag:
        return self.__prop15
    @prop15.setter
    def prop15(self, value: TestFlag):
        self.__prop15 = value


    @property
    def prop16(self) -> Set[int]:
        return self.__prop16
    @prop16.setter
    def prop16(self, value: Set[int]):
        self.__prop16 = value


    @property
    def prop17(self) -> Tuple[str, int]:
        return self.__prop17
    @prop17.setter
    def prop17(self, value: Tuple[str, int]):
        self.__prop17 = value


    @property
    def prop18(self) -> Decimal:
        return self.__prop18
    @prop18.setter
    def prop18(self, value: Decimal):
        self.__prop18 = value

    @property
    def prop19(self) -> tuple[str, ...]:
        return self.__prop19
    @prop19.setter
    def prop19(self, value: tuple[str, ...]):
        self.__prop19 = value

    def function1(self) -> str:
        return "Test"

    @classmethod
    def function2(cls) -> str:
        return "Test"

    @staticmethod
    def function3() -> str:
        return "Test"