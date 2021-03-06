from django.utils.crypto import get_random_string

from .models import Player, Game


def generate_unique_anonymous_username():
    """
    Generate an unique username for a player. Check in database if the username already exists.
    TODO: check in db if a user with the generated username already exists
    """
    unique_id = get_random_string(length=10)
    new_username = "u_%s" % unique_id
    return new_username


def create_new_game(p1_type, p2_type):
    """
    Generate two random players and create a new Game instance.
    """
    player1 = Player.objects.create(username=generate_unique_anonymous_username(), type=p1_type)
    player2 = Player.objects.create(username=generate_unique_anonymous_username(), type=p2_type)
    return Game.objects.create(player1=player1, player2=player2)


def calculate_stats(game):
    return {
        1: {
            "win": game.player1.win_against_player(game.player2),
            "lose": game.player1.loose_against_player(game.player2),
            "draw": game.player1.draw_against_player(game.player2),
        },
        2: {
            "win": game.player2.win_against_player(game.player1),
            "lose": game.player2.loose_against_player(game.player1),
            "draw": game.player2.draw_against_player(game.player1),
        }
    }
