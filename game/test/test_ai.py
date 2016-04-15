from django.test import TestCase

from game.ai import TicTacToeAI


class TicTacToeAITest(TestCase):

    def setUp(self):
        board_state = [['o', ' ', 'x'],
                       ['x', ' ', ' '],
                       ['x', 'o', 'o']]

        self.g = TicTacToeAI(board_state)

    def test_possible_moves(self):
        self.assertEqual(self.g.possible_moves(), [(0, 1), (1, 1), (1, 2)])

    def test_winner_o(self):
        self.assertEqual(self.g.board_status(), None)
        self.g.move('o', 1, 1)
        self.assertEqual(self.g.board_status(), 'o')

    def test_winner_x(self):
        self.assertEqual(self.g.board_status(), None)
        self.g.move('x', 1, 1)
        self.assertEqual(self.g.board_status(), 'x')

    def test_draw_board_status(self):
        draw_board_state = [['o', 'o', 'x'],
                            ['x', 'x', 'o'],
                            ['o', 'x', 'o']]
        g = TicTacToeAI(draw_board_state)
        self.assertEqual(g.board_status(), 'draw')

    def test_score_possible_moves(self):
        self.assertEqual(self.g.score_possible_moves(), [None, 1, None])


class TestSpecificGameStates(TestCase):

    def test_state_1(self):
        bs = [['o', 'x', 'x'],
              ['x', ' ', 'o'],
              ['x', 'o', 'o']]

        g = TicTacToeAI(bs, 'x')
        self.assertEqual(g.get_next_move(), (1, 1))

    def test_state_2(self):
        bs = [['o', 'x', 'x'],
              ['x', ' ', 'o'],
              ['x', 'o', 'o']]

        g = TicTacToeAI(bs, 'o')
        self.assertEqual(g.get_next_move(), (1, 1))

    def test_state_3(self):
        bs = [['o', ' ', 'x'],
              ['x', ' ', ' '],
              ['x', 'o', 'o']]

        g = TicTacToeAI(bs, 'x')
        self.assertEqual(g.get_next_move(), (1, 1))

    def test_state_4(self):
        bs = [['o', ' ', 'x'],
              ['x', ' ', ' '],
              ['x', 'o', 'o']]

        g = TicTacToeAI(bs, 'o')
        self.assertEqual(g.get_next_move(), (1, 1))

    def test_state_5(self):
        bs = [['o', 'x', 'x'],
              ['x', ' ', ' '],
              ['x', 'o', 'o']]

        g = TicTacToeAI(bs, 'x')
        self.assertEqual(g.get_next_move(), (1, 1))

    def test_state_6(self):
        bs = [['o', 'x', 'x'],
              ['x', ' ', ' '],
              ['x', 'o', 'o']]

        g = TicTacToeAI(bs, 'o')
        self.assertEqual(g.get_next_move(), (1, 1))

    def test_state_7(self):
        bs = [['x', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]

        g = TicTacToeAI(bs, 'o')
        self.assertIn(g.get_next_move(), [(0, 1), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])

    def test_state_8(self):
        # loose position
        bs = [['x', ' ', 'x'],
              [' ', 'o', 'x'],
              ['o', ' ', ' ']]

        g = TicTacToeAI(bs, 'o')
        self.assertIn(g.get_next_move(), [(0, 1), (1, 0), (2, 1), (2, 2)])

    def test_state_9(self):
        bs = [['x', ' ', ' '],
              [' ', 'o', ' '],
              [' ', ' ', 'x']]

        g = TicTacToeAI(bs, 'o')
        for _ in range(10):
            self.assertIn(g.get_next_move(), [(0, 1), (1, 0), (1, 2), (2, 1)])

    def test_state_10(self):
        # draw state
        bs = [['x', 'x', 'o'],
              ['o', 'o', 'x'],
              ['x', ' ', ' ']]

        g = TicTacToeAI(bs, 'o')
        self.assertIn(g.get_next_move(), [(2, 1), (2, 2)])

    def test_state_11(self):
        # draw state
        bs = [[' ', ' ', ' '],
              [' ', 'o', ' '],
              ['x', 'o', 'x']]

        g = TicTacToeAI(bs, 'x')
        self.assertEqual(g.get_next_move(), (0, 1))

    def test_state_12(self):
        bs = [['x', 'o', 'x'],
              [' ', 'x', 'o'],
              ['o', ' ', ' ']]

        g = TicTacToeAI(bs, 'x')
        for _ in range(10):
            self.assertEqual(g.get_next_move(), (2, 2))

    def test_state_13(self):
        bs = [['x', 'o', 'x'],
              ['o', 'x', 'o'],
              ['o', ' ', ' ']]

        g = TicTacToeAI(bs, 'x')
        self.assertEqual(g.get_next_move(), (2, 2))
