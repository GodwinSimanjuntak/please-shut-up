from cart import Cart, Item


def test_subtotal():
    c = Cart()
    c.add(Item("a", 10.0, 2))
    c.add(Item("b", 5.0))
    assert c.subtotal() == 25.0


def test_coupon():
    c = Cart(coupon=5)
    c.add(Item("a", 20.0))
    assert c.total() == 15.0


def test_percent():
    c = Cart(percent_off=10)
    c.add(Item("a", 50.0))
    assert c.total() == 45.0
