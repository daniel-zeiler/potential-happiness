from threading import Lock, Condition

"""
There is an intersection of two roads. First road is road A where cars travel from North to South in direction 1
and from South to North in direction 2. Second road is road B where cars travel from West to East in direction 3 and
from East to West in direction 4.



There is a traffic light located on each road before the intersection. A traffic light can either be green or red.

Green means cars can cross the intersection in both directions of the road. Red means cars in both directions cannot
cross the intersection and must wait until the light turns green. The traffic lights cannot be green on both roads at
the same time. That means when the light is green on road A, it is red on road B and when the light is green on road
B, it is red on road A.

Initially, the traffic light is green on road A and red on road B. When the light is green on one road, all cars can
cross the intersection in both directions until the light becomes green on the other road. No two cars traveling on
different roads should cross at the same time.

Design a deadlock-free traffic light controlled system at this intersection.

Implement the function void carArrived(carId, roadId, direction, turnGreen, crossCar) where:

carId is the id of the car that arrived. roadId is the id of the road that the car travels on. direction is the
direction of the car. turnGreen is a function you can call to turn the traffic light to green on the current road.
crossCar is a function you can call to let the current car cross the intersection. Your answer is considered correct
if it avoids cars deadlock in the intersection. Turning the light green on a road when it was already green is
considered a wrong answer.



Example 1:

Input: cars = [1,3,5,2,4], directions = [2,1,2,4,3], arrivalTimes = [10,20,30,40,50]
Output: [
"Car 1 Has Passed Road A In Direction 2",    // Traffic light on road A is green, car 1 can cross the intersection.
"Car 3 Has Passed Road A In Direction 1",    // Car 3 crosses the intersection as the light is still green.
"Car 5 Has Passed Road A In Direction 2",    // Car 5 crosses the intersection as the light is still green.
"Traffic Light On Road B Is Green",          // Car 2 requests green light for road B.
"Car 2 Has Passed Road B In Direction 4",    // Car 2 crosses as the light is green on road B now.
"Car 4 Has Passed Road B In Direction 3"     // Car 4 crosses the intersection as the light is still green.
]
Example 2:

Input: cars = [1,2,3,4,5], directions = [2,4,3,3,1], arrivalTimes = [10,20,30,40,40] Output: [ "Car 1 Has Passed Road
A In Direction 2",    // Traffic light on road A is green, car 1 can cross the intersection. "Traffic Light On Road B
Is Green",          // Car 2 requests green light for road B. "Car 2 Has Passed Road B In Direction 4",
// Car 2 crosses as the light is green on road B now. "Car 3 Has Passed Road B In Direction 3",    // Car 3 crosses
as the light is green on road B now. "Traffic Light On Road A Is Green",          // Car 5 requests green light for
road A. "Car 5 Has Passed Road A In Direction 1",    // Car 5 crosses as the light is green on road A now. "Traffic
Light On Road B Is Green",          // Car 4 requests green light for road B. Car 4 blocked until car 5 crosses and
then traffic light is green on road B. "Car 4 Has Passed Road B In Direction 3"     // Car 4 crosses as the light is
green on road B now. ] Explanation: This is a dead-lock free scenario. Note that the scenario when car 4 crosses
before turning light into green on road A and allowing car 5 to pass is also correct and Accepted scenario. """
from typing import Callable


class TrafficLight:
    def __init__(self):
        pass

    def carArrived(
            self,
            carId: int,  # ID of the car
            roadId: int,  # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
            direction: int,  # Direction of the car
            turnGreen: 'Callable[[], None]',  # Use turnGreen() to turn light to green on current road
            crossCar: 'Callable[[], None]'  # Use crossCar() to make car cross the intersection
    ) -> None:
        pass


"""
You have the four functions:

printFizz that prints the word "fizz" to the console,
printBuzz that prints the word "buzz" to the console,
printFizzBuzz that prints the word "fizzbuzz" to the console, and
printNumber that prints a given integer to the console.
You are given an instance of the class FizzBuzz that has four functions: fizz, buzz, fizzbuzz and number. The same instance of FizzBuzz will be passed to four different threads:

Thread A: calls fizz() that should output the word "fizz".
Thread B: calls buzz() that should output the word "buzz".
Thread C: calls fizzbuzz() that should output the word "fizzbuzz".
Thread D: calls number() that should only output the integers.
Modify the given class to output the series [1, 2, "fizz", 4, "buzz", ...] where the ith token (1-indexed) of the series is:

"fizzbuzz" if i is divisible by 3 and 5,
"fizz" if i is divisible by 3 and not 5,
"buzz" if i is divisible by 5 and not 3, or
i if i is not divisible by 3 or 5.
Implement the FizzBuzz class:

FizzBuzz(int n) Initializes the object with the number n that represents the length of the sequence that should be printed.
void fizz(printFizz) Calls printFizz to output "fizz".
void buzz(printBuzz) Calls printBuzz to output "buzz".
void fizzbuzz(printFizzBuzz) Calls printFizzBuzz to output "fizzbuzz".
void number(printNumber) Calls printnumber to output the numbers.
 

Example 1:

Input: n = 15
Output: [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11,"fizz",13,14,"fizzbuzz"]
Example 2:

Input: n = 5
Output: [1,2,"fizz",4,"buzz"]
"""


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        pass

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        pass

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        pass

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        pass


"""
Suppose we have a class:

public class Foo { public void first() { print("first"); } public void second() { print("second"); } public void 
third() { print("third"); } } The same instance of Foo will be passed to three different threads. Thread A will call 
first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to 
ensure that second() is executed after first(), and third() is executed after second(). 

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem 
to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness. 



Example 1:

Input: nums = [1,2,3] Output: "firstsecondthird" Explanation: There are three threads being fired asynchronously. The 
input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" 
is the correct output. Example 2: 

Input: nums = [1,3,2] Output: "firstsecondthird" Explanation: The input [1,3,2] means thread A calls first(), 
thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output. 


Constraints:

nums is a permutation of [1, 2, 3].
"""


class Foo:
    def __init__(self):
        pass

    def first(self, print_first: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        print_first()

    def second(self, print_second: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        print_second()

    def third(self, print_third: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        print_third()


"""
Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
The same instance of FooBar will be passed to two different threads:

thread A will call foo(), while
thread B will call bar().
Modify the given program to output "foobar" n times.

 

Example 1:

Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
"foobar" is being output 1 time.
Example 2:

Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.
"""


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


"""
You have a function printNumber that can be called with an integer parameter and prints it to the console.

For example, calling printNumber(7) prints 7 to the console.
You are given an instance of the class ZeroEvenOdd that has three functions: zero, even, and odd. The same instance of ZeroEvenOdd will be passed to three different threads:

Thread A: calls zero() that should only output 0's.
Thread B: calls even() that should only output even numbers.
Thread C: calls odd() that should only output odd numbers.
Modify the given class to output the series "010203040506..." where the length of the series must be 2n.

Implement the ZeroEvenOdd class:

ZeroEvenOdd(int n) Initializes the object with the number n that represents the numbers that should be printed.
void zero(printNumber) Calls printNumber to output one zero.
void even(printNumber) Calls printNumber to output one even number.
void odd(printNumber) Calls printNumber to output one odd number.
 

Example 1:

Input: n = 2
Output: "0102"
Explanation: There are three threads being fired asynchronously.
One of them calls zero(), the other calls even(), and the last one calls odd().
"0102" is the correct output.
Example 2:

Input: n = 5
Output: "0102030405"
"""


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        pass

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        pass

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        pass


"""
There are two kinds of threads: oxygen and hydrogen. Your goal is to group these threads to form water molecules.

There is a barrier where each thread has to wait until a complete molecule can be formed. Hydrogen and oxygen threads 
will be given releaseHydrogen and releaseOxygen methods respectively, which will allow them to pass the barrier. 
These threads should pass the barrier in groups of three, and they must immediately bond with each other to form a 
water molecule. You must guarantee that all the threads from one molecule bond before any other threads from the next 
molecule do. 

In other words:

If an oxygen thread arrives at the barrier when no hydrogen threads are present, it must wait for two hydrogen 
threads. If a hydrogen thread arrives at the barrier when no other threads are present, it must wait for an oxygen 
thread and another hydrogen thread. We do not have to worry about matching the threads up explicitly; the threads do 
not necessarily know which other threads they are paired up with. The key is that threads pass the barriers in 
complete sets; thus, if we examine the sequence of threads that bind and divide them into groups of three, 
each group should contain one oxygen and two hydrogen threads. 

Write synchronization code for oxygen and hydrogen molecules that enforces these constraints.



Example 1:

Input: water = "HOH"
Output: "HHO"
Explanation: "HOH" and "OHH" are also valid answers.
Example 2:

Input: water = "OOHHHH"
Output: "HHOHHO"
Explanation: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" and "OHHOHH" are also valid answers.
"""


class H2O:
    def __init__(self):
        pass

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()


"""
Five silent philosophers sit at a round table with bowls of spaghetti. Forks are placed between each pair of 
adjacent philosophers. 

Each philosopher must alternately think and eat. However, a philosopher can only eat spaghetti when they have both 
left and right forks. Each fork can be held by only one philosopher and so a philosopher can use the fork only if it 
is not being used by another philosopher. After an individual philosopher finishes eating, they need to put down both 
forks so that the forks become available to others. A philosopher can take the fork on their right or the one on 
their left as they become available, but cannot start eating before getting both forks. 

Eating is not limited by the remaining amounts of spaghetti or stomach space; an infinite supply and an infinite 
demand are assumed. 

Design a discipline of behaviour (a concurrent algorithm) such that no philosopher will starve; i.e., 
each can forever continue to alternate between eating and thinking, assuming that no philosopher can know when others 
may want to eat or think. 



The problem statement and the image above are taken from wikipedia.org

 

The philosophers' ids are numbered from 0 to 4 in a clockwise order. Implement the function void wantsToEat(
philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork) where: 

philosopher is the id of the philosopher who wants to eat. pickLeftFork and pickRightFork are functions you can call 
to pick the corresponding forks of that philosopher. eat is a function you can call to let the philosopher eat once 
he has picked both forks. putLeftFork and putRightFork are functions you can call to put down the corresponding forks 
of that philosopher. The philosophers are assumed to be thinking as long as they are not asking to eat (the function 
is not being called with their number). Five threads, each representing a philosopher, will simultaneously use one 
object of your class to simulate the process. The function may be called for the same philosopher more than once, 
even before the last call ends. 

 

Example 1:

Input: n = 1 Output: [[4,2,1],[4,1,1],[0,1,1],[2,2,1],[2,1,1],[2,0,3],[2,1,2],[2,2,2],[4,0,3],[4,1,2],[0,2,1],[4,2,
2],[3,2,1],[3,1,1],[0,0,3],[0,1,2],[0,2,2],[1,2,1],[1,1,1],[3,0,3],[3,1,2],[3,2,2],[1,0,3],[1,1,2],[1,2,
2]] Explanation: n is the number of times each philosopher will call the function. The output array describes the 
calls you made to the functions controlling the forks and the eat function, its format is: output[i] = [a, b, 
c] (three integers) - a is the id of a philosopher. - b specifies the fork: {1 : left, 2 : right}. - c specifies the 
operation: {1 : pick, 2 : put, 3 : eat}. 
"""


class DiningPhilosophers:

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        pass
