
from game import Game

ai_player = 'x'


def score(g):
    result = g.get_winner_or_draw()

    if result == ai_player:
        return 1
    elif result == 'draw':
        return 0
    else:
        return 0


def minimax(g):

    # if end, return score
    if g.get_winner_or_draw():
        return score(g)

    scores = []
    moves = []

    for x, y in g.get_empty_fields():
        possible_game = g.move()


if __name__ == '__main__':
    g = Game()
    g.print_board()
