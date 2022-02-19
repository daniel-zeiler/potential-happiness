from typing import Iterable, List


class RoundRobinIterator:
    def __init__(self, iterables: List[Iterable]):
        self.iterables = iterables
        self.pointer = 0

    def iterate(self):
        while self.iterables:
            self.pointer = self.pointer % len(self.iterables)
            try:
                value = next(self.iterables[self.pointer])
                self.pointer = self.pointer + 1
                yield value
            except StopIteration:
                self.iterables = self.iterables[:self.pointer] + self.iterables[self.pointer + 1:]


class StepIterator:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def step_in(self):
        for value in range(self.start, self.stop + 1, self.step):
            yield value


class InfiniteIterator:
    def __init__(self, iterable: Iterable):
        self.saved = []
        self.iterable = iterable

    def cycle(self):
        for element in self.iterable:
            self.saved.append(element)
            yield element
        while self.saved:
            for element in self.saved:
                yield element


for value in RoundRobinIterator([
    InfiniteIterator(StepIterator(0, 100, 20).step_in()).cycle(),
    InfiniteIterator(StepIterator(0, 100, 20).step_in()).cycle()
]).iterate():
    print(value)
