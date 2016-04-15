import random

from copy import deepcopy

from utils import all_equal, list_not_all_none


def board_state_print(board_state):
    """
    Human readable representation of the board state.
    """
    print
    for i, row in enumerate(board_state):
        print '%s | %s | %s' % tuple(row)
        print '---------' if not i == 2 else ''


def board_state_possible_moves(board_state):
    result = []
    for i, row in enumerate(board_state):
        for j, column in enumerate(row):
            if board_state[i][j] == ' ':
                result.append((i, j))
    return result


def board_state_status(board_state):
    """
    Return 'winner', 'draw' or None.
    """

    # diagonal win
    d1 = [row[i] for i, row in enumerate(board_state)]
    if all_equal(d1):
        return d1[0]
    d2 = [row[-i-1] for i, row in enumerate(board_state)]
    if all_equal(d2):
        return d2[0]

    # horizontal win
    for row in board_state:
        if all_equal(row):
            return row[0]

    # vertical win
    for row in zip(*board_state):  # transpose the board
        if all_equal(row):
            return row[0]

    # draw game, no winner, the board is full
    if not board_state_possible_moves(board_state):
        return 'draw'

    return None


def board_state_after_move(board_state, move):
    p, x, y = move
    new_board_state = deepcopy(board_state)
    new_board_state[x][y] = p
    return new_board_state


def board_state_score(board_state, ai_player):
    result = board_state_status(board_state)

    if not result:
        return None

    if result == ai_player:
        return 1
    elif result == 'draw':
        return 0
    else:
        return -1


def board_state_score_possible_moves(board_state, ai_player):
    scores = []
    for field in board_state_possible_moves(board_state):
        m = (ai_player, field[0], field[1])
        b = board_state_after_move(board_state, m)
        scores.append(board_state_score(b, ai_player))
    return scores


def minimax(bs, ai_player, move):
    current_player = move[0]
    new_bs = board_state_after_move(bs, move)

    # game is finished
    if not board_state_possible_moves(new_bs):
        return board_state_score(new_bs, ai_player)

    # change player
    current_player = 'o' if current_player == 'x' else 'x'

    # get scores for all possible moves
    scores = []
    for empty_field in board_state_possible_moves(new_bs):
        m = (current_player, empty_field[0], empty_field[1])
        new_new_bs = board_state_after_move(new_bs, m)
        scores.append(board_state_score(new_new_bs, ai_player))

    # if game is ended, return score
    if list_not_all_none(scores):
        if ai_player == current_player:
            return max(scores)
        else:
            return min(scores)

    # game is not ended, recursion
    else:
        moves = [(current_player, empty_field[0], empty_field[1]) for empty_field in board_state_possible_moves(new_bs)]

        if ai_player == current_player:
            return max([minimax(new_bs, ai_player, m) for m in moves])
        else:
            return min([minimax(new_bs, ai_player, m) for m in moves])


class TicTacToeAI(object):

    def __init__(self, board=None, ai_player=None):
        self.board = [[' ' for _ in range(3)] for _ in range(3)] if board is None else board
        self.ai_player = 'x' if ai_player is None else ai_player

    def print_board(self):
        board_state_print(self.board)

    def move(self, player, x, y):
        self.board[x][y] = player

    def possible_moves(self):
        """
        Return a list of possible moves, e.g. [(0, 1), (1, 1)].
        """
        return board_state_possible_moves(self.board)

    def board_status(self):
        """
        Return a winner ('x' or 'o'), 'draw' or None.
        """
        return board_state_status(self.board)

    def score_possible_moves(self):
        return board_state_score_possible_moves(self.board, self.ai_player)

    def get_next_move(self):
        """
        Calculate next move with Minimax algorithm.
        """

        # if board is empty, return random move
        if len(self.possible_moves()) == 9:
            return random.randint(0, 2), random.randint(0, 2)

        # can win in one move
        scores = board_state_score_possible_moves(self.board, self.ai_player)
        if 1 in scores:
            return board_state_possible_moves(self.board)[scores.index(1)]

        good_moves = []
        draw_moves = []
        bad_moves = []

        for field in board_state_possible_moves(self.board):
            m = (self.ai_player, field[0], field[1])
            score = minimax(self.board, self.ai_player, m)

            if score == 1:
                good_moves.append(m)
            elif score == 0:
                draw_moves.append(m)
            else:
                bad_moves.append(m)

        if good_moves:
            selected_move = random.choice(good_moves)
        elif draw_moves:
            selected_move = random.choice(draw_moves)
        else:
            selected_move = random.choice(bad_moves)

        return selected_move[1], selected_move[2]
