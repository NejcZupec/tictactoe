class Game(object):
    """
    A tic-tac-toe game.
    """

    def __init__(self):
        """
        Initialize an empty board (2D array). A whitespace (' ') represents a blank field.
        """
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.moves = []  # every move is presented as a tuple (player, x, y)

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
            d1 = [self.board[i][i] for i in range(len(self.board))]
            if self._all_equal(d1):
                return last_player
            d2 = [row[i] for i, row in enumerate(self.board)]
            if self._all_equal(d2):
                return last_player

            # horizontal win
            for row in self.board:
                if self._all_equal(row):
                    return last_player

            # vertical win
            for row in zip(*self.board):  # transpose the board
                if self._all_equal(row):
                    return last_player

            # Draw game. No winner, the board is full.
            if len(self.moves) == 9:
                return 'draw'

        return None

    @staticmethod
    def _all_equal(row):
        return not row[0] == ' ' and row[1:] == row[:-1]
