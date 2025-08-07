# pyright: basic
from pytest import fixture, raises as assert_raises
from os import path, makedirs
from shutil import rmtree

from runtime.serialization.toml import Serializer, serialize, deserialize

from tests.formats.test_base import TestBase
from tests.classes.test_type1 import TestType1

@fixture(scope = "class")
def base():
    type = "toml"
    testpath = "tests/testdata/toml"

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
        assert is_toml(serialized)

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

def test_base_serialization(base: TestBase):
    base.test_base_serialization()

def test_untyped_serialization(base: TestBase):
    base.test_untyped_serialization()

def test_deserialization(base: TestBase):
    base.test_deserialization()


def is_toml(data: str):
    try:
        from toml import loads
        _ = loads(data)
        return True
    except ValueError:
        return False
