from typing import List

"""
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end
with a special character '#').

You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously
typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character
except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already
typed.

Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before. The
returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have
the same hot degree, use ASCII-code order (smaller one appears first). If less than 3 hot sentences exist,
return as many as you can. When the input is a special character, it means the sentence ends, and in this case,
you need to return an empty list. Implement the AutocompleteSystem class:

AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
List<String> input(char c) This indicates that the user typed the character c. Returns an empty array [] if c == '#'
and stores the inputted sentence in the system. Returns the top 3 historical hot sentences that have the same prefix
as the part of the sentence already typed. If there are fewer than 3 matches, return them all.


Example 1:

Input
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
Output
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

Explanation AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"],
[5, 3, 2, 2]); obj.input("i"); // return ["i love you", "island", "i love leetcode"]. There are four sentences that
have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and
'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot
sentences, so "ironman" will be ignored. obj.input(" "); // return ["i love you", "i love leetcode"]. There are only
two sentences that have prefix "i ". obj.input("a"); // return []. There are no sentences that have prefix "i a".
obj.input("#"); // return []. The user finished the input, the sentence "i a" should be saved as a historical
sentence in system. And the following input will be counted as a new search.

"""
import collections
import heapq


class AutocompleteSystem:
    def __init__(self, words: List[str], times: [int]):
        pass

    def input_character(self, character: str) -> List[str]:
        pass


"""
A binary search tree.
"""


class BinarySearchTree:
    def __init__(self):
        pass

    def insert(self):
        pass

    def level_order_traversal(self):
        pass

    def delete(self):
        pass


"""
Lets play connect four!

Initialize with input with:
    connect_four = ConnectFour(int(input('size')))
    Either human or computer start first
        if the computer detects that theres a winning move or will bock, it should make that move
    Detect winner or draw!
"""


class ConnectFour:
    def __init__(self, size):
        pass

    def __str__(self):
        pass

    def play(self):
        pass

    def detect_winner(self, x, y, player):
        pass

    def make_human_move(self):
        pass

    def make_computer_move(self):
        pass


"""
A filesystem!
"""


class FileSystem:
    def __init__(self):
        pass

    def add_file(self, file_path, contents):
        pass

    def add_directory(self, file_path):
        pass

    def list_directory(self, file_path):
        pass

    def read_file(self, file_path):
        pass


"""
LRU Cache
"""


class LRUCache:
    def __init__(self, capacity: int):
        pass

    def add_item(self, key: str, value: int):
        pass

    def get_item(self, key: str):
        pass

    def update_item(self, key: str, value: int):
        pass


"""
Stock exchange!
create buy order, create listing, create sell order
"""


class StockExchange:
    def __init__(self):
        pass

    def buy_order(self, order):
        pass

    def sell_order(self, order):
        pass


"""The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle
value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


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
Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the
answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has
two attributes:

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

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid
and set the four children to Null and stop. If the current grid has different values, set isLeaf to False and set val
to any value and divide the current grid into four sub-grids as shown in the photo. Recurse for each of the children
with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path
terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a
list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or
val is False we represent it as 0.



Example 1:


Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.

Example 2:



Input: grid = [
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0]
]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:



Constraints:

n == grid.length == grid[i].length
n == 2x where 0 <= x <= 6

"""


class Node:
    def __init__(self, is_leaf, val=None, top_left=None, top_right=None, bottom_left=None, bottom_right=None):
        self.val = val
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.is_leaf = is_leaf


class QuadTree:
    def __init__(self, input):
        pass


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
        return uber_quad_tree_node


"""
Text Editor
"""


class TextEditor:
    def __init__(self, text=''):
        pass

    def update_state(self):
        pass

    def undo(self):
        pass

    def redo(self):
        pass

    def append(self, a_string):
        pass

    def move(self, position):
        pass

    def backspace(self):
        pass

    def select(self, start, end):
        pass

    def copy(self):
        pass

    def paste(self):
        pass

    def cut(self):
        pass
