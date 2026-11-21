from lib import pytest_hidden
TEST = '''
from cart import Cart, Item
def test_big_coupon():
    c = Cart(coupon=100); c.add(Item("a", 20.0)); assert c.total() == 0
def test_coupon():
    c = Cart(coupon=5); c.add(Item("a", 20.0)); assert c.total() == 15.0
def test_percent():
    c = Cart(percent_off=10); c.add(Item("a", 50.0)); assert c.total() == 45.0
'''
def check(work, orig, answer):
    return pytest_hidden(work, TEST)
