# 3 problems

"""
You're given a list of n integers arr[0...(n-1)]. You must compute a list output[0...(n-1)] such that,
for each index i (between 0 and n-1, inclusive), output[i] is equal to the product of the three largest elements out
of arr[0...i] (or equal to -1 if i < 2, as arr[0...i] then includes fewer than three elements). Note that the three
largest elements used to form any product may have the same values as one another, but they must be at different
indices in arr. Signature int[] findMaxProduct(int[] arr) Input n is in the range [1, 100,000]. Each value arr[i] is
in the range [1, 1,000]. Output Return a list of n integers output[0...(n-1)], as described above. Example 1 n = 5 arr
= [1, 2, 3, 4, 5] output = [-1, -1, 6, 24, 60] The 3rd element of output is 3*2*1 = 6, the 4th is 4*3*2 = 24,
and the 5th is 5*4*3 = 60. Example 2 n = 5 arr = [2, 1, 2, 1, 2] output = [-1, -1, 4, 4, 8] The 3rd element of output
is 2*2*1 = 4, the 4th is 2*2*1 = 4, and the 5th is 2*2*2 = 8.
"""


def findMaxProduct(arr):
    pass


"""The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle 
value and the median is the mean of the two middle values. 

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object. void addNum(int num) adds the integer num from the data stream to 
the data structure. double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual 
answer will be accepted. 
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 
"""


class MedianFinder:

    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

"""
You want to schedule a certain number of trips with a collection of several cabs.

Given an integer n representing a desired number of trips, and an array cabTravelTime representing your cabs and how 
long it takes each cab (at that index of the array) to make a trip, return the minimum time required to make n trips. 

Assume that cabs can run simultaneously and there is no waiting period between trips. There may be multiple cabs with 
the same time cost.* 

Examples If n=3 and cabTravelTime=[1,2], then the answer is 2. This is because the first cab (index 0, cost 1) can 
make 2 trips costing a total of 2 time units, and the second cab can make a single trip costing 2 at the same time. 

n=10
cabTravelTime=[1,3,5,7,8]

* 7 trips with cab 0 (cost 1)
* 2 trips with cab 1 (cost 3)
* 1 trip with cab 2 (cost 5)
So, answer is 7 (there could be other combinations)

n=3
cabTravelTime=[3,4,8]

* 2 trips with cab 0 (cost 6)
* 1 trip with cab 1 (cost 4)
Time = 6
"""


def number_of_cabs(n, cabTravelTime):
    pass


"""
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted
order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays.
For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also,
we wouldn't include intervals like [5, 5] in our answer, as they have zero length.



Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
"""
import heapq


# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


def employeeFreeTime(schedule: '[[Interval]]') -> '[Interval]':
    pass
