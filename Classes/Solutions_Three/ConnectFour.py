import random


class ConnectFour:
    def __init__(self, size=6):
        self.size = size
        self.board = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.turn = random.choice([False, True])
        self.available_moves = {(self.size - 1, n) for n in range(self.size)}
        self.winner = None

    """
    Visualize the board.
    """

    def print_board(self):
        for row in self.board:
            print(row)
        print('~~~~~~~~~~~~~~~~~~')

    """
    Get input from human user.
    """

    def human_move(self):
        x = None
        y = None
        print('pick a move: ' + str(self.available_moves))
        while (x, y) not in self.available_moves:
            (x, y) = int(input('input x coordinate')), int(input('input y coordinate'))
        return x, y

    """
    If possible, make winning move.  Else make blocking move.  Else move randomly.
    """

    def smarter_robo_move(self):
        for moves in self.available_moves:
            if self.check_move(moves[0], moves[1], False, 3):
                return moves[0], moves[1]

        for moves in self.available_moves:
            if self.check_move(moves[0], moves[1], True, 3):
                return moves[0], moves[1]

        return random.choice(list(self.available_moves))

    """
    Return true if for any direction pair we reach the target value.  
    Otherwise return False.
    """

    def check_move(self, x, y, player_id, target_value):
        def recursive_check(x, y, direction):
            result = 0
            if 0 <= x < len(self.board) and 0 <= y < len(self.board[0]) and self.board[x][y] == player_id:
                result += recursive_check(x + direction[0], y + direction[1], direction) + 1
            return result

        direction_pairs = [[[-1, 0], [1, 0]], [[0, 1], [0, -1]], [[-1, -1], [1, 1]], [[-1, 1], [1, -1]]]
        return any([recursive_check(x, y, direction_a) + recursive_check(x, y, direction_b) >= target_value for
                    direction_a, direction_b in direction_pairs])

    def play(self):
        while self.winner is None and self.available_moves:
            self.print_board()
            if self.turn:
                x, y = self.human_move()
            else:
                x, y = self.smarter_robo_move()
            self.board[x][y] = self.turn
            self.available_moves.remove((x, y))
            if x != 0:
                self.available_moves.add((x - 1, y))

            if self.check_move(x, y, self.turn, 5):
                self.winner = self.turn
            else:
                self.turn = not self.turn

        self.print_board()
        if self.winner is not None:
            print('~~WINNER~~')
            if self.turn:
                print('HUMAN!')
            else:
                print('COMPUTE!')
        else:
            print('TIE!')


connect_four = ConnectFour(int(input('board size')))
connect_four.play()
