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

    username = models.CharField(max_length=255)
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
    result = models.CharField(max_length=15, choices=RESULT)

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
