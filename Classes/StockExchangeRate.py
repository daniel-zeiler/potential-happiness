import collections
import heapq


class User:
    def __init__(self, user_id):
        self.portfolio = collections.defaultdict(int)
        self.user_id = user_id
        self.money = 0
        self.open_orders = collections.defaultdict(Order)

    def deposit(self, value):
        self.money += value

    def withdraw(self, value):
        self.money = min(0, self.money - value)

    def create_buy_order(self, stock, value, quantity):
        if self.money >= quantity * value:
            self.money -= quantity * value
            return BuyOrder(stock.symbol, quantity, value, self.user_id)
        raise Exception("User does not have enough money to create this order")

    def create_sell_order(self, stock, value, quantity):
        if stock.symbol in self.portfolio and self.portfolio[stock.symbol] >= quantity:
            self.portfolio[stock.symbol] -= quantity
            return SellOrder(stock.symbol, quantity, value, self.user_id)
        raise Exception('User does not own enough %s' % stock.symbol)


class Order:
    def __init__(self, symbol, quantity, value, user_id):
        self.symbol = symbol
        self.value = value
        self.quantity = quantity
        self.fulfilled_quantity = 0
        self.user_id = user_id

    def update_order(self, quantity):
        pass


class SellOrder(Order):
    def __init__(self, symbol, quantity, value, user_id):
        super().__init__(symbol, quantity, value, user_id)


class BuyOrder(Order):
    def __init__(self, symbol, quantity, value, user_id):
        super().__init__(symbol, quantity, value, user_id)


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.buy_orders_heap = []
        self.sell_orders_heap = []

    def buy(self, quantity, value, user_id):
        while self.sell_orders_heap[0][0] < value and quantity > 0:
            if self.sell_orders_heap[0][1].quanity > quantity:
                self.sell_orders_heap[0][1].quanity -= quantity
                return 0
            else:
                quantity -= self.sell_orders_heap[0].pop()[1].quanity
        buy_order = BuyOrder(self.symbol, quantity, value, user_id)
        heapq.heappush(self.buy_orders_heap, (value, buy_order))

        return buy_order

    def sell(self, quantity, value, user_id):
        while self.buy_orders_heap[0][0] > value and quantity > 0:
            if self.buy_orders_heap[0][1].quanity > quantity:
                self.buy_orders_heap[0][1].quanity -= quantity
                return 0
            else:
                quantity -= self.sell_orders_heap[0].pop()[1].quanity
        sell_order = SellOrder(self.symbol, quantity, value, user_id)
        heapq.heappush(self.sell_orders_heap, (value, sell_order))

        return sell_order


class StockExchange:
    def __init__(self):
        self.stocks = collections.defaultdict(Stock)
        self.users = collections.defaultdict(User)

    def add_stock(self, symbol):
        self.stocks[symbol] = Stock(symbol)

    def process_buy_order(self, user_id, symbol, quantity, value):
        if user_id not in self.users or symbol not in self.stocks:
            return -1
        user = self.users[user_id]
        stock = self.stocks[symbol]
        buy_order = user.create_buy_order(stock, value, quantity)

    def process_sell_order(self, user_id, symbol, quantity, value):
        if user_id not in self.users or symbol not in self.stocks:
            return -1
        user = self.users[user_id]
        stock = self.stocks[symbol]
        sell_order = user.create_sell_order(stock, value, quantity)

    def process_transaction(self, sold, bought):
        pass
