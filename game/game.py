class Game(object):
    """
    A tic-tac-toe game.
    """

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.moves = []  # every move is presented as a tuple (player, x, y)

    def print_board(self):
        print
        for i, row in enumerate(self.board):
            print '%s | %s | %s' % tuple(row)
            print '---------' if not i == 2 else ''

    def move(self, player, x, y):
        assert player in ['o', 'x'], "A possible player is only 'o' or 'x'."
        assert x in [0, 1, 2], "X should be 0, 1 or 2."
        assert y in [0, 1, 2], "Y should be 0, 1 or 2."
        assert self.board[x][y] not in ['o', 'x'], "This position is already occupied."
        assert len(self.moves) == 0 or not self.moves[-1][0] == player, "The other player should play."

        self.board[x][y] = player
        move = (player, x, y)
        self.moves.append(move)

    def is_game_ended(self):
        if len(self.moves) > 4:

            # diagonal win
            d1 = [self.board[i][i] for i in range(len(self.board))]
            if self.all_equal(d1):
                return True

            d2 = [row[i] for i, row in enumerate(self.board)]
            if self.all_equal(d2):
                return True

            # horizontal win
            for row in self.board:
                if self.all_equal(row):
                    return True

            # vertical win
            for row in zip(*self.board):  # transpose board
                if self.all_equal(row):
                    return True

        return False

    @staticmethod
    def all_equal(row):
        return not row[0] == ' ' and row[1:] == row[:-1]


if __name__ == '__main__':
    g = Game()

    # Game example
    g.print_board()
    g.move('x', 0, 1)
    g.print_board()
    g.move('o', 0, 0)
    g.print_board()
    g.move('x', 1, 1)
    g.print_board()

