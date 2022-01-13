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

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
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
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

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


def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    pass


"""
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

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


"""
You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

You are given an array of employees employees where:

employees[i].id is the ID of the ith employee.
employees[i].importance is the importance value of the ith employee.
employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.
Given an integer id that represents an employee's ID, return the total importance value of this employee and all their direct and indirect subordinates.

 

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
