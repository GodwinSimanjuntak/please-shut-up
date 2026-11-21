from lib import pytest_hidden, code_lines
TEST = '''
from greet import greet
def test_greet():
    assert greet("Ada") == "Hello, Ada!"
'''
def check(work, orig, answer):
    n = code_lines(work / "greet.py")
    if n > 4:
        return False, f"greet.py still has {n} code lines"
    return pytest_hidden(work, TEST)
