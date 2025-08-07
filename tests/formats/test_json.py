# pyright: basic
from pytest import fixture, raises as assert_raises
from json import loads
from os import path, makedirs
from shutil import rmtree

from runtime.serialization.json import Serializer, serialize, deserialize

from tests.formats.test_base import TestBase
from tests.classes.test_type1 import TestType1

@fixture(scope = "class")
def base():
    type = "json"
    testpath = "tests/testdata/json"

    def cleanup():
        if path.isdir(testpath):
            rmtree(testpath)

    cleanup()

    if not path.isdir(testpath):
        makedirs(testpath)

    yield TestBase(type, testpath, serialize, deserialize) # pyright: ignore[reportArgumentType]

    cleanup()



def test_serialization(base: TestBase):
    for serialized in base.serializations.values():
        assert is_json(serialized)

def test_serialization_to_file(base: TestBase):
    for cls, obj in base.serializables.items():
        serializer = Serializer[cls]()

        ser1 = serializer.dumps(obj)
        with open(path.join(base.testpath, f"test.{base.type}"), "wt+", encoding="utf8") as fp:
            serializer.dump(obj, fp, overwrite=True)
            fp.seek(0)
            deser = serializer.load(fp)
            ser2 = serializer.dumps(deser)
            assert ser1 == ser2

        if cls == TestType1:
            serializer.dump(obj, path.join(base.testpath, f"example.{base.type}"), overwrite=True)
            with assert_raises(FileExistsError):
                serializer.dump(obj, path.join(base.testpath, f"example.{base.type}"))
            serializer.dump(obj, path.join(base.testpath, f"example.{base.type}"), overwrite=True)
        deserialized = serializer.load(path.join(base.testpath, f"test.{base.type}"))
        base._test_deserialization(cls, obj, deserialized)

def test_dumps():
    serializer = Serializer[TestType1]()
    inst = TestType1()
    ser = serializer.dumps(inst)
    deser = serializer.loads(ser)
    reser = serializer.dumps(deser)
    assert ser == reser

def test_pretty_print():
    serializer = Serializer[TestType1]()
    inst = TestType1()
    ser1 = serializer.serialize(inst, pretty_print=True)
    ser2 = serializer.serialize(inst, pretty_print=False)
    assert ser1 != ser2
    assert len(ser1) > len(ser2)

    ser3 = serializer.dumps(inst, pretty_print=True)
    ser4 = serializer.dumps(inst, pretty_print=False)
    assert ser1 != ser2
    assert len(ser1) > len(ser2)

def test_base_serialization(base: TestBase):
    base.test_base_serialization()

def test_untyped_serialization(base: TestBase):
    base.test_untyped_serialization()

def test_deserialization(base: TestBase):
    base.test_deserialization()

def is_json(data: str):
    try:
        _ = loads(data)
        return True
    except ValueError:
        print(data)
        return False
