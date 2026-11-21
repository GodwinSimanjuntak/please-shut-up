from lib import pytest_hidden
TEST = '''
from posts import add_tag, make_post
def test_independent():
    assert add_tag({}, "a")["tags"] == ["a"]
    assert add_tag({}, "b")["tags"] == ["b"]
def test_make_post():
    assert make_post("x", "a", "b")["tags"] == ["a", "b"]
    assert make_post("y", "c")["tags"] == ["c"]
'''
def check(work, orig, answer):
    return pytest_hidden(work, TEST)
