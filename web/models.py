from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Player(models.Model):
    """
    TicTacToe player.
    """

    PLAYER_TYPE = (
        ('ai_random', 'AI Random'),
        ('ai_min_max', 'AI MinMax'),
        ('anonymous', 'Anonymous'),
        ('registered', 'Registered'),
    )

    username = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=15, choices=PLAYER_TYPE)

    def __unicode__(self):
        return 'Player (username=%s, type=%s)' % (self.username, self.type)


class Game(models.Model):
    """
    Game container. Player1 has always crosses and she starts first.
    """

    RESULT = (
        ('win1', 'Player 1 wins'),
        ('win2', 'Player 2 wins'),
        ('draw', 'Draw'),
        ('in_progress', 'In progress'),
    )

    player1 = models.ForeignKey('web.Player', related_name='player1')  # cross
    player2 = models.ForeignKey('web.Player', related_name='player2')  # circle
    date_started = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=15, choices=RESULT, default='in_progress')

    def get_absolute_url(self):
        return reverse('game', args=[self.id])

    def add_move(self, player, x, y):
        """
        Save move to database.
        player = p1 or p2
        """
        return Move.objects.create(
            game=self,
            player=self.player1 if player == 'p1' else self.player2,
            sequence_no=self.get_next_move_sequence_number(),
            x=x,
            y=y,
        )

    def add_move_and_get_action(self, player, x, y):
        """
        A wrapper for the add_move function. It adds action and returns move and action as a tuple.
        """
        m = self.add_move(player, x, y)
        return m, self.get_winner_or_draw()

    def get_last_move(self):
        return self.move_set.latest('sequence_no')

    def get_next_move_sequence_number(self):
        if self.move_set.count() == 0:
            return 1
        return self.get_last_move().sequence_no + 1

    def get_board_2d_and_moves(self):
        """
        Generates board and moves variables, suitable for the Game class (game.game.Game).
        """

        # create an empty 2D board
        board = [[' ' for _ in range(3)] for _ in range(3)]
        moves = []

        # fill the board with the current state
        for m in self.move_set.all().order_by('sequence_no'):
            p = 'x' if m.player == self.player1 else 'o'
            board[m.x][m.y] = p
            moves.append((p, m.x, m.y))

        return board, moves

    def get_winner_or_draw(self):
        """
        Returns:
         - 'None' - if game is not finished yet
         - 'draw' - draw game
         - 'x' - player 1 wins
         - 'o' - player 2 wins
        """
        from game.game import Game
        board, moves = self.get_board_2d_and_moves()
        g = Game(board=board, moves=moves)
        return g.get_winner_or_draw()

    def __unicode__(self):
        return 'Game (%s vs. %s, result=%s)' % (self.player1.username, self.player2.username, self.result)


class Move(models.Model):
    """
    Player's move.
    """

    game = models.ForeignKey('web.Game')
    player = models.ForeignKey('web.Player')
    sequence_no = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    x = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])
    y = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])

    def __unicode__(self):
        return 'Move (player=%s, x=%d, y=%d)' % (self.player.username, self.x, self.y)
