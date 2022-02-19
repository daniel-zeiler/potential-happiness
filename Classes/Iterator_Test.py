from itertools import cycle, islice

"""
Iterator from another Iterator
Merge Iterator from list of iterators in Round Robin fashion
Merge Iterator from iterator of iterators in Round Robin fashion
Merge Iterator from iterator of iterators one after another
Step Iterator using start / end / step => Handle scenarios
Given a list of values, create a infinite cyclic iterator


A simple problem where I have iterate through list and print in interleaving fashion. I completed that easily. Then,
was asked to implement 2 classes(1 takes list as input while other takes (start, end, stepSize) as input) with
interator pattern and use them to solve original problem instead of foreach loop that I had used. Completed that too.
Then, was asked to create another iterator implementation that takes items of previous 2 types and iterates through
them in the original fashion. Partially completed that.
"""


def step(start, end, step_size):
    for i in range(start, end + 1, step_size):
        yield i


def round_robin(iterables):
    num_active = len(iterables)
    iter_cycle = cycle(iterables)
    while num_active:
        try:
            for iter in iter_cycle:
                yield next(iter)
        except StopIteration:
            num_active -= 1
            iter_cycle = cycle(islice(iter_cycle, num_active))

    # turn = 0
    # try:
    #     while True:
    #         if turn:
    #             turn = not turn
    #             yield next(gen_one)
    #         else:
    #             turn = not turn
    #             yield next(gen_two)
    # except StopIteration:
    #     for value in gen_two:
    #         yield value
    #     for value in gen_one:
    #         yield value


for value in cycle(round_robin([step(0, 200, 20), step(0, 20, 3), step(0, 20, 5)])):
    print(value)
