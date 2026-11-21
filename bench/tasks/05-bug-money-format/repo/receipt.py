def format_total(prices):
    total = sum(prices)
    return "$" + str(total)


def receipt(lines):
    out = [f"{name}: ${price}" for name, price in lines]
    out.append("Total: " + format_total([p for _, p in lines]))
    return "\n".join(out)
