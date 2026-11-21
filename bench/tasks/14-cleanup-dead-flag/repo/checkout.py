ENABLE_NEW_CHECKOUT = True  # rolled out to 100% in March


def _old_checkout(cart):
    total = 0
    for item in cart:
        total += item["price"] * item["qty"]
    if total > 100:
        total = total * 0.95
    return {"total": round(total, 2), "version": "old"}


def _new_checkout(cart):
    total = sum(i["price"] * i["qty"] for i in cart)
    return {"total": round(total, 2), "version": "new"}


def checkout(cart):
    if ENABLE_NEW_CHECKOUT:
        return _new_checkout(cart)
    return _old_checkout(cart)
