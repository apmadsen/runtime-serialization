# pyright: basic
from pytest import fixture
from dataclasses import dataclass
from datetime import datetime, date
from typing import TypeVar, Generic, cast, Any, Optional, List, Dict, Mapping, Set, Tuple, Union
from enum import Enum
import numpy
from delegate.pattern import delegate
from delegate.events import Event, Channel

from tests.classes.test_type1 import TestEnum, TestType1
from tests.classes.test_type2 import TestType2
from tests.classes.test_type3 import TestType3
from tests.classes.test_type4 import TestType4
from tests.classes.test_type5 import TestType5
from tests.classes.test_type6 import TestType6
from tests.classes.test_type7_8 import TestType7, TestType8
from tests.classes.generic_type import GenericType
from tests.classes.custom_list import CustomList, CustomSequence
from tests.classes.custom_dict import CustomDict, CustomMapping
from tests.classes.custom_set import CustomSet

@fixture(scope = "package")
def serializable_types():
    yield [
        TestType1(),
        TestType2(456.32, datetime.now(), {'asghdfj':'yhhd'}, TestType1(), b'CA0F'),
        TestType3(),
        TestType4(),
        TestType5(),
        TestType6("Test", 3457, 436.65),
        TestType7(CustomList([TestType8(4568569)])),
        Tuple[str],
        Tuple[str, int],
        list,
        List[str],
        set,
        Set[str],
        dict,
        Dict[str, int],
        Mapping[str, int],
        Union[str, int],
        Union[str, int, None],
        str | None,
        TestEnum,
        CustomList[str],
        CustomDict[str, int],
        CustomMapping[str, int],
        CustomSequence[str],
        CustomSet[str],
        # GenericType,
        # GenericType[str]
    ]

@fixture(scope = "package")
def serializables():
    yield [
        TestType1(),
        TestType2(456.32, datetime.now(), {'asghdfj':'yhhd'}, TestType1(), b'CA0F'),
        TestType3(),
        TestType4(),
        TestType5(),
        TestType6("Test", 3457, 436.65),
        TestType7(CustomList([TestType8(4568569)]))
    ]
