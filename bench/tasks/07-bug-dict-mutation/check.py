from lib import pytest_hidden
TEST = '''
from sessions import prune_expired
def test_prune():
    d = {"a": {"expires": 5}, "b": {"expires": 20}, "c": {"expires": 1}}
    out = prune_expired(d, 10)
    assert set(out) == {"b"}
    assert set(d) == {"b"}
'''
def check(work, orig, answer):
    return pytest_hidden(work, TEST)
