"""
Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
isLeaf: True if the node is leaf node on the tree or False if the node has the four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.



Example 1:


Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.

Example 2:



Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:



Constraints:

n == grid.length == grid[i].length
n == 2x where 0 <= x <= 6

"""
import collections
from typing import List


class QuadTreeNode:
    def __init__(self, val=None, is_leaf=False, top_left=None, top_right=None, bottom_left=None, bottom_right=None):
        self.val = val
        self.is_leaf = is_leaf
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right


def fill_quadtree(matrix):
    if len(matrix[0]) == 1:
        return QuadTreeNode(matrix[0][0], True)
    else:
        if matrix[0][0] \
                == matrix[0][len(matrix[0]) - 1] \
                == matrix[len(matrix) - 1][0] \
                == matrix[len(matrix) - 1][len(matrix[0]) - 1]:
            return QuadTreeNode(matrix[0][0], True)
        else:
            quad_tree_node = QuadTreeNode('*', False)
            half_length = int(len(matrix) / 2)
            quad_tree_node.top_left = fill_quadtree([row[:half_length] for row in matrix[:half_length]])
            quad_tree_node.top_right = fill_quadtree([row[half_length:] for row in matrix[:half_length]])
            quad_tree_node.bottom_left = fill_quadtree([row[:half_length] for row in matrix[half_length:]])
            quad_tree_node.bottom_right = fill_quadtree([row[half_length:] for row in matrix[half_length:]])
            return quad_tree_node


class QuadTree:
    def __init__(self, matrix):
        self.head = fill_quadtree(matrix)

    def __str__(self):
        result = []
        queue = collections.deque([[self.head, 0]])
        while queue:
            quadtree_node, level = queue.popleft()
            if level == len(result):
                result.append([str(quadtree_node.val)])
            else:
                result[level].append(str(quadtree_node.val))
            if quadtree_node.bottom_left:
                queue.append([quadtree_node.bottom_left, level + 1])
            if quadtree_node.bottom_right:
                queue.append([quadtree_node.bottom_right, level + 1])
            if quadtree_node.top_left:
                queue.append([quadtree_node.top_left, level + 1])
            if quadtree_node.top_right:
                queue.append([quadtree_node.top_right, level + 1])

        return ' '.join(' '.join(a_result) + '\n' for a_result in result)


input = [
    [1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0]
]
quadtree = QuadTree(input)
print(quadtree)

"""
I got an interesting question from Uber, it's a phone interview.

Implement a quadtree with its properties:

  Each node has four children (non-value) or one value.
For example:

      Root
 A   B   C            D
 1   2   3       E  F  G  H
                 4  5  6  7

  ** Implement a quadtree and then write an algorithm to convert a 2D-matrix into a quadtree format.
For example:

  [[1,2,3,4],       1 2 | 3 4                  Root   
   [5,6,7,8], >>>   5 6 | 7 8   >>>    TL     TR      BL    BR
   [9,0,5,5],       ---------         1256   3478    9091    5
   [9,1,5,5]]       9 0 | 5 5     
                    9 1 | 5 5
Note: TL means top-left, TR means top-right, BL means bottom-left, BR means bottom-right.

As shown in the description above, for some quarters like bottom right BR, it has all 5s, so the quadtree only stores 
one value (number 5) instead of storing 4 numbers (5 5 5 5). """


class UberQuadTreeNode:
    def __init__(self, values=None, top_left=None, top_right=None, bottom_left=None, bottom_right=None):
        self.values = values
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right


class UberQuadTree:
    def __init__(self, matrix):
        self.head = self.build_quadtree(matrix)

    def build_quadtree(self, matrix):
        uber_quad_tree_node = UberQuadTreeNode()

        if len(matrix) == 2:
            if matrix[0][1] == matrix[0][0] == matrix[1][0] == matrix[1][1]:
                uber_quad_tree_node.values = [matrix[0][0]]
            else:
                uber_quad_tree_node.values = [matrix[0][1], matrix[0][0], matrix[1][0], matrix[1][1]]
            return uber_quad_tree_node

        mid_pointer = int(len(matrix) / 2)

        uber_quad_tree_node.bottom_left = self.build_quadtree([row[:mid_pointer] for row in matrix[:mid_pointer]])
        uber_quad_tree_node.bottom_right = self.build_quadtree([row[:mid_pointer] for row in matrix[mid_pointer:]])
        uber_quad_tree_node.top_left = self.build_quadtree([row[mid_pointer:] for row in matrix[:mid_pointer]])
        uber_quad_tree_node.top_right = self.build_quadtree([row[mid_pointer:] for row in matrix[mid_pointer:]])
        return uber_quad_tree_node


input = [
    [1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0]
]
UberQuadTree(input)


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def construct(grid: List[List[int]]) -> 'Node':
    if len(grid) == 1:
        return Node(grid[0][0], True, None, None, None, None)
    else:
        half_length = int(len(grid) / 2)
        top_left = construct([row[:half_length] for row in grid[:half_length]])
        top_right = construct([row[half_length:] for row in grid[:half_length]])
        bottom_left = construct([row[:half_length] for row in grid[half_length:]])
        bottom_right = construct([row[half_length:] for row in grid[half_length:]])
        if bottom_left.val == bottom_right.val == top_left.val == top_right.val != '*':
            return Node(bottom_left.val, True, None, None, None, None)
        else:
            return Node('*', False, top_left, top_right, bottom_left, bottom_right)


input = [
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]
construct(input)
