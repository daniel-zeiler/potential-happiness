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
        def detect_winner_recursive(x, y, directions, player):
            result = 0
            if 0 <= x < len(self.board) and 0 <= y < len(self.board[0]) and self.board[x][y] == player:
                result += 1
                result += detect_winner_recursive(x + directions[0], y + directions[1], directions, player)
            return result

        vertical = detect_winner_recursive(x - 1, y, [-1, 0], player) + \
                   detect_winner_recursive(x + 1, y, [1, 0], player) + 1

        horitzonal = detect_winner_recursive(x, y - 1, [0, -1], player) + \
                     detect_winner_recursive(x, y + 1, [0, 1], player) + 1

        diag_left = detect_winner_recursive(x - 1, y - 1, [-1, -1], player) + \
                    detect_winner_recursive(x + 1, x + 1, [1, 1], player) + 1

        diag_right = detect_winner_recursive(x + 1, y - 1, [1, -1], player) + \
                     detect_winner_recursive(x - 1, y + 1, [-1, 1], player) + 1

        return vertical >= 4 or horitzonal >= 4 or diag_left >= 4 or diag_right >= 4

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
        x, y = random.choice(list(self.possible_moves))
        self.board[x][y] = 0
        self.possible_moves.remove((x, y))
        if x != 0:
            self.possible_moves.add((x - 1, y))
        return x, y


connect_four = ConnectFour(int(input('size')))
