from lib import pytest_hidden
TEST = '''
from pager import paginate
def test_pages():
    items = list(range(25))
    assert paginate(items, 1) == list(range(10))
    assert paginate(items, 3) == [20, 21, 22, 23, 24]
    assert paginate(items, 2, per_page=5) == [5, 6, 7, 8, 9]
'''
def check(work, orig, answer):
    return pytest_hidden(work, TEST)
