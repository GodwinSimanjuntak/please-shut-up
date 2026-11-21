from lib import pytest_hidden
TEST = '''
from receipt import format_total
def test_format():
    assert format_total([0.1, 0.2]) == "$0.30"
    assert format_total([5]) == "$5.00"
    assert format_total([]) == "$0.00"
    assert format_total([19.999]) == "$20.00"
'''
def check(work, orig, answer):
    return pytest_hidden(work, TEST)
