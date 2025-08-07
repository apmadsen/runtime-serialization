# pyright: basic
# ruff: noqa
from runtime.serialization import serializable
from dataclasses import dataclass

@serializable
@dataclass
class TestType6:
    __test__ = False

    prop1: str
    prop2: int
    prop3: float
