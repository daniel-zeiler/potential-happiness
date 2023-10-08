import collections
import heapq


class Order:
    def __init__(self, quantity, value, stock_name, user_id):
        self.value = value
        self.quantity = quantity
        self.stock_name = stock_name
        self.user_id = user_id


class Listing:
    def __init__(self, stock_name):
        self.stock_name = stock_name
        self.buy_orders = []
        self.sell_orders = []

    def current_price(self):
        if not self.buy_orders or not self.sell_orders:
            return float('inf')
        buy_order = self.buy_orders[0][1]
        sell_order = self.sell_orders[0][1]
        return (buy_order.value * buy_order.quantity + sell_order.value * sell_order.quantity) / \
               (buy_order.quantity + sell_order.quantity)

    def buy(self, order):
        if self.sell_orders:
            sell_order = self.sell_orders[0][1]
            while sell_order and sell_order.value < order.value and order.quantity > 0:
                if sell_order.quantity < order.quantity:
                    order.quantity -= heapq.heappop(self.sell_orders)[1].quantity
                    if not self.sell_orders:
                        break
                    sell_order = self.sell_orders[0][1]
                else:
                    sell_order.quantity -= order.quantity
                    order.quantity = 0

        if order.quantity > 0:
            heapq.heappush(self.buy_orders, (-order.value, order))

    def sell(self, order):
        if self.buy_orders:
            buy_order = self.buy_orders[0][1]
            while buy_order and buy_order.value > order.value and order.quantity > 0:
                if buy_order.quantity < order.quantity:
                    order.quantity -= heapq.heappop(self.buy_orders)[1].quantity
                    if not self.buy_orders:
                        break
                    buy_order = self.buy_orders[0][1]
                else:
                    buy_order.quantity -= order.quantity
                    order.quantity = 0

        if order.quantity > 0:
            heapq.heappush(self.sell_orders, (order.value, order))


class Stock:
    def __init__(self, stock_name, user_id, quantity):
        self.stock_name = stock_name
        self.user_id = user_id
        self.quantity = quantity


class User:
    def __init__(self, user_id):
        self.portfolio = collections.defaultdict(Stock)
        self.money = 0
        self.user_id = user_id

    def sell(self, value, quantity, stock_name):
        order = Order(quantity, value, stock_name, self.user_id)
        # validate order
        return order

    def buy(self, value, quantity, stock_name):
        order = Order(quantity, value, stock_name, self.user_id)
        # validate order
        return order


class StockExchange:
    def __init__(self):
        self.listings = collections.defaultdict(Listing)
        self.users = collections.defaultdict(User)

    def add_user(self, user_id):
        self.users[user_id] = User(user_id)
        return self.users[user_id]

    def add_listing(self, stock_name):
        self.listings[stock_name] = Listing(stock_name)

    def buy_order(self, order):
        if order.stock_name in self.listings:
            stock = self.listings[order.stock_name]
            stock.buy(order)
            print(stock.current_price())

    def sell_order(self, order):
        if order.stock_name in self.listings:
            stock = self.listings[order.stock_name]
            stock.sell(order)
            print(stock.current_price())


stock_exchange = StockExchange()
stock_exchange.add_listing('COIN')
user_one = stock_exchange.add_user('USER_ONE')
user_two = stock_exchange.add_user('USER_TWO')
stock_exchange.sell_order(user_one.sell(102, 100, 'COIN'))
stock_exchange.buy_order(user_two.buy(100, 100, 'COIN'))
stock_exchange.buy_order(user_two.buy(99, 100, 'COIN'))
stock_exchange.buy_order(user_two.buy(98, 100, 'COIN'))
stock_exchange.buy_order(user_two.buy(97, 100, 'COIN'))
stock_exchange.buy_order(user_two.buy(5, 100000, 'COIN'))
stock_exchange.sell_order(user_one.sell(75, 2000, 'COIN'))
stock_exchange.sell_order(user_one.sell(200, 100, 'COIN'))
stock_exchange.buy_order(user_two.buy(55, 1000, 'COIN'))
