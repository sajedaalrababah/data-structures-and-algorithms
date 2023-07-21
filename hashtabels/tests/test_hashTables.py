import pytest
from hashTables import Hashtable

def test_set_and_get():
    ht = Hashtable()
    ht.set("key1", "value1")
    assert ht.get("key1") == "value1"


def test_set_replaces_existing_key():
    ht = Hashtable()
    ht.set("key1", "value1")
    ht.set("key1", "value2")
    assert ht.get("key1") == "value2"


def test_get_nonexistent_key():
    ht = Hashtable()
    assert ht.get("key1") is None


def test_has_existing_key():
    ht = Hashtable()
    ht.set("key1", "value1")
    assert ht.has("key1") is True


def test_has_nonexistent_key():
    ht = Hashtable()
    assert ht.has("key1") is False


def test_keys():
    ht = Hashtable()
    ht.set("key1", "value1")
    ht.set("key2", "value2")
    ht.set("key3", "value3")
    keys = ht.keys()
    assert "key1" in keys
    assert "key2" in keys
    assert "key3" in keys
    assert len(keys) == 3


def test_collision_handling():
    ht = Hashtable(size=1)  # Force collision with a small size
    ht.set("key1", "value1")
    ht.set("key2", "value2")
    assert ht.get("key1") == "value1"
    assert ht.get("key2") == "value2"


def test_retrieve_collision_value():
    ht = Hashtable(size=1)  # Force collision with a small size
    ht.set("key1", "value1")
    ht.set("key2", "value2")
    assert ht.get("key1") == "value1"
    assert ht.get("key2") == "value2"


def test_hash():
    ht = Hashtable()
    assert ht.hash("key1") >= 0
    assert ht.hash("key1") < ht.size


# Run the tests
pytest.main(["-v"])