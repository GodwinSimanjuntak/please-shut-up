from lib import pytest_hidden
TEST = '''
from checkout import checkout
def test_new():
    assert checkout([{"price": 60, "qty": 2}]) == {"total": 120, "version": "new"}
'''
def check(work, orig, answer):
    src = (work / "checkout.py").read_text()
    for name in ["_old_checkout", "ENABLE_NEW_CHECKOUT"]:
        if name in src:
            return False, f"{name} still in checkout.py"
    return pytest_hidden(work, TEST)
