from lib import pytest_hidden
TEST = '''
from inventory import list_items
n = lambda xs: [x["name"] for x in xs]
def test_sort():
    assert n(list_items()) == ["bolt", "anvil", "chain"]
    assert n(list_items(sort_by="price")) == ["bolt", "chain", "anvil"]
    assert n(list_items(sort_by="name")) == ["anvil", "bolt", "chain"]
    assert n(list_items(sort_by="stock")) == ["anvil", "chain", "bolt"]
'''
def check(work, orig, answer):
    return pytest_hidden(work, TEST)
