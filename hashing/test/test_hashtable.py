import pytest
from linkedlist.hashing import hashtable
from linkedlist.hashing.hashtable import HashTable, BLANK

@pytest.fixture()
def hash_table():
    sample_data = hashtable.HashTable(capacity=100)
    sample_data["hola"] = "hello"
    sample_data[98.6] = 37
    sample_data[False] = True
    return sample_data

def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None

def test_should_create_empty_value_slots():
    assert HashTable(capacity=3).pairs == 3*[BLANK]

def test_should_insert_key_value_pairs(hash_table):

    assert ("hola", "hello") in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs

    assert len(hash_table) == 100

@pytest.mark.skip
def test_should_not_shrink_when_removing_elements():
    pass

def test_should_not_contain_none_value_when_created():
    hash_table = hashtable.HashTable(capacity=100)
    values = [pair.value for pair in hash_table.pairs if pair]
    assert None not in values

@pytest.mark.skip
def test_should_insert_none_value():
    hash_table = HashTable(capacity=100)
    hash_table["hola"] = None
    assert None in hash_table

def test_should_raise_error_on_missing_key():
    hash_table = HashTable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"

def test_should_find_key(hash_table):
    assert "hola" in hash_table

def test_should_not_find_key(hash_table):
    assert "missing_key" not in hash_table

def test_should_get_value(hash_table):
    assert hash_table.get("hola") == "hello"

def test_should_get_none_when_missing_key(hash_table):
    assert hash_table.get("missing_key") is None

def test_should_get_default_value_when_missing_key(hash_table):
    assert hash_table.get("missing_key", "default") == "default"

def test_should_get_value_with_default(hash_table):
    assert hash_table.get("hola", "default") == "hello"

def test_should_delete_key_value_pair(hash_table):
    assert ("hola", "hello") in hash_table.pairs
    assert len(hash_table) == 100

    del hash_table["hola"]

    assert ("hola", "hello") not in hash_table.pairs
    assert len(hash_table) == 100

def test_should_raise_key_error_when_deleting(hash_table):
    with pytest.raises(KeyError) as execption_info:
        del hash_table["missing_key"]
    assert execption_info.value.args[0] == "missing_key"

def test_should_update_value(hash_table):
    assert hash_table["hola"] == "hello"
    hash_table["hola"] = "hallo"

    assert hash_table["hola"] == "hallo"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True
    assert len(hash_table) == 100

def test_should_return_pairs(hash_table):
    assert ("hola", "hallo") in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs