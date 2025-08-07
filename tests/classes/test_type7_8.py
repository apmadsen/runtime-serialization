# pyright: basic
# ruff: noqa
from __future__ import annotations
from runtime.serialization import serializable
from dataclasses import dataclass

from tests.classes.custom_list import CustomList


@serializable
@dataclass
class TestType8:
    __test__ = False

    prop1: int



@serializable
@dataclass
class TestType7:
    __test__ = False

    prop1: CustomList[TestType8]
