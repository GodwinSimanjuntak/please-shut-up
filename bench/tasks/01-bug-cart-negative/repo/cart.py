from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    price: float
    qty: int = 1


@dataclass
class Cart:
    items: list = field(default_factory=list)
    coupon: float = 0.0  # flat amount off
    percent_off: float = 0.0

    def add(self, item):
        self.items.append(item)

    def subtotal(self):
        return sum(i.price * i.qty for i in self.items)

    def total(self):
        sub = self.subtotal()
        sub = sub - self.coupon
        sub = sub - sub * self.percent_off / 100
        return round(sub, 2)
