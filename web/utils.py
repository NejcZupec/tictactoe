from django.utils.crypto import get_random_string

from .models import Player, Game


def generate_unique_anonymous_username():
    """
    Generate an unique username for a player. Check in database if the username already exists.
    TODO: check in db if a user with the generated username already exists
    """
    unique_id = get_random_string(length=12)
    new_username = "user_%s" % unique_id
    return new_username


def create_new_game(p1_type, p2_type):
    player1 = Player.objects.create(username=generate_unique_anonymous_username(), type=p1_type)
    player2 = Player.objects.create(username=generate_unique_anonymous_username(), type=p2_type)

    return Game.objects.create(player1=player1, player2=player2)
