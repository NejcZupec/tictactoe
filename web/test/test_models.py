from django.test import TestCase

from web.models import Player, Game, Move


class PlayerGameMoveModelTest(TestCase):

    def setUp(self):

        # generate players
        self.player1 = Player.objects.create(username='anonymous1', type='anonymous')
        self.player2 = Player.objects.create(username='anonymous2', type='anonymous')

        # start game
        self.game = Game.objects.create(
            player1=self.player1,
            player2=self.player2,
            result='in_progress',
        )

    def test_player_one_starts(self):
        pass

    def test_player_two_cant_start(self):
        pass

    def test_one_game_can_have_max_nine_moves(self):
        pass

    def test_get_next_move_sequence_number(self):
        m1 = self.game.add_move('p1', 0, 0)
        self.assertEqual(m1.sequence_no, 1)

        m2 = self.game.add_move('p2', 1, 1)
        self.assertEqual(m2.sequence_no, 2)

        self.assertEqual(Move.objects.filter(game=self.game).count(), 2)
