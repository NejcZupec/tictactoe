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

    def test_already_played_move_cant_be_played_again(self):
        g = Game()

        g.move('o', 1, 1)
        with self.assertRaises(AssertionError):
            g.move('x', 1, 1)

    def test_consecutive_moves_not_the_same_player(self):
        g = Game()

        g.move('x', 0, 0)
        with self.assertRaises(AssertionError):
            g.move('x', 1, 0)

    def test_illegal_players(self):
        g = Game()

        with self.assertRaises(AssertionError):
            g.move('d', 0, 0)

        with self.assertRaises(AssertionError):
            g.move(' ', 0, 0)

        with self.assertRaises(AssertionError):
            g.move('-', 0, 0)

    def test_moves(self):
        g = Game()
        m1 = ('o', 1, 1)
        m2 = ('x', 2, 2)
        m3 = ('o', 0, 1)

        g.move(*m1)
        g.move(*m2)
        g.move(*m3)
        self.assertListEqual([m1, m2, m3], g.moves)

    def test_is_game_ended(self):
        # game 1 - diagonal win
        g = Game()
        g.move('x', 0, 0)
        g.move('o', 0, 1)
        g.move('x', 1, 1)
        g.move('o', 1, 2)
        self.assertFalse(g.is_game_ended(), "Game is not ended yet.")
        g.move('x', 2, 2)
        self.assertTrue(g.is_game_ended(), "Game should ended - diagonal win.")

        # game 2 - horizontal win
        g = Game()
        g.move('x', 0, 0)
        g.move('o', 1, 1)
        g.move('x', 0, 1)
        g.move('o', 1, 2)
        self.assertFalse(g.is_game_ended(), "Game is not ended yet.")
        g.move('x', 0, 2)
        self.assertTrue(g.is_game_ended(), "Game should ended - horizontal win.")

        # game 3 - vertical win
        g = Game()
        g.move('x', 0, 0)
        g.move('o', 0, 1)
        g.move('x', 1, 0)
        g.move('o', 1, 1)
        self.assertFalse(g.is_game_ended(), "Game is not ended yet.")
        g.move('x', 2, 0)
        self.assertTrue(g.is_game_ended(), "Game should ended - vertical win.")

        # game 4 - more than 5 moves
        g = Game()
        g.move('x', 0, 0)
        g.move('o', 0, 1)
        g.move('x', 1, 1)
        g.move('o', 1, 2)
        g.move('x', 2, 1)
        g.move('o', 0, 2)
        self.assertFalse(g.is_game_ended(), "Game is not ended yet.")
        g.move('x', 2, 2)
        self.assertTrue(g.is_game_ended(), "Game should ended - vertical win.")




