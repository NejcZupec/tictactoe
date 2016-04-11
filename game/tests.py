from django.test import TestCase

from game import Game


class GameTest(TestCase):

    def test_initial_board(self):
        g = Game()
        self.assertEqual(g.board, [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

    def test_print_board(self):
        pass

    def test_move(self):
        g = Game()

        g.move('o', 0, 0)
        self.assertEqual(g.board, [['o', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

        g.move('x', 1, 0)
        self.assertEqual(g.board, [['o', ' ', ' '], ['x', ' ', ' '], [' ', ' ', ' ']])

        g.move('o', 2, 2)
        self.assertEqual(g.board, [['o', ' ', ' '], ['x', ' ', ' '], [' ', ' ', 'o']])

        g.move('x', 1, 2)
        self.assertEqual(g.board, [['o', ' ', ' '], ['x', ' ', 'x'], [' ', ' ', 'o']])

    def test_illegal_moves(self):
        g = Game()

        with self.assertRaises(AssertionError):
            g.move('o', 5, 0)

        with self.assertRaises(AssertionError):
            g.move('o', -1, 0)

        with self.assertRaises(AssertionError):
            g.move('o', 0, -1)

        with self.assertRaises(AssertionError):
            g.move('o', 0, 5)

    def test_illegal_players(self):
        g = Game()

        with self.assertRaises(AssertionError):
            g.move('d', 0, 0)

        with self.assertRaises(AssertionError):
            g.move(' ', 0, 0)

        with self.assertRaises(AssertionError):
            g.move('-', 0, 0)


