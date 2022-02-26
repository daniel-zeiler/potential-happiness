"""
You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and
1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. You are given an array positions
where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may
assume all four edges of the grid are all surrounded by water.

Example 1:

Input: m = 3, n = 3, positions = [
    [0,0],[0,1],[1,2],[2,1]
]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid is filled with water.
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.
Example 2:

Input: m = 1, n = 1, positions = [[0,0]]
Output: [1]
"""
from typing import List


def numIslands2(m: int, n: int, positions: List[List[int]]) -> List[int]:
    pass


"""
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 
-> 1 -> ... forever. You will start at the bus stop source (You are not on any bus initially), and you want to go to 
the bus stop target. You can travel between bus stops by buses only. 

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
"""


def numBusesToDestination(routes: List[List[int]], source: int, target: int) -> int:
    pass


"""
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted 
lexicographically by the rules of this new language. 

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the 
new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them. 

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s 
comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, 
then s is smaller if and only if s.length < t.length. 

 

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
"""


def alienOrder(words: List[str]) -> str:
    pass
