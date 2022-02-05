from typing import List

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""


def merge(intervals: List[List[int]]) -> List[List[int]]:
    pass


"""
Design a stack which supports the following operations.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of 
elements in the stack or do nothing if the stack reached the maxSize.
void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
int pop() Pops and returns the top of stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less 
than k elements in the stack, just increment all the elements in the stack.
 

Example 1:

Input
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop",
"pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
Explanation
CustomStack customStack = new CustomStack(3); // Stack is Empty []
customStack.push(1);                          // stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.pop();                            // return 2 --> Return top of the stack 2, 
stack becomes [1]
customStack.push(2);                          // stack becomes [1, 2]
customStack.push(3);                          // stack becomes [1, 2, 3]
customStack.push(4);                          // stack still [1, 2, 3], Don't add another 
elements as size is 4
customStack.increment(5, 100);                // stack becomes [101, 102, 103]
customStack.increment(2, 100);                // stack becomes [201, 202, 103]
customStack.pop();                            // return 103 --> Return top of the stack 103, 
stack becomes [201, 202]
customStack.pop();                            // return 202 --> Return top of the stack 102, 
stack becomes [201]
customStack.pop();                            // return 201 --> Return top of the stack 101, 
stack becomes []
customStack.pop();                            // return -1 --> Stack is empty return -1.
"""


class CustomStack:

    def __init__(self, maxSize: int):
        pass

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def increment(self, k: int, val: int) -> None:
        pass


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


"""
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), 
..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

 

Example 1:

Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
Example 2:

Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 
6) = 1 + 2 + 6 = 9.
"""


def arrayPairSum(self, nums: List[int]) -> int:
    pass


"""
Given an integer array nums, move all the even integers at the beginning of the array followed by 
all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
"""


def sortArrayByParity(nums: List[int]) -> List[int]:
    pass


"""
Given an array arr, replace every element in that array with the greatest element among the 
elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
"""


def replaceElements(arr: List[int]) -> List[int]:
    pass


"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [
starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and 
in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or 
represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

Example 1:


Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
Example 3:

Input: firstList = [], secondList = [[4,8],[10,12]]
Output: []
Example 4:

Input: firstList = [[1,7]], secondList = [[3,10]]
Output: [[3,7]]
"""


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[
    List[int]]:
    pass


"""
Given an array nums of distinct integers, return all the possible permutations. You can return 
the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""


def permute(nums: List[int]) -> List[List[int]]:
    pass


"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""


def subsets(nums: List[int]) -> List[List[int]]:
    pass


"""
You are keeping score for a baseball game with strange rules. The game consists of several 
rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings 
ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

An integer x - Record a new score of x.
"+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will 
always be two previous scores.
"D" - Record a new score that is double the previous score. It is guaranteed there will always be 
a previous score.
"C" - Invalidate the previous score, removing it from the record. It is guaranteed there will 
always be a previous score.
Return the sum of all the scores on the record.

 

Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
Example 2:

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
Example 3:

Input: ops = ["1"]
Output: 1
"""


def calPoints(ops: List[str]) -> int:
    pass


"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that 
single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""


def singleNumber(self, nums: List[int]) -> int:
    pass


"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are 
also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in 
arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
"""


def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    pass


"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in 
the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    pass


"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row 
that is either directly below or diagonally left/right. Specifically, the next element from 
position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

Example 1:


Input: matrix = [
  [2,1,3],
  [6,5,4],
  [7,8,9]
]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:


Input: matrix = [
  [-19, 57],
  [-40, -5]
]
Output: -59
Explanation: The falling path with a minimum sum is shown.
"""


def minFallingPathSum(matrix: List[List[int]]) -> int:
    pass


"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an 
integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (
y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the 
order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
"""


def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    pass


"""
Given two integer arrays pushed and popped each with distinct values, return true if this could 
have been the result of a sequence of push and pop operations on an initially empty stack, 
or false otherwise.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
"""


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    pass


"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix 
directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
Example 3:

Input: matrix = [[1]]
Output: [[1]]
Example 4:

Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]
"""


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """


"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return 
the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    pass


"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash 
them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of 
this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1
"""


def lastStoneWeight(stones: List[int]) -> int:
    pass


"""
Given an array of non-negative integers arr, you are initially positioned at start index of the 
array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach 
to any index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
"""


def canReach(arr: List[int], start: int) -> bool:
    pass


"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the 
array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""


def longestOnes(nums: List[int], k: int) -> int:
    pass


"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once 
you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""


def minCostClimbingStairs(cost: List[int]) -> int:
    pass


"""
There is a bookstore owner that has a store open for n minutes. Every minute, some number of 
customers enter the store. You are given an integer array customers of length n where customers[
i] is the number of the customer that enters the store at the start of the ith minute and all 
those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[
i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, 
they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes 
consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
Example 2:

Input: customers = [1], grumpy = [0], minutes = 1
Output: 1
"""


def maxSatisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    pass


"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
"""


def getRow(self, rowIndex: int) -> List[int]:
    pass


"""
You are given an array of logs. Each log is a space-delimited string of words, where the first 
word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, 
then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit 
dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
Example 2:

Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
"""


def reorderLogFiles(logs: List[str]) -> List[str]:
    pass


"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in 
the result must appear as many times as it shows in both arrays and you may return the result in 
any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load 
all elements into the memory at once?
"""


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    pass


"""
You are given an integer array height of length n. There are n vertical lines drawn such that the 
two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains 
the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, 
the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""


def maxArea(height: List[int]) -> int:
    pass


"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any 
profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


def maxProfit(prices: List[int]) -> int:
    pass


"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a 
different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, 
return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the 
sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) 
According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as 
the blank character which is less than any other character (More info).
"""


def isAlienSorted(words: List[str], order: str) -> bool:
    pass


"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item 
was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was 
present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that 
at least one element exists when this method is called). Each element must have the same 
probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time 
complexity.

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always 
return 2.
"""


class RandomizedSet:

    def __init__(self):
        pass

    def insert(self, val: int) -> bool:
        pass

    def remove(self, val: int) -> bool:
        pass

    def getRandom(self) -> int:
        pass


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have 
the result be placed in the first part of the array nums. More formally, if there are k elements 
after removing the duplicates, then the first k elements of nums should hold the final result. It 
does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array 
in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 
0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


def removeElement(nums: List[int], val: int) -> int:
    pass


"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is 
secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai 
trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 
otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
"""


def findJudge(n: int, trust: List[List[int]]) -> int:
    pass


"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which 
has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the 
divide and conquer approach, which is more subtle.
"""


def maxSubArray(nums: List[int]) -> int:
    pass


"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements 
without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of 
the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""


def lengthOfLIS(self, nums: List[int]) -> int:
    pass


"""
Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", 
"eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is stretchy if it can 
be made to be equal to s by any number of applications of the following extension operation: 
choose a group consisting of characters c, and add some number of characters c to the group so 
that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", 
but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do 
another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query 
word "hello" would be stretchy because of these two extension operations: query = "hello" -> 
"hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy.

 

Example 1:

Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
Example 2:

Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
Output: 3
"""


def expressiveWords(s: str, words: List[str]) -> int:
    pass


"""
You are a professional robber planning to rob houses along a street. Each house has a certain 
amount of money stashed, the only constraint stopping you from robbing each of them is that 
adjacent houses have security systems connected and it will automatically contact the police if 
two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum 
amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""


def rob(nums: List[int]) -> int:
    pass


"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


def merge_2(intervals: List[List[int]]) -> List[List[int]]:
    pass


"""
You are given a large integer represented as an integer array digits, where each digits[i] is the 
ith digit of the integer. The digits are ordered from most significant to least significant in 
left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [0]
Output: [1]
Explanation: The array represents the integer 0.
Incrementing by one gives 0 + 1 = 1.
Thus, the result should be [1].
Example 4:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""


def plusOne(digits: List[int]) -> List[int]:
    pass


"""
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, 
which makes it impossible to reach the last index.
"""


def canJump(nums: List[int]) -> bool:
    pass


"""
Find the first and last occurence of K in the sorted list nums.

Example 1:
Input: nums = [1,1,1,1,1,2,2,3,4,5,5,5,5,6], k = 1
Output: [0,4]

Example 2:
Input: nums = [1,1,1,1,1,2,2,3,4,5,5,5,5,6], k = 5
Output: [9,12]

Example 2:
Input: nums = [1,1,1,1,1,2,2,3,4,5,5,5,5,6], k = 4
Output: [8,8]

Example 2:
Input: nums = [1,1,1,1,1,2,2,3,4,5,5,5,5,6,11], k = 10
Output: []
"""


def first_and_last_of_k(nums: List[int], k: int) -> List[int]:
    pass


"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

Example 1:


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
"""


def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    pass


"""
Given a list of lists representing integers, add them up and return in the same format.
input = [
    [9,9,9,9],
    [1,1],
    [9,4,5,6],
    [9,0,0,0],
    [9,9,9,9]
]
output = [3,8,4,6,5]
"""


def plus_one_large_number(input: List[List[int]]) -> List[int]:
    pass


"""
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), 
determine if a person could attend all meetings. 

Example 1:

Input:
[[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input:[[7,10],[2,4]]

Output:true
"""


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    pass


"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],…] (si < ei), 
find the minimum number of conference rooms required. 

For example, Given [[0, 30],[5, 10],[15, 20]], return 2.
"""


def numberMeetingRooms(intervals: List[List[int]]) -> int:
    pass


"""Given a list of intervals calendar and a number of available conference rooms. For each query, return true if the 
meeting can be added to the calendar successfully without causing a conflict, otherwise false. A conference room can 
only hold one meeting at a time. 

Example 1:

Input: calendar = [[1, 2], [4, 5], [8, 10]], rooms = 1, queries = [[2, 3], [3, 4]]
Output: [true, true]
Example 2:

Input: calendar = [[1, 2], [4, 5], [8, 10]], rooms = 1, queries = [[4, 5], [5, 6]]
Output: [false, true]
Example 3:

Input:
calendar = [[1, 3], [4, 6], [6, 8], [9, 11], [6, 9], [1, 3], [4, 10]]
rooms = 3
queries = [[1, 9], [2, 6], [7, 9], [3, 5], [3, 9], [2, 4], [7, 10], [5, 9], [3, 10], [9, 10]]
Output: [false, true, false, true, false, true, false, false, false, true]
"""


def meeting_room_conflicts(calendar: List[List[int]], rooms: int, queries: list[List[int]]) -> List[bool]:
    pass


"""
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (
inclusive) and returns it. The probability of picking an index i is w[i] / sum(w). 

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability 
of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%). 


Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
Example 2:

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
"""


class PickWeightedRandom:

    def __init__(self, w: List[int]):
        pass

    def pickIndex(self) -> int:
        pass


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


"""" 
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth 
characters and is fully (left and right) justified. 

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra 
spaces ' ' when necessary so that each line has exactly maxWidth characters. 

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not 
divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right. 

For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = [
    "What","must","be","acknowledgment","shall","be"
], 
maxWidth = 16 
Output: [
    "What   must   be", 
    "acknowledgment  ",
     "shall be        " 
] 
Explanation: Note that the last line is "shall be    " instead of "shall     
be", because the last line must be left-justified instead of fully-justified. Note that the second line is also 
left-justified becase it contains only one word. 

Example 3: 

Input: words = [
    "Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art",
"is","everything","else","we","do"
], 
maxWidth = 20 
Output: [ 
    "Science  is  what we",
    "understand      well", 
    "enough to explain to",
    "a  computer.  Art is",
    "everything  else  we",
    "do                  "
]
"""


def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    pass


"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
"""


def validMountainArray(arr: List[int]) -> bool:
    pass


class MyCalendarTwo:

    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True


calendar_two = MyCalendarTwo()
print(calendar_two.book(10, 20))
print(calendar_two.book(50, 60))
print(calendar_two.book(10, 40))
print(calendar_two.book(5, 15))
print(calendar_two.book(5, 10))
print(calendar_two.book(25, 55))


def shortestToChar(s: str, c: str) -> List[int]:
    target_indices = []
    for i, character in enumerate(s):
        if character == c:
            target_indices.append(i)

    result = [0 for _ in range(len(s))]
    pointer_a = 0
    for i, character in enumerate(s):
        if pointer_a == len(target_indices) - 1:
            result[i] = (abs(i - target_indices[pointer_a]))
        elif abs(i - target_indices[pointer_a]) > abs(i - target_indices[pointer_a + 1]):
            pointer_a += 1
        result[i] = (abs(i - target_indices[pointer_a]))

    return result


s = "loveleetcode"
c = "e"
print(shortestToChar(s, c))

"""There is a long road with markers on it after each unit of distance. There are some ubers standing on the road. 
You are given the starting and ending coordinate of each uber (both inclusive). Note: At any given marker there may 
be multiple ubers or there may be none at all. 

Your task is to find the number of markers on which at least one uber is present. An uber with coordinates (l, 
r) is considered to be present on a marker m if and only if l ≤ m ≤ r. 

Example

For coordinates=[[4, 7], [-1, 5], [3, 6]], the output should be easyCountUber(coordinates) = 9.
"""


def number_of_markers_on_road(coordinates):
    pass


"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""


def threeSum(self, nums: List[int]) -> List[List[int]]:
    pass
