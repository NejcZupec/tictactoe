from django.http import Http404, HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect, render

from .models import Game
from .utils import create_new_game


class HomeView(TemplateView):
    template_name = 'home.html'


class GameView(TemplateView):
    template_name = 'game.html'

    def get(self, request, game_id, *args, **kwargs):
        game = Game.objects.get(id=game_id)

        board = {
            "row0": [game.get_field_state(0, i) for i in range(3)],
            "row1": [game.get_field_state(1, i) for i in range(3)],
            "row2": [game.get_field_state(2, i) for i in range(3)],
        }

        game_finished = True if game.get_winner_or_draw() else False

        return render(request, self.template_name, locals())


def new_game(request, p1_type, p2_type):
    """
    Start a new game. Create a Game object and redirects to it.
    """
    if p1_type == 'anonymous' and p2_type == 'anonymous':
        game = create_new_game('anonymous', 'anonymous')
        return redirect(game)

    if p1_type == 'anonymous' and p2_type == 'ai_random':
        game = create_new_game('anonymous', 'ai_random')
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
