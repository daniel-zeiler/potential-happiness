from typing import Optional, List
from binarytree import Node

"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there 
are no nodes with a
value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
"""


def count_good_nodes_in_binary_tree(root):
    pass


"""
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the 
company is the one 
with headID. 

Each employee has one direct manager given in the manager array where manager[i] is the direct 
manager of the i-th 
employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have 
a tree structure. 

The head of the company wants to inform all the company employees of an urgent piece of news. He 
will inform his 
direct subordinates, and they will inform their subordinates, and so on until all employees know 
about the urgent news. 

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., 
After informTime[i] 
minutes, all his direct subordinates can start spreading the news). 

Return the number of minutes needed to inform all the employees about the urgent news.

 

Example 1:

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.
Example 2:

Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0] Output: 1 
Explanation: The head of the 
company with id = 2 is the direct manager of all the employees in the company and needs 1 minute 
to inform them all. 
The tree structure of the employees in the company is shown. Example 3: 

Input: n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]
Output: 21
Explanation: The head has id = 6. He will inform employee with id = 5 in 1 minute.
The employee with id = 5 will inform the employee with id = 4 in 2 minutes.
The employee with id = 4 will inform the employee with id = 3 in 3 minutes.
The employee with id = 3 will inform the employee with id = 2 in 4 minutes.
The employee with id = 2 will inform the employee with id = 1 in 5 minutes.
The employee with id = 1 will inform the employee with id = 0 in 6 minutes.
Needed time = 1 + 2 + 3 + 4 + 5 + 6 = 21.
Example 4:

Input: n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,
1,0,0,0,0,0,0,0,0]
Output: 3
Explanation: The first minute the head will inform employees 1 and 2.
The second minute they will inform employees 3, 4, 5 and 6.
The third minute they will inform the rest of employees.
Example 5:

Input: n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]
Output: 1076
"""


def time_needed_inform_all_employees(n, head_id, manager, inform_time):
    pass


"""
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node 
and has the value 
target, it should also be deleted (you need to continue doing that until you can't). 

Example 1:

Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
Example 2:

Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]
Example 3:

Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
Example 4:

Input: root = [1,1,1], target = 1
Output: []
Example 5:

Input: root = [1,2,3], target = 1
Output: [1,2,3]
"""


def delete_leaves_given_value(root, target):
    pass


"""
Given a binary tree with the following rules:

root.val == 0
If Node.val == x and Node.left != null, then Node.left.val == 2 * x + 1
If Node.val == x and Node.right != null, then Node.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all Node.val have been changed to -1.

Implement the FindElements class:

FindElements(Node* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.

Example 1:

Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 
Example 2:

Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False
Example 3:

Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True
"""


# Definition for a binary tree node.
# class Node:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[Node]):
        return

    def find(self, target: int) -> bool:
        pass


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)


"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] 
and rightChild[
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


def validate_binary_nodes(n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    pass


"""
Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
"""


def deepest_leaves_sum(root: Optional[Node]) -> int:
    pass


"""
Given the root of a binary tree, return the sum of values of nodes with an even-valued 
grandparent. If there are 
no nodes with an even-valued grandparent, return 0. 

A grandparent of a node is the parent of its parent if it exists.

Example 1:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5] Output: 18 Explanation: The red nodes 
are the nodes with 
even-value grandparent while the blue nodes are the even-value grandparents. Example 2: 

Input: root = [1]
Output: 0
"""


def sumEvenGrandparent(self, root: Node) -> int:
    pass


"""
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children The depth of the root of 
the tree is 0. if the 
depth of a node is d, the depth of each of its children is d + 1. The lowest common ancestor of a 
set S of nodes, 
is the node A with the largest depth such that every node in S is in the subtree with root A. 
 
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of 
nodes 7 and 4 is 3.
Example 2:

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree, and it's the lca of itself.
Example 3:

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.
"""


def lca_deepest_leaves(root: Optional[Node]) -> Optional[Node]:
    pass


"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union 
of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

Example 1:

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
"""


def del_nodes(root: Node, to_delete: List[int]) -> List[Node]:
    pass


"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, 
and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
"""


def max_level_sum(root: Optional[Node]) -> int:
    pass


"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of 
the original BST 
is changed to the original key plus the sum of all keys greater than the original key in BST. 

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
Example 2:

Input: root = [0,null,1]
Output: [1,null,1]
Example 3:

Input: root = [1,0,2]
Output: [3,3,2]
Example 4:

Input: root = [3,2,4,1]
Output: [7,9,4,10]
"""


def bstToGst(self, root: Node) -> Node:
    pass


"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a 
and b where v = 
|a.val - b.val| and a is an ancestor of b. 

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an 
ancestor of b.

Example 1:

Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
Example 2:

Input: root = [1,null,2,null,0,3]
Output: 3
"""


def max_ancestor_diff(root: Optional[Node]) -> int:
    pass


"""
Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., 
binary search tree), 
construct the tree and return its root. 

It is guaranteed that there is always possible to find a binary search tree with the given 
requirements for the given 
test cases. 

A binary search tree is a binary tree where for every node, any descendant of Node.left has a 
value strictly less 
than Node.val, and any descendant of Node.right has a value strictly greater than Node.val. 

A preorder traversal of a binary tree displays the value of the node first, then traverses 
Node.left, then traverses 
Node.right. 

Example 1:

Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
Example 2:

Input: preorder = [1,3]
Output: [1,null,3]
"""


def bstFromPreorder(self, preorder: List[int]) -> Optional[Node]:
    pass


"""
Given the root of a binary tree with unique values and the values of two different nodes of the 
tree x and y, 
return true if the nodes corresponding to the values x and y in the tree are cousins, or false 
otherwise. 

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node 
are at the depth k + 1.

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
"""


def is_cousins(root: Optional[Node], x: int, y: int) -> bool:
    pass


"""
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, 
col - 1) and (row + 
1, col + 1) respectively. The root of the tree is at (0, 0). 

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each 
column index starting 
from the leftmost column and ending on the rightmost column. There may be multiple nodes in the 
same row and same 
column. In such a case, sort these nodes by their values. 

Return the vertical order traversal of the binary tree.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
Example 2:

Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
Example 3:

Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be 
ordered by their values.
"""


def verticalTraversal(self, root: Optional[Node]) -> List[List[int]]:
    pass


"""
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

Example 1:

Input: root = [1,1,1,1,1,null,1]
Output: true
Example 2:

Input: root = [2,2,2,5,2]
Output: false
"""


def is_unival_tree(root: Optional[Node]) -> bool:
    pass


"""
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the 
left and right child 
subtrees. 

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y 
after some number of 
flip operations. 

Given the roots of two binary trees root1 and root2, return true if the two trees are flip 
equivalent or false 
otherwise. 

Example 1:

Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Example 2:

Input: root1 = [], root2 = []
Output: true
Example 3:

Input: root1 = [], root2 = [1]
Output: false
Example 4:

Input: root1 = [0,null,1], root2 = []
Output: false
Example 5:

Input: root1 = [0,null,1], root2 = [0,1]
Output: true
"""


def flip_equiv(root1: Optional[Node], root2: Optional[Node]) -> bool:
    pass


"""
Given the root node of a binary search tree and two integers low and high, return the sum of 
values of all nodes 
with a value in the inclusive range [low, high]. 

Example 1:

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
"""


def range_sum_bst(root: Optional[Node], low: int, high: int) -> int:
    pass


"""
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node 
in the tree is 
now the root of the tree, and every node has no left child and only one right child. 

Example 1:

Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:

Input: root = [5,1,7]
Output: [1,null,5,null,7]
"""


def increasingBST(self, root: Node) -> Node:
    pass


"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves 
form a leaf value 
sequence. 

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,
null,9,8]
Output: true
Example 2:

Input: root1 = [1], root2 = [1]
Output: true
Example 3:

Input: root1 = [1], root2 = [2]
Output: false
Example 4:

Input: root1 = [1,2], root2 = [2,2]
Output: true
Example 5:

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
"""


def leaf_similar(root1: Optional[Node], root2: Optional[Node]) -> bool:
    pass


"""
Given the root of a binary tree, the value of a target node target, and an integer k, return an 
array of the 
values of all nodes that have a distance k from the target node. 

You can return the answer in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 
4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
"""


def distance_k(root: Node, target: Node, k: int) -> List[int]:
    pass


"""
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not 
containing a 1 
has been removed. 

A subtree of a node node is node plus every node that is a descendant of node.

Example 1:

Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
Example 2:

Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
Example 3:

Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
"""


def pruneTree(root: Optional[Node]) -> Optional[Node]:
    pass


"""
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of 
any two different nodes in the tree. 

Example 1:

Input: root = [4,2,6,1,3]
Output: 1
Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1
"""


def minDiffInBST(root: Optional[Node]) -> int:
    pass


"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest 
element in the sorted 
order, not the kth distinct element. 

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of 
integers nums. int add(int 
val) Appends the integer val to the stream and returns the element representing the kth largest 
element in the stream. 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
"""


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        return

    def add(self, val: int) -> int:
        pass


"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
Return the root 
node of the BST after the insertion. It is guaranteed that the new value does not exist in the 
original BST. 

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a 
BST after insertion. 
You can return any of them. 

Example 1:

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
"""


def insertIntoBST(root: Optional[Node], val: int) -> Optional[Node]:
    return


"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that 
node. If such a 
node does not exist, return null. 

Example 1:

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:

Input: root = [4,2,7,1,3], val = 5
Output: []
"""


def searchBST(root: Optional[Node], val: int) -> Optional[Node]:
    pass


"""
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of 
children is separated by 
the null value (See examples) 

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,
null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
"""


def postorder(self, root: 'Node') -> List[int]:
    pass


"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of 
children is separated by 
the null value (See examples) 

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,
null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
"""


def preorder(self, root: 'Node') -> List[int]:
    pass


"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the 
farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of 
children is separated by 
the null value (See examples). 

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,
null,14]
Output: 5
"""


def maxDepth(root: 'Node') -> int:
    pass


"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of 
children is separated by 
the null value (See examples). 

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,
null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
"""


def levelOrder(self, root: 'Node') -> List[List[int]]:
    pass


"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each 
node in this 
tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is 
the smaller value 
among its two sub-nodes. More formally, the property root.val = min(root.left.val, 
root.right.val) always holds. 

Given such a binary tree, you need to output the second minimum value in the set made of all the 
nodes' value in the 
whole tree. 

If no such second minimum value exists, output -1 instead.

Example 1:

Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:

Input: root = [2,2,2]
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""


def findSecondMinimumValue(root: Optional[Node]) -> int:
    pass


"""
Given the root of a binary search tree and the lowest and highest boundaries as low and high, 
trim the tree so 
that all its elements lies in [low, high]. Trimming the tree should not change the relative 
structure of the elements 
that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be 
proven that there is 
a unique answer. 

Return the root of the trimmed binary search tree. Note that the root may change depending on the 
given bounds.

Example 1:

Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]
Example 2:

Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]
Example 3:

Input: root = [1], low = 1, high = 2
Output: [1]
Example 4:

Input: root = [1,null,2], low = 1, high = 3
Output: [1,null,2]
Example 5:

Input: root = [1,null,2], low = 2, high = 4
Output: [2]
"""


def trimBST(root: Optional[Node], low: int, high: int) -> Optional[Node]:
    pass


"""
You are given an integer array nums with no duplicates. A maximum binary tree can be built 
recursively from nums 
using the following algorithm: 

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.

Example 1:

Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation: The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.
Example 2:


Input: nums = [3,2,1]
Output: [3,null,2,null,1]
"""


def constructMaximumBinaryTree(nums: List[int]) -> Optional[Node]:
    pass


"""
Given the root of a Binary Search Tree and a target number k, return true if there exist two 
elements in the BST 
such that their sum is equal to the given target. 

Example 1:

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
Example 3:

Input: root = [2,1,3], k = 4
Output: true
Example 4:

Input: root = [2,1,3], k = 1
Output: false
Example 5:

Input: root = [2,1,3], k = 3
Output: true
"""


def findTarget(root: Optional[Node], k: int) -> bool:
    pass


"""
Given the root of a binary tree, return the average value of the nodes on each level in the form 
of an array. 
Answers within 10-5 of the actual answer will be accepted. 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
"""


def averageOfLevels(root: Optional[Node]) -> List[float]:
    pass


"""
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are 
overlapped while the others 
are not. You need to merge the two trees into a new binary tree. The merge rule is that if two 
nodes overlap, 
then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be 
used as the node of 
the new tree. 

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Example 1:

Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]
"""


def mergeTrees(root1: Optional[Node], root2: Optional[Node]) -> Optional[Node]:
    pass


"""
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a 
binary tree with 
the preorder traversal way, and return it. 

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship 
between the string and 
the original binary tree. 

Example 1:

Input: root = [1,2,3,4] Output: "1(2(4))(3)" Explanation: Originally, it needs to be "1(2(4)())(
3()())", but you need 
to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)" Example 2: 

Input: root = [1,2,3,null,4] Output: "1(2()(4))(3)" Explanation: Almost the same as the first 
example, 
except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship 
between the input and 
the output. """


def tree2str(root: Optional[Node]) -> str:
    pass


"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may 
not pass through the root. 

The length of a path between two nodes is represented by the number of edges between them.

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
"""


def diameterOfBinaryTree(root: Optional[Node]) -> int:
    pass


"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of 
the original BST 
is changed to the original key plus the sum of all keys greater than the original key in BST. 

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
Example 2:

Input: root = [0,null,1]
Output: [1,null,1]
Example 3:

Input: root = [1,0,2]
Output: [3,3,2]
Example 4:

Input: root = [3,2,4,1]
Output: [7,9,4,10]
"""


def convertBST(root: Optional[Node]) -> Optional[Node]:
    pass


"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the 
values of any two different nodes in the tree.

Example 1:

Input: root = [4,2,6,1,3]
Output: 1
Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1

"""


def getMinimumDifference(root: Optional[Node]) -> int:
    pass


"""
Serialization is converting a data structure or object into a sequence of bits so that it can be 
stored in a file 
or memory buffer, or transmitted across a network connection link to be reconstructed later in 
the same or another 
computer environment. 

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on 
how your 
serialization/deserialization algorithm should work. You need to ensure that a binary search tree 
can be serialized 
to a string, and this string can be deserialized to the original tree structure. 

The encoded string should be as compact as possible.

Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
Example 2:

Input: root = []
Output: []
"""


# Definition for a binary tree node.
# class Node:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Node) -> str:
        """Encodes a tree to a single string.
        """

    def deserialize(self, data: str) -> Node:
        """Decodes your encoded data to tree.
        """


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans


"""
Given the root of a binary tree, return the sum of all left leaves.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
"""


def sumOfLeftLeaves(root: Optional[Node]) -> int:
    pass


"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]
"""


def binaryTreePaths(root: Optional[Node]) -> List[str]:
    pass


"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes p and q as 
the lowest node in T that has both p and q as descendants (where we allow a node to be a 
descendant of itself).” 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according 
to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
"""


def lowestCommonAncestor(root: 'Node', p: 'Node', q: 'Node') -> 'Node':
    pass


"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (
1-indexed) of all the 
values of the nodes in the tree. 

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""


def kthSmallest(self, root: Optional[Node], k: int) -> int:
    pass


"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:

Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
"""


def invertTree(root: Optional[Node]) -> Optional[Node]:
    pass


"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the 
values of the nodes 
you can see ordered from top to bottom. 

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
"""


def rightSideView(root: Optional[Node]) -> List[int]:
    pass


"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a 
binary search tree (BST):

BSTIterator(Node root) Initializes an object of the BSTIterator class. The root of the BST is 
given as part of 
the constructor. The pointer should be initialized to a non-existent number smaller than any 
element in the BST. 
boolean hasNext() Returns true if there exists a number in the traversal to the right of the 
pointer, 
otherwise returns false. int next() Moves the pointer to the right, then returns the number at 
the pointer. Notice 
that by initializing the pointer to a non-existent smallest number, the first call to next() will 
return the smallest 
element in the BST. 

You may assume that next() calls will always be valid. That is, there will be at least a next 
number in the in-order 
traversal when next() is called. 

Example 1:

Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
"""


# Definition for a binary tree node.
# class Node:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[Node]):
        pass

    def next(self) -> int:
        pass

    def hasNext(self) -> bool:
        pass


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,2]
Output: [1,2]
Example 5:

Input: root = [1,null,2]
Output: [1,2]
 
"""


def preorderTraversal(root: Optional[Node]) -> List[int]:
    pass


"""
Given a binary tree

struct Node { int val; Node *left; Node *right; Node *next; } Populate each next pointer to point 
to its next right 
node. If there is no next right node, the next pointer should be set to NULL. 

Initially, all next pointers are set to NULL.

Example 1:

Input: root = [1,2,3,4,5,null,7] Output: [1,#,2,3,#,4,5,7,#] Explanation: Given the above binary 
tree (Figure A), 
your function should populate each next pointer to point to its next right node, just like in 
Figure B. The 
serialized output is in level order as connected by the next pointers, with '#' signifying the 
end of each level. 
Example 2: 

Input: root = []
Output: []
"""


def connect(root: 'Node') -> 'Node':
    pass


"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has 
two children. The 
binary tree has the following definition: 

struct Node { int val; Node *left; Node *right; Node *next; } Populate each next pointer to point 
to its next right 
node. If there is no next right node, the next pointer should be set to NULL. 

Initially, all next pointers are set to NULL.

Example 1:

Input: root = [1,2,3,4,5,6,7] Output: [1,#,2,3,#,4,5,6,7,#] Explanation: Given the above perfect 
binary tree (Figure 
A), your function should populate each next pointer to point to its next right node, just like in 
Figure B. The 
serialized output is in level order as connected by the next pointers, with '#' signifying the 
end of each level. 
Example 2: 

Input: root = []
Output: []
"""


def connect2(self, root: 'Node') -> 'Node':
    pass


"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a 
root-to-leaf path such 
that adding up all the values along the path equals targetSum. 

A leaf is a node with no children.

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
"""


def hasPathSum(root: Optional[Node], targetSum: int) -> bool:
    pass


"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the 
nearest leaf node.

Note: A leaf is a node with no children.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""


def minDepth(root: Optional[Node]) -> int:
    pass


"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
"""


def isBalanced(root: Optional[Node]) -> bool:
    pass


"""
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. 
(i.e., 
from left to right, level by level from leaf to root). 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""


def levelOrderBottom(root: Optional[Node]) -> List[List[int]]:
    pass


"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node 
down to the farthest 
leaf node. 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
Example 3:

Input: root = []
Output: 0
Example 4:

Input: root = [0]
Output: 1
"""


def maxDepth2(root: Optional[Node]) -> int:
    pass


"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (
i.e., from left to 
right, then right to left for the next level and alternate between). 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""


def zigzagLevelOrder(root: Optional[Node]) -> List[List[int]]:
    pass


"""Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., 
from left to right, 
level by level). 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""


def levelOrder2(self, root: Optional[Node]) -> List[List[int]]:
    pass


"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around 
its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false
"""


def isSymmetric(root: Optional[Node]) -> bool:
    pass


"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have 
the same value.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false
"""


def isSameTree(p: Optional[Node], q: Optional[Node]) -> bool:
    pass


"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

Input: root = [2,1,3]
Output: true
Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


def isValidBST(root: Optional[Node]) -> bool:
    pass


"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.=

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [1,2]
"""


def inorderTraversal(self, root: Optional[Node]) -> List[int]:
    pass


"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
"""


def pathSum(root: Optional[Node], targetSum: int) -> List[List[int]]:
    pass


"""
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

 

Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:

Input: root = [0]
Output: 0
"""


def sumRootToLeaf(root: Optional[Node]) -> int:
    pass
