import random


class ConnectFour:
    def __init__(self, board_size):
        self.board = [[None for _ in range(board_size)] for _ in range(board_size)]
        self.turn = True
        self.available_moves = {(board_size - 1, x) for x in range(board_size)}
        self.winner = None

    def check_winner(self, x, y, turn):
        directions = [[[-1, -1], [1, 1]], [[1, -1], [-1, 1]], [[-1, 0], [1, 0]], [[0, 1], [0, -1]]]

        def recursive_check(x, y, direction):
            result = 0
            if 0 <= x < len(self.board) and 0 <= y < len(self.board[0]) and self.board[x][y] == turn:
                result += 1
                result += recursive_check(x + direction[0], y + direction[1], direction)
            return result

        for direction_a, direction_b in directions:
            if recursive_check(x + direction_a[0], y + direction_a[1], direction_a) + recursive_check(
                    x + direction_b[0], y + direction_b[1], direction_b) + 1 == 4:
                return True

    def pick_move(self):
        for available_move_x, available_move_y in self.available_moves:
            if self.check_winner(available_move_x, available_move_y, True) or self.check_winner(available_move_x,
                                                                                                available_move_y,
                                                                                                False):
                return available_move_x, available_move_y
        return random.choice(list(self.available_moves))

    def print_board(self):
        for x, row in enumerate(self.board):
            print(row)
        print('~~~~~~~~~~~')

    def play(self):
        while self.winner is None and self.available_moves:
            if self.turn:
                self.print_board()
                print('available moves: %s', str(self.available_moves))
                x = int(input('x coordinate'))
                y = int(input('y coordinate'))
            else:
                x, y = self.pick_move()
            self.available_moves.remove((x, y))
            if x != 0:
                self.available_moves.add((x - 1, y))
            self.board[x][y] = self.turn
            if self.check_winner(x, y, self.turn):
                self.winner = self.turn
            self.turn = not self.turn

        self.print_board()
        if self.winner is not None:
            print('WINNER:', 'human' if self.winner else 'computer')
        else:
            print('TIE!')


connect_four = ConnectFour(int(input('board size')))
connect_four.play()
