import collections
from queue import PriorityQueue


class Order:
    def __init__(self, quantity, value, timestamp):
        self.quantity = quantity
        self.value = value
        self.timestamp = timestamp

    def __str__(self):
        return "value:%s quantity:%s" % (self.value, self.quantity)


class Listing:
    def __init__(self):
        self.buy_orders = PriorityQueue()
        self.sell_orders = PriorityQueue()

    def sell(self, order):
        while order.quantity > 0 and self.buy_orders.queue and self.buy_orders.queue[0][0] < order.value:
            value, timestamp, buy_order = self.buy_orders.queue[0]
            if buy_order.quantity <= order.quantity:
                order.quantity -= buy_order.quantity
                self.buy_orders.get()
            else:
                buy_order.quantity -= order.quantity
                order.quantity = 0
        if order.quantity > 0:
            self.sell_orders.put((order.value, order.timestamp, order))
            print('sell order remaining: ' + str(order))

    def buy(self, order):
        while order.quantity > 0 and self.sell_orders.queue and -self.sell_orders.queue[0][0] > order.value:
            value, timestamp, sell_order = self.sell_orders.queue[0]
            if sell_order.quantity <= order.quantity:
                order.quantity -= sell_order.quantity
                self.sell_orders.get()
            else:
                sell_order.quantity -= order.quantity
                order.quantity = 0
        if order.quantity > 0:
            self.buy_orders.put((-order.value, order.timestamp, order))
            print('buy order remaining: ' + str(order))


class StockExchange:
    def __init__(self):
        self.symbols = collections.defaultdict(Listing)

    def sell_stock(self, symbol, timestamp, quantity, value):
        if symbol in self.symbols:
            self.symbols[symbol].sell(Order(quantity, value, timestamp))

    def buy_stock(self, symbol, timestamp, quantity, value):
        if symbol in self.symbols:
            self.symbols[symbol].buy(Order(quantity, value, timestamp))

    def add_listing(self, symbol):
        self.symbols[symbol] = Listing()


stock_exchange = StockExchange()
symbols = ['SPY', 'COIN', 'RBN', 'UBER']
for symbol in symbols:
    stock_exchange.add_listing(symbol)

buy_orders = [['SPY', 1, 100, 100], ['SPY', 1, 100, 95]]
sell_orders = [['SPY', 1, 1, 99], ['SPY', 1, 200, 80]]

for buy, sell in zip(buy_orders, sell_orders):
    stock_exchange.buy_stock(buy[0], buy[1], buy[2], buy[3])
    stock_exchange.sell_stock(sell[0], sell[1], sell[2], sell[3])
