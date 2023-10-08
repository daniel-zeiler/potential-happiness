"""
Find the largest perimeter of an island given a 2 dimensional array of 1's and 0's representing
land and water respectively.

Land = 1
Water = 0
Island = contiguous 1's that are adjacent to other 1's to the left, right, up, or down

Edge of an island = any 1 that is adjacent to a 0 OR grid boundary to the left, right, up, or down

Perimeter = total # of 1's on the edge of an island

Example 1:

Input:
[[1, 0, 1, 1, 1],
 [1, 0, 1, 1, 1],
 [0, 1, 0, 1, 1]]

Output: 7 (Island on the right)
Example 2:

Input:
[[0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 1, 1, 1, 0],
 [0, 1, 0, 1, 1, 1, 0],
 [0, 0, 1, 1, 1, 1, 0],
 [0, 0, 0, 0, 0, 0, 0]]

Output: 9 (Island on the right)
"""
from typing import List


def largest_parameter(input):
    pass


"""
There is a city composed of n x n blocks, where each block contains a single building shaped like 
a vertical square prism. You are given a 0-indexed n x n integer matrix grid where grid[r][c] 
represents the height of the building located in the block at row r and column c.

A city's skyline is the the outer contour formed by all the building when viewing the side of the 
city from a distance. The skyline from each cardinal direction north, east, south, and west may 
be different.

We are allowed to increase the height of any number of buildings by any amount (the amount can be 
different per building). The height of a 0-height building can also be increased. However, 
increasing the height of a building should not affect the city's skyline from any cardinal 
direction.

Return the maximum total sum that the height of the buildings can be increased by without 
changing the city's skyline from any cardinal direction.



Example 1:


Input: grid = [
  [3,0,8,4],
  [2,4,5,7],
  [9,2,6,3],
  [0,3,1,0]
]
Output: 35
Explanation: The building heights are shown in the center of the above image.
The skylines when viewed from each cardinal direction are drawn in red.
The grid after increasing the height of buildings without affecting skylines is:
gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
Example 2:

Input: grid = [[0,0,0],[0,0,0],[0,0,0]]
Output: 0
Explanation: Increasing the height of any building will result in the skyline changing.
"""


def maxIncreaseKeepingSkyline(grid: List[List[int]]) -> int:
    pass


"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.



Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
"""


def countSquares(matrix: List[List[int]]) -> int:
    pass


"""
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number 
of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only 
be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any 
size. At least one horizontal or vertical cell separates between two battleships (i.e., there are 
no adjacent battleships).



Example 1:


Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
Example 2:

Input: board = [["."]]
Output: 0
"""


def countBattleships(board: List[List[str]]) -> int:
    pass


"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][
j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely 
surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the 
island. One cell is a square with side length 1. The grid is rectangular, width and height don't 
exceed 100. Determine the perimeter of the island.



Example 1:


Input: grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]

Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
"""


def islandPerimeter(grid: List[List[int]]) -> int:
    pass


"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are 
surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,
0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,
0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    pass


"""
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount 
of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.


Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
"""


def getMaximumGold(grid: List[List[int]]) -> int:
    pass


"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, 
right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next 
click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' 
and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit (
'1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.


Example 1:


Input: board = [
  ["E","E","E","E","E"],
  ["E","E","M","E","E"],
  ["E","E","E","E","E"],
  ["E","E","E","E","E"]
], click = [3,0]
Output: [
  ["B","1","E","1","B"],
  ["B","1","M","1","B"],
  ["B","1","1","1","B"],
  ["B","B","B","B","B"]
  ]
Example 2:


Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B",
"B","B"]], click = [1,2]
Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
"""


def updateBoard(board: List[List[str]], click: List[int]) -> List[List[str]]:
    pass


"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular 
automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (
represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (
horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia 
article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current 
state, where births and deaths occur simultaneously. Given the current state of the m x n grid 
board, return the next state.



Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.


Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You 
cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, 
which would cause problems when the active area encroaches upon the border of the array (i.e., 
live cells reach the border). How would you address these problems?
"""


def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """


"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land 
cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or 
walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in 
any number of moves.



Example 1:


Input: grid = [
  [0,0,0,0],
  [1,0,1,0],
  [0,1,1,0],
  [0,0,0,0]
]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because 
its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
"""


def numEnclaves(grid: List[List[int]]) -> int:
    pass


"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""


def minPathSum(grid: List[List[int]]) -> int:
    pass


"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel 
value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the 
image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally 
to the starting pixel of the same color as the starting pixel, plus any pixels connected 
4-directionally to those pixels (also with the same color), and so on. Replace the color of all 
of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.



Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), 
all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) 
are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the 
starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
"""


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    pass


"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or 
vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""


def numIslands(grid: List[List[str]]) -> int:
    pass


"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this 
is impossible, return -1.



Example 1:


Input: grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, 
because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""


def orangesRotting(grid: List[List[int]]) -> int:
    pass


"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's 
and return its area.



Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0",
"1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
"""


def maximalSquare(matrix: List[List[str]]) -> int:
    pass


"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If 
there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the 
bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and 
they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.



Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [
  [0,0,0],
  [1,1,0],
  [1,1,0]
  ]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
"""


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    pass


"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""


def exist(board: List[List[str]], word: str) -> bool:
    pass


"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean 
touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges. 

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[
r][c] represents the height above sea level of the cell at coordinate (r, c). 

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, 
and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any 
cell adjacent to an ocean into the ocean. 

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (
ri, ci) to both the Pacific and Atlantic oceans. 



Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
"""


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    pass


"""
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.


Example 1:

Input
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]

Explanation
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
"""


class TicTacToe:

    def __init__(self, n: int):
        pass

    def move(self, row: int, col: int, player: int) -> int:
        pass


"""

You are running a gravity simulation involving falling boxes and breakable obstacles.
The situation is represented by a rectangular matrix of characters board.

Each cell of the matrix board contains one of three characters:

'.', which means that the cell is empty;
'*', which means that the cell contains an obstacle;
'#', which means that the cell contains a box.

The boxes each fall down simultaneously as far as possible, until hitting an obstacle, another grounded box, 
or the bottom of the board. If a box hits an obstacle then the box explodes, destroying itself and any other boxes 
within the eight cells surrounding the obstacle. 

All the explosions happen simultaneously as well.

Given board, your task is to return the state of the board after all boxes have fallen.

Example

For


board = [['#', '.', '#', '#', '*'],
         ['#', '.', '.', '#', '#'],
         ['.', '#', '.', '#', '.'],
         ['.', '.', '#', '.', '#'],
         ['#', '*', '.', '.', '.'],
        ['.', '.', '*', '#', '.']]
the output should be

fallAndCrush2(board)

[['.', '.', '.', '.', '*'],
['.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.'],
['.', '*', '.', '.', '#'],
['#', '.', '*', '.', '#']]
"""


def fallAndCrush2(board):
    pass


"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands 
in grid. 

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.



Example 1:

Input: grid = [
    [0,1],[1,0]
]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
"""


def shortestBridge(self, grid: List[List[int]]) -> int:
    pass
