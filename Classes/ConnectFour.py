import random


class ConnectFour:
    def __init__(self, size):
        self.board = [[None for _ in range(size)] for _ in range(size)]
        self.possible_moves = {(len(self.board) - 1, y) for y in range(size)}
        self.turn = random.choice([0, 1])
        self.winner = False
        self.play()

    def play(self):
        while self.possible_moves:
            self.print_board()
            if self.turn == 1:
                x, y = self.make_human_move()
            else:
                x, y = self.make_computer_move()
            if self.detect_winner(x, y, self.turn):
                self.winner = True
                break
            self.turn = not self.turn
        self.print_board()
        if not self.winner:
            print('TIE!')
        elif self.turn:
            print('HUMAN WINNER!')
        else:
            print('COMPUTER WINNER!')

    def print_board(self):
        for row in self.board:
            print(row)
        print('~~~~~~~~~~~~~~~~~~~~~~')

    def detect_winner(self, x, y, player):
        def detect_winner_recursive(x, y, direction, player):
            result = 0
            if 0 <= x < len(self.board) and 0 <= y < len(self.board[0]) and self.board[x][y] == player:
                result += 1
                result += detect_winner_recursive(x + direction[0], y + direction[1], direction, player)
            return result

        max_in_direction = 0
        directions = [[[-1, 0], [1, 0]], [[0, -1], [0, 1]], [[-1, -1], [1, 1]], [[-1, 1], [1, -1]]]

        for direction_a, direction_b in directions:
            direction_val = detect_winner_recursive(x + direction_a[0], y + direction_a[1], direction_a, player) + \
                            detect_winner_recursive(x + direction_b[0], y + direction_b[1], direction_b, player) + 1
            max_in_direction = max(max_in_direction, direction_val)

        return max_in_direction >= 4

    def make_human_move(self):
        while True:
            print('available moves: ' + str(self.possible_moves))
            input_x = int(input('x coordinate'))
            input_y = int(input('y coordinate'))
            if self.board[input_x][input_y] is None and (input_x, input_y) in self.possible_moves:
                self.board[input_x][input_y] = 1
                self.possible_moves.remove((input_x, input_y))
                if input_x != 0:
                    self.possible_moves.add((input_x - 1, input_y))
                return input_x, input_y

    def make_computer_move(self):
        x_move = y_move = None
        for x, y in self.possible_moves:
            # if there's a move that will win or will block, make that move.
            if self.detect_winner(x, y, 0) or self.detect_winner(x, y, 1):
                x_move, y_move = x, y
        if not x_move and not y_move:
            x_move, y_move = random.choice(list(self.possible_moves))
        self.board[x_move][y_move] = 0
        self.possible_moves.remove((x_move, y_move))
        if x_move != 0:
            self.possible_moves.add((x_move - 1, y_move))
        return x_move, y_move


connect_four = ConnectFour(int(input('size')))
