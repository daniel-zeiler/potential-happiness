# 55 problems

import collections
import heapq
from typing import List

"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody. Everybody (except for the town judge) trusts the town judge. There is exactly one
person that satisfies properties 1 and 2. You are given an array trust where trust[i] = [ai, bi] representing that
the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: n = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
"""


def find_town_judge(n: int, trust: List[List[int]]) -> int:
    pass


"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to 
node n - 1 and return them in any order. 

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed 
edge from node i to node graph[i][j]). 

Example 1:

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:

Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
Example 3:

Input: graph = [[1],[]]
Output: [[0,1]]
Example 4:

Input: graph = [[1,2,3],[2],[3],[]]
Output: [[0,1,2,3],[0,2,3],[0,3]]
Example 5:

Input: graph = [[1,3],[2],[3],[]]
Output: [[0,1,2,3],[0,3]]
"""


def all_paths_source_to_target(graph):
    pass


"""
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [
fromi, toi] represents a directed edge from node fromi to node toi. 

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique 
solution exists. 

Notice that you can return the vertices in any order.

Example 1:

Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]] Output: [0,3] Explanation: It's not possible to reach all the 
nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3]. Example 
2: 

Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]] Output: [0,2,3] Explanation: Notice that vertices 0, 
3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 
and 4. 
"""


def minimum_vertices_reach_all_nodes(n: int, edges: List[List[int]]) -> List[int]:
    pass


"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit 
all the rooms. However, you cannot enter a locked room without having its key. 

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it 
unlocks, and you can take all of them with you to unlock the other rooms. 

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you 
can visit all the rooms, or false otherwise. 

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room. 
"""


def keys_and_rooms(rooms: List[List[int]]) -> bool:
    pass


"""
547. Number of Provinces There are n cities. Some of them are connected, while some are not. If city a is 
connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly 
with city c. 

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly 
connected, and isConnected[i][j] = 0 otherwise. 

Return the total number of provinces.

Example 1:

Input: isConnected = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
]
Output: 2
Example 2:

Input: isConnected = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]
Output: 3
"""


def number_of_provinces(is_connected):
    pass


"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The 
added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is 
represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai 
and bi in the graph. 

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, 
return the answer that occurs last in the input. 

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
"""


def redundant_connections(edges):
    pass


"""
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, 
bi] indicates that there is a bidirectional road between cities ai and bi. 

The network rank of two different cities is defined as the total number of directly connected roads to either city. 
If a road is directly connected to both cities, it is only counted once. 

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

Example 1:

Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]] Output: 4 Explanation: The network rank of cities 0 and 1 is 4 as 
there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once. Example 2: 

Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
Output: 5
Explanation: There are 5 roads that are connected to cities 1 or 2.
Example 3:

Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
Output: 5
Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.
"""


def maximal_network_rank(n, roads):
    pass


"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 
0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an 
edge from node i to each node in graph[i]. 

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from 
that node leads to a terminal node. 

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Example 1:

Illustration of graph
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
Example 2:

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
"""


def find_eventual_safe_nodes(graph):
    pass


"""
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D 
array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], 
there is an undirected edge between node u and node v. The graph has the following properties: 

There are no self-edges (graph[u] does not contain u). There are no parallel edges (graph[u] does not contain 
duplicate values). If v is in graph[u], then u is in graph[v] (the graph is undirected). The graph may not be 
connected, meaning there may be two nodes u and v such that there is no path between them. A graph is bipartite if 
the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in 
set A and a node in set B. 

Return true if and only if it is bipartite.

Example 1:

Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]] Output: false Explanation: There is no way to partition the nodes into 
two independent sets such that every edge connects a node in one and a node in the other. Example 2: 

Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
"""


def is_graph_bipartite(graph):
    pass


"""
You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes a bidirectional 
path between garden xi to garden yi. In each garden, you want to plant one of 4 types of flowers. 

All gardens have at most 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, 
they have different types of flowers. 

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden. The 
flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists. 

Example 1:

Input: n = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Explanation:
Gardens 1 and 2 have different types.
Gardens 2 and 3 have different types.
Gardens 3 and 1 have different types.
Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].
Example 2:

Input: n = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 """


def flower_planting_no_adjacent(n, paths):
    pass


"""

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as 
directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it 
takes for a signal to travel from source to target. 

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it 
is impossible for all the n nodes to receive the signal, return -1. 

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
"""


def network_delay_time(times, n, k):
    pass


"""
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike 
some other people, and they should not go into the same group. 

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not 
like the person labeled bi, return true if it is possible to split everyone into two groups in this way. 

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].
Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
"""


def possible_bipartition(n, dislikes):
    pass


"""
Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take
course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1. Return the ordering of
courses you should take to finish all courses. If there are many valid answers, return any of them. If it is
impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]] Output: [0,1] Explanation: There are a total of 2 courses to take. To
take course 1 you should have finished course 0. So the correct course order is [0,1]. Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] Output: [0,2,1,3] Explanation: There are a total of
4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be
taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,
3]. Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
"""


def course_schedule_two(num_courses, prerequisites):
    pass


"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[
i], return true if and only if all the given nodes form exactly one valid binary tree. 

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

Example 1:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:

Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
Example 4:

Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false
"""


def validate_binary_tree(n, left_child, right_child):
    pass


"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, 
Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single 
variable. 

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer 
for Cj / Dj = ?. 

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and 
that there is no contradiction. 

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
"""


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
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


def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    pass


"""You have a data structure of employee information, including the employee's unique ID, importance value, 
and direct subordinates' IDs. 

You are given an array of employees employees where:

employees[i].id is the ID of the ith employee. employees[i].importance is the importance value of the ith employee. 
employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee. Given an integer id 
that represents an employee's ID, return the total importance value of this employee and all their direct and 
indirect subordinates. 

 

Example 1:


Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
Output: 11
Explanation: Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3.
They both have an importance value of 3.
Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.
Example 2:


Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
Output: -3
Explanation: Employee 5 has an importance value of -3 and has no direct subordinates.
Thus, the total importance value of employee 5 is -3.
"""


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def getImportance(employees: List['Employee'], id: int) -> int:
    pass


"""Suppose you are at a party with n people (labeled from 0 to n - 1), and among them, there may exist one celebrity. 
The definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them. 

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do 
is to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out 
the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense). 

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int 
findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if 
there is a celebrity in the party. If there is no celebrity, return -1. 

 

Example 1:


Input: graph = [[1,1,0],[0,1,0],[1,1,1]] Output: 1 Explanation: There are three persons labeled with 0, 
1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i ][j] = 0 means person i does not know 
person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody. Example 
2: 


Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.
 

Constraints:

n == graph.length
n == graph[i].length
2 <= n <= 100
graph[i][j] is 0 or 1.
graph[i][i] == 1
"""


# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

def findCelebrity(self, n: int) -> int:
    pass


"""
Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in 
s1 exactly k times so that the resulting string equals s2. 

Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.

 

Example 1:

Input: s1 = "ab", s2 = "ba"
Output: 1
Example 2:

Input: s1 = "abc", s2 = "bca"
Output: 2
"""


def kSimilarity(s1: str, s2: str) -> int:
    pass


"""A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words 
beginWord -> s1 -> s2 -> ... -> sk such that: 

Every adjacent pair of words differs by a single letter. Every si for 1 <= i <= k is in wordList. Note that beginWord 
does not need to be in wordList. sk == endWord Given two words, beginWord and endWord, and a dictionary wordList, 
return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such 
sequence exists. 

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    pass


"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array 
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take 
course ai. 

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
 
 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]] Output: false Explanation: There are a total of 2 courses to 
take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 
1. So it is impossible. 


Example 3:
100
[[1,0],[2,0],[2,1],[3,1],[3,2],[4,2],[4,3],[5,3],[5,4],[6,4],[6,5],[7,5],[7,6],[8,6],[8,7],[9,7],[9,8],[10,8],[10,9],
[11,9],[11,10],[12,10],[12,11],[13,11],[13,12],[14,12],[14,13],[15,13],[15,14],[16,14],[16,15],[17,15],[17,16],[18,16],
[18,17],[19,17],[19,18],[20,18],[20,19],[21,19],[21,20],[22,20],[22,21],[23,21],[23,22],[24,22],[24,23],[25,23],[25,24],
[26,24],[26,25],[27,25],[27,26],[28,26],[28,27],[29,27],[29,28],[30,28],[30,29],[31,29],[31,30],[32,30],[32,31],[33,31],
[33,32],[34,32],[34,33],[35,33],[35,34],[36,34],[36,35],[37,35],[37,36],[38,36],[38,37],[39,37],[39,38],[40,38],[40,39],
[41,39],[41,40],[42,40],[42,41],[43,41],[43,42],[44,42],[44,43],[45,43],[45,44],[46,44],[46,45],[47,45],[47,46],[48,46],
[48,47],[49,47],[49,48],[50,48],[50,49],[51,49],[51,50],[52,50],[52,51],[53,51],[53,52],[54,52],[54,53],[55,53],[55,54],
[56,54],[56,55],[57,55],[57,56],[58,56],[58,57],[59,57],[59,58],[60,58],[60,59],[61,59],[61,60],[62,60],[62,61],[63,61],
[63,62],[64,62],[64,63],[65,63],[65,64],[66,64],[66,65],[67,65],[67,66],[68,66],[68,67],[69,67],[69,68],[70,68],[70,69],
[71,69],[71,70],[72,70],[72,71],[73,71],[73,72],[74,72],[74,73],[75,73],[75,74],[76,74],[76,75],[77,75],[77,76],[78,76],
[78,77],[79,77],[79,78],[80,78],[80,79],[81,79],[81,80],[82,80],[82,81],[83,81],[83,82],[84,82],[84,83],[85,83],[85,84],
[86,84],[86,85],[87,85],[87,86],[88,86],[88,87],[89,87],[89,88],[90,88],[90,89],[91,89],[91,90],[92,90],[92,91],[93,91],
[93,92],[94,92],[94,93],[95,93],[95,94],[96,94],[96,95],[97,95],[97,96],[98,96],[98,97],[99,97]
]
"""


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    pass


"""There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] 
= [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi. 

Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. 
If it is impossible to connect all the n cities, return -1, 

The cost is the sum of the connections' costs used.

 

Example 1:


Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.
Example 2:


Input: n = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: There is no way to connect all cities even if all edges are used.
"""


def minimumCost(self, n: int, connections: List[List[int]]) -> int:
    pass


"""
Currency Exchange


You given data set in the form of list of <curr1 - curr2 - ask - bid> ask means how much curr2 do you have to spend 
to buy 1 unit of curr1 and bid is how much of curr2 will you get if you sell 1 unit of curr1. 
Now given any two currencies x and y. Find the best conversion rate.

a list of currency relationships with exchange values. (BTC - USD)
find the best exchange rate from currency1 to currency2.

data = [
    (BTC,ETH,1/10,10),
    (BTC,USDC,1/13000,13000),
    (ETH,USDC,1/1300,1300),
    (LINK,USDC,1/28,28),
    (LINK,SDE,1/234,234),
    (SDE,COIN,1/400,400),
    (COIN,USDC,1/24,24)
]

"""


def currency_exchange(currency_one, currency_two, data):
    def get_graph():
        graph = collections.defaultdict(dict)
        for curr_one, curr_two, rate in data:
            graph[curr_one][curr_two] = rate
            graph[curr_two][curr_one] = 1 / rate
        return graph

    graph = get_graph()

    def traverse(currency, visited):
        result = 0
        if currency == currency_two:
            return 1
        for adjacent in graph[currency]:
            if adjacent not in visited:
                result = max(result, graph[currency][adjacent] * traverse(adjacent, visited | {adjacent}))
        return result

    return traverse(currency_one, {currency_one})


data = [
    ['USD', 'JPY', 110], ['USD', 'AUD', 1.45], ['JPY', 'GBP', 0.0070]
]
print(currency_exchange('GBP', 'AUD', data))

"""
You're developing a system for scheduling advising meetings with students in a Computer Science program. Each 
meeting should be scheduled when a student has completed 50% of their academic program. 

Each course at our university has at most one prerequisite that must be taken first. No two courses share a 
prerequisite. There is only one path through the program. 

Write a function that takes a list of (prerequisite, course) pairs, and returns the name of the course that the 
student will be taking when they are halfway through their program. (If a track has an even number of courses, 
and therefore has two "middle" courses, you should return the first one.) 

Sample input 1: (arbitrarily ordered)
prereqs_courses1 = [
	["Foundations of Computer Science", "Operating Systems"],
	["Data Structures", "Algorithms"],
	["Computer Networks", "Computer Architecture"],
	["Algorithms", "Foundations of Computer Science"],
	["Computer Architecture", "Data Structures"],
	["Software Design", "Computer Networks"]
]

In this case, the order of the courses in the program is:
	Software Design
	Computer Networks
	Computer Architecture
	Data Structures
	Algorithms
	Foundations of Computer Science
	Operating Systems

Sample output 1:
	"Data Structures"


Sample input 2:
prereqs_courses2 = [
	["Data Structures", "Algorithms"],
	["Algorithms", "Foundations of Computer Science"],
	["Foundations of Computer Science", "Logic"]
]


Sample output 2:
	"Algorithms"

Sample input 3:
prereqs_courses3 = [
	["Data Structures", "Algorithms"],
]


Sample output 3:
	"Data Structures"

Complexity analysis variables:

n: number of pairs in the input

prereqs_courses1 = [
    ["Foundations of Computer Science", "Operating Systems"],
    ["Data Structures", "Algorithms"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"]
]

prereqs_courses2 = [
    ["Data Structures", "Algorithms"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Foundations of Computer Science", "Logic"]
 ]

prereqs_courses3 = [
    ["Data Structures", "Algorithms"]
]
"""

from collections import defaultdict, deque


def half_prereq(prerequisites):
    def get_graph_and_in_degree():
        in_degree = defaultdict(int)
        graph = defaultdict(list)
        for before, after in prerequisites:
            if before not in in_degree:
                in_degree[before] = 0
            if after not in in_degree:
                in_degree[after] = 0
            graph[before].append(after)
            in_degree[after] += 1
        return graph, in_degree

    graph, in_degree = get_graph_and_in_degree()
    queue = deque(list(filter(lambda x: in_degree[x] == 0, in_degree.keys())))

    result = []
    while queue:
        course = queue.popleft()
        result.append(course)
        for adjacent in graph[course]:
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:
                queue.append(adjacent)

    if len(result) != len(graph):
        raise Exception('unable to complete')
    return result[(len(result) // 2)]


prereqs_courses1 = [
    ["Foundations of Computer Science", "Operating Systems"],
    ["Data Structures", "Algorithms"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"]
]
print(half_prereq(prereqs_courses1))

"""
You operate a marketplace for buying & selling used textbooks For a given textbook eg“TheoryofCryptography”
there are people who want to buy this textbook and people who want to sell

OfferstoBUY: [$100, $100, $99, $99, $97, $90]

OfferstoSELL:[$109, $110, $110, $114, $115$, 119]

A match occurs when two people agree on a price Some new offers do not match These offers should be added to the 
active set of offers 

For example, Tim offers to SELL at $150 This will not match No one is willing to buy at that price so we save the offer

OfferstoSELL:: [$109, $110, $110, $114, $115, $119, $150]

When matching we want to give the customer the “best price”

Example matches: If Jane offers to BUY at $120

she will match and buy a book for $109 (the lowest offer)
"""


class OfferMatchingLinearTime:
    def __init__(self, max_price):
        self.prices = [deque([]) for _ in range(max_price)]
        self.buy_pointer = -1
        self.sell_pointer = max_price + 1
        self.max_price = max_price

    def buy(self, offer):
        if self.sell_pointer == self.max_price + 1 or offer < self.prices[self.sell_pointer][0]:
            self.prices[offer].append(offer)
            self.buy_pointer = max(self.buy_pointer, offer)
        else:
            result = self.prices[self.sell_pointer].popleft()
            while not self.prices[self.sell_pointer] and self.sell_pointer != self.max_price + 1:
                self.sell_pointer += 1
            return result

    def sell(self, offer):
        if self.buy_pointer == -1 or offer > self.prices[self.buy_pointer][0]:
            self.prices[offer].append(offer)
            self.sell_pointer = min(self.sell_pointer, offer)
        else:
            result = self.prices[self.buy_pointer].popleft()
            while not self.prices[self.buy_pointer] and self.buy_pointer != -1:
                self.buy_pointer -= 1
            return result


from datetime import datetime, timedelta


class OfferMatcher:
    def __init__(self):
        self.buy_offers = []
        self.sell_offers = []

    def buy(self, offer, cancellation_time):
        timestamp = datetime.now()
        while self.sell_offers and timestamp > self.sell_offers[0][1]:
            heapq.heappop(self.sell_offers)
        if not self.sell_offers or offer < self.sell_offers[0][0]:
            heapq.heappush(self.buy_offers, [-offer, cancellation_time])
        else:
            return heapq.heappop(self.sell_offers[0])

    def sell(self, offer, cancellation_time):
        timestamp = datetime.now()
        while self.buy_offers and timestamp > self.buy_offers[0][1]:
            heapq.heappop(self.buy_offers)
        if not self.buy_offers or offer > -self.buy_offers[0][0]:
            heapq.heappush(self.sell_offers, [offer, cancellation_time])
        else:
            return -heapq.heappop(self.buy_offers[0])

    def __str__(self):
        return str(sorted(self.buy_offers, key=lambda x: -x[0])) + '\n' + str(sorted(self.sell_offers))


offer_matcher = OfferMatcher()
OfferstoBUY = [100, 100, 99, 99, 97, 90]
OfferstoSELL = [109, 110, 110, 114, 115, 119]
a_time = datetime.now()

for buy, sell in zip(OfferstoBUY, OfferstoSELL):
    print(offer_matcher.buy(buy, a_time + timedelta(minutes=30)))
    print(offer_matcher.sell(sell, a_time + timedelta(minutes=30)))

print(offer_matcher)
print(offer_matcher.sell(150, a_time + timedelta(minutes=30)))
print(offer_matcher.buy(120, a_time + timedelta(minutes=30)))

"""
You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some 
intersections. The inputs are generated such that you can reach any intersection from any other intersection and that 
there is at most one road between any two intersections. 

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road 
between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel 
from intersection 0 to intersection n - 1 in the shortest amount of time. 

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be 
large, return it modulo 109 + 7. 

 

Example 1:


Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6
Example 2:

Input: n = 2, roads = [[1,0,10]]
Output: 1
Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.
"""


def countPaths(self, n: int, roads: List[List[int]]) -> int:
    pass


"""There is an undirected weighted connected graph. You are given a positive integer n which denotes that the graph 
has n nodes labeled from 1 to n, and an array edges where each edges[i] = [ui, vi, weighti] denotes that there is an 
edge between nodes ui and vi with weight equal to weighti. 

A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start and zk = end and 
there is an edge between zi and zi+1 where 0 <= i <= k-1. 

The distance of a path is the sum of the weights on the edges of the path. Let distanceToLastNode(x) denote the 
shortest distance of a path between node n and node x. A restricted path is a path that also satisfies that 
distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1. 

Return the number of restricted paths from node 1 to node n. Since that number may be too large, return it modulo 109 
+ 7. 

 

Example 1:


Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]] Output: 3 Explanation: Each circle 
contains the node number in black and its distanceToLastNode value in blue. The three restricted paths are: 1) 1 --> 
2 --> 5 2) 1 --> 2 --> 3 --> 5 3) 1 --> 3 --> 5 Example 2: 


Input: n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]] Output: 1 Explanation: Each 
circle contains the node number in black and its distanceToLastNode value in blue. The only restricted path is 1 --> 
3 --> 7. """


def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
    pass


"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array 
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take 
course bi. 

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1. Prerequisites can 
also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course 
a is a prerequisite of course c. 

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course 
uj is a prerequisite of course vj or not. 

Return a boolean array answer, where answer[j] is the answer to the jth query.

 

Example 1:


Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.
Example 2:

Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.
Example 3:


Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]
"""


def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    pass


"""
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a 
bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold. 

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most 
distanceThreshold, If there are multiple such cities, return the city with the greatest number. 

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

 

Example 1:


Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4 Output: 3 Explanation: The figure 
above describes the graph. The neighboring cities at a distanceThreshold = 4 for each city are: City 0 -> [City 1, 
City 2] City 1 -> [City 0, City 2, City 3] City 2 -> [City 0, City 1, City 3] City 3 -> [City 1, City 2] Cities 0 and 
3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest 
number. Example 2: 


Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.
"""


def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    pass


"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where 
connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other 
computer directly or indirectly through the network. 

You are given an initial computer network connections. You can extract certain cables between two directly connected 
computers, and place them between any pair of disconnected computers to make them directly connected. 

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not 
possible, return -1. 

 

Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
"""


def makeConnected(n: int, connections: List[List[int]]) -> int:
    pass


"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [
a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge 
succProb[i]. 

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and 
return its success probability. 

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer 
by at most 1e-5. 

 

Example 1:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2 Output: 0.25000 Explanation: 
There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25. 
Example 2: 



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000
Example 3:



Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.
"""


def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    pass


"""
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. 
Each edge is red or blue in this graph, and there could be self-edges and parallel edges. 

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, 
and blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph. Return 
an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that 
the edge colors alternate along the path, or -1 if such a path does not exist. 

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
"""


def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    pass


"""There is a group of n people labeled from 0 to n - 1 where each person has a different amount of money and a 
different level of quietness. 

You are given an array richer where richer[i] = [ai, bi] indicates that ai has more money than bi and an integer 
array quiet where quiet[i] is the quietness of the ith person. All the given data in richer are logically correct (
i.e., the data will not lead you to a situation where x is richer than y and y is richer than x at the same time). 

Return an integer array answer where answer[x] = y if y is the least quiet person (that is, the person y with the 
smallest value of quiet[y]) among all people who definitely have equal to or more money than the person x. 

 

Example 1:

Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0] Output: [5,5,2,5,4,5,6,
7] Explanation: answer[0] = 5. Person 5 has more money than 3, which has more money than 1, which has more money than 
0. The only person who is quieter (has lower quiet[x]) is person 7, but it is not clear if they have more money than 
person 0. answer[7] = 7. Among all people that definitely have equal to or more money than person 7 (which could be 
persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x]) is person 7. The other answers can be 
filled out with similar reasoning. """


def loudAndRich(richer: List[List[int]], quiet: List[int]) -> List[int]:
    pass


"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, 
toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei. 

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If 
there is no such route, return -1. 

 

Example 1:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
"""


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    pass
