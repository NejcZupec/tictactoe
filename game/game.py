import random

from utils import all_equal


class Game(object):
    """
    A tic-tac-toe game. A whitespace (' ') represents a blank field.
    """

    def __init__(self, board=None, moves=None):
        """
        Initialize a TicTacToe game with specific moves and board.
        """
        self.board = [[' ' for _ in range(3)] for _ in range(3)] if board is None else board
        self.moves = [] if moves is None else moves  # every move is presented as a tuple (player, x, y)

    def print_board(self):
        """
        Human readable representation of the board state.
        """
        print
        for i, row in enumerate(self.board):
            print '%s | %s | %s' % tuple(row)
            print '---------' if not i == 2 else ''

    def move(self, player, x, y):
        """
        Player 'x' or 'o' changes the state one the board[x][y]. Before the move, all constraints (valid moves, etc.)
        are checked.
        """
        assert player in ['o', 'x'], "A possible player is only 'o' or 'x'."
        assert x in [0, 1, 2], "X should be 0, 1 or 2."
        assert y in [0, 1, 2], "Y should be 0, 1 or 2."
        assert self.board[x][y] not in ['o', 'x'], "This position is already occupied."
        assert len(self.moves) == 0 or not self.moves[-1][0] == player, "The other player should play."

        self.board[x][y] = player
        move = (player, x, y)
        self.moves.append(move)

    def get_winner_or_draw(self):
        """
        Returns status of the game. If a player wins, returns 'o' or 'x'. If the board is full and no one won, return
        'draw'. Otherwise return None.
        """
        if len(self.moves) > 4:
            last_player = self.moves[-1][0]

            # diagonal win
            d1 = [row[i] for i, row in enumerate(self.board)]
            if all_equal(d1):
                return last_player
            d2 = [row[-i-1] for i, row in enumerate(self.board)]
            if all_equal(d2):
                return last_player

            # horizontal win
            for row in self.board:
                if all_equal(row):
                    return last_player

            # vertical win
            for row in zip(*self.board):  # transpose the board
                if all_equal(row):
                    return last_player

            # draw game, no winner, the board is full
            if len(self.moves) == 9:
                return 'draw'

        return None

    def get_empty_fields(self):
        """
        Return a list of empty fields, e.g. [(0, 1), (1, 1)].
        """
        result = []
        for i, row in enumerate(self.board):
            for j, _ in enumerate(row):
                if self.board[i][j] == ' ':
                    result.append((i, j))
        return result

    def next_random_move(self):
        """
        Randomly choose an empty field, e.g. (2, 1).
        """
        empty_fields = self.get_empty_fields()
        return random.choice(empty_fields)

