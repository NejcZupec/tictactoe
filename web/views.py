import json

from django.http import Http404, HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect, render

from .models import Game, Player
from .utils import create_new_game, generate_unique_anonymous_username, calculate_stats


class HomeView(TemplateView):
    template_name = 'home.html'


class GameView(TemplateView):
    template_name = 'game.html'

    def get(self, request, game_id, *args, **kwargs):
        game = Game.objects.get(id=game_id)
        board = [[game.get_field_state(row_index, column_index) for column_index in range(3)] for row_index in range(3)]
        game_finished = True if game.get_winner_or_draw() else False
        ai_player = game.get_ai_player()
        stats = calculate_stats(game)

        return render(request, self.template_name, locals())


def new_game(request, p1_type, p2_type):
    """
    Start a new game. Create a Game object and redirects to it.
    """
    if p1_type == 'anonymous' and p2_type == 'anonymous':
        game = create_new_game('anonymous', 'anonymous')
        return redirect(game)

    if p1_type == 'anonymous' and p2_type == 'ai_random':
        player1 = Player.objects.create(username=generate_unique_anonymous_username(), type=p1_type)
        player2, created = Player.objects.get_or_create(username="AI Random", type=p2_type)
        game = Game.objects.create(player1=player1, player2=player2)
        return redirect(game)

    raise Http404


def new_move(request, game_id):
    """
    Save a new game's move to database.
    """
    game = Game.objects.get(id=game_id)
    player = request.POST.get('player')
    x = request.POST.get('x')
    y = request.POST.get('y')

    m, action = game.add_move_and_get_action(player, x, y)

    return HttpResponse(str(action))


def rematch(request, game_id):
    old_game = Game.objects.get(id=game_id)

    game = Game.objects.create(
        player1=old_game.player2,
        player2=old_game.player1,
    )

    return redirect(game)


def ai_next_move(request, game_id):
    game = Game.objects.get(id=game_id)
    x, y = game.get_next_random_move()

    return HttpResponse(json.dumps({'x': x, 'y': y}), content_type='application/json')
