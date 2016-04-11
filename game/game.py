class Game:
    """
    A tic-tac-toe game.
    """
    board = []

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for i, row in enumerate(self.board):
            print '%s | %s | %s' % tuple(row)
            print '---------' if not i == 2 else ''

    def move(self, player, x, y):
        assert player in ['o', 'x'], "A possible player is only 'o' or 'x'."
        assert x in [0, 1, 2], "X should be 0, 1 or 2."
        assert y in [0, 1, 2], "Y should be 0, 1 or 2."

        self.board[x][y] = player


if __name__ == '__main__':
    g = Game()

    # Game example
    g.print_board()
    g.move('x', 0, 1)
    g.print_board()
    g.move('o', 0, 0)
    g.print_board()

