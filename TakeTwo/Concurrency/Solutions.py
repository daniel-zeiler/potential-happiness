from typing import Callable
from threading import Lock, Barrier


class TrafficLight:
    def __init__(self):
        self.lock = Lock()
        self.green = 1

    def carArrived(
            self,
            carId: int,  # ID of the car
            roadId: int,  # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
            direction: int,  # Direction of the car
            turnGreen: 'Callable[[], None]',  # Use turnGreen() to turn light to green on current road
            crossCar: 'Callable[[], None]'  # Use crossCar() to make car cross the intersection
    ) -> None:
        with self.lock:
            if self.green != roadId:
                self.green = roadId
                turnGreen()
            crossCar()


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.barrier = Barrier(4)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 != 0:
                printFizz()
            self.barrier.wait()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 == 0:
                printBuzz()
            self.barrier.wait()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 == 0:
                printFizzBuzz()
            self.barrier.wait()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 != 0:
                printNumber(i)
            self.barrier.wait()


class Foo:
    def __init__(self):
        self.lock_one = Lock()
        self.lock_two = Lock()
        self.lock_one.acquire()
        self.lock_two.acquire()

    def first(self, print_first: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        print_first()
        self.lock_one.release()

    def second(self, print_second: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.lock_one:
            print_second()
            self.lock_two.release()

    def third(self, print_third: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.lock_two:
            print_third()


class FooBar:
    def __init__(self, n):
        self.n = n

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
