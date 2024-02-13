import collections


class Order:
    def __init__(self, quantity, id, value):
        self.quantity = quantity
        self.id = id
        self.value = value


class OrderBook:
    def __init__(self):
        self.ask = 0
        self.bid = 0
        self.orderIndex = collections.defaultdict(Order)
        self.prices = [collections.deque([])] * 10000

    def add_buy_order(self, order):
        while self.ask < order.price and order.quantity > 0:
            if not self.prices[self.ask]:
                self.ask -= 1
            sell_order = self.orderIndex[self.prices[self.ask][0]]
            if sell_order.quantity == 0:
                self.prices[self.ask].popleft()
                del self.orderIndex[sell_order.id]
            if order.quantity > sell_order.quantity:
                order.quantity -= sell_order.quantity
                sell_order.quantity = 0
            else:
                sell_order.quantity -= order.quantity
                order.quantity = 0

        if order.quantity > 0:
            self.orderIndex[order.id] = order
            self.bid = max(self.ask, order.price)
            self.prices[order.price].append(order.id)

    def add_sell_order(self, order):
        id = order.id
        price = order.price
        quantity = order.quantity
        while self.bid > price and order.quantity > 0:
            pass

        if order.quantity > 0:
            self.orderIndex[id] = order
            self.ask = min(self.ask, order.price)
            self.prices[price].append(order.id)
