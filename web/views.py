import json

from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
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

        return render(request, self.template_name, {
            'game': Game.objects.get(id=game_id),
            'board': [[game.get_field_state(row_idx, column_idx) for column_idx in range(3)] for row_idx in range(3)],
            'game_finished': True if game.get_winner_or_draw() else False,
            'ai_player': game.get_ai_player(),
            'stats': calculate_stats(game),
            'online_game': 'false',
        })


class GameOnlineView(TemplateView):
    template_name = 'game.html'

    def get(self, request, game_id, *args, **kwargs):
        game = Game.objects.get(id=game_id)
        username = request.GET.get('player')
        url = '%s?player=%s' % (reverse('online_game', args=[game.id]), game.player2.username)

        return render(request, self.template_name, {
            'board': [[game.get_field_state(row_idx, column_idx) for column_idx in range(3)] for row_idx in range(3)],
            'game_finished': True if game.get_winner_or_draw() else False,
            'ai_player': game.get_ai_player(),
            'stats': calculate_stats(game),
            'username': username,
            'show_online_modal_window': True if username == game.player1.username and game.move_set.count() == 0 else False,
            'online_game_opponent_url': request.build_absolute_uri(url),
            'online_game': 'true',
        })


class Leaderboard(TemplateView):
    template_name = 'leaderboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'players': Player.objects.all(),
        })


def new_game(request, p1_type, p2_type):
    """
    Start a new game. Create a Game object and redirects to it.
    """
    if p1_type == 'anonymous' and p2_type == 'anonymous':
        game = create_new_game('anonymous', 'anonymous')
        return redirect(game)

    if p1_type == 'anonymous' and p2_type == 'ai_random':
        player1 = Player.objects.create(username=generate_unique_anonymous_username(), type=p1_type)
        player2, _ = Player.objects.get_or_create(username="AI Random", type=p2_type)
        game = Game.objects.create(player1=player1, player2=player2)
        return redirect(game)

    if p1_type == 'anonymous' and p2_type == 'ai_min_max':
        player1 = Player.objects.create(username=generate_unique_anonymous_username(), type=p1_type)
        player2, _ = Player.objects.get_or_create(username="AI MiniMax", type=p2_type)
        game = Game.objects.create(player1=player1, player2=player2)
        return redirect(game)

    raise Http404


def new_online_game(request, p1_type, p2_type):

    if p1_type == 'anonymous' and p2_type == 'anonymous':
        player1 = Player.objects.create(username=generate_unique_anonymous_username(), type=p1_type)
        player2 = Player.objects.create(username=generate_unique_anonymous_username(), type=p2_type)
        game = Game.objects.create(player1=player1, player2=player2)

        url = '%s?player=%s' % (reverse('online_game', args=[game.id]), player1.username)
        return redirect(url)

    raise Http404


@csrf_exempt
def new_move(request, game_id):
    """
    Save a new game's move to database.
    """
    game = Game.objects.get(id=game_id)
    player = request.POST.get('player')
    x = request.POST.get('x')
    y = request.POST.get('y')

    _, action = game.add_move_and_get_action(player, x, y)

    return HttpResponse(str(action))


def rematch(request, game_id):
    old_game = Game.objects.get(id=game_id)

    game = Game.objects.create(
        player1=old_game.player2,
        player2=old_game.player1,
    )

    return redirect(game)


@csrf_exempt
def ai_next_move(request, game_id):
    game = Game.objects.get(id=game_id)

    if game.get_ai_player_type() == 'ai_random':
        x, y = game.get_next_random_move()
    else:
        x, y = game.get_next_minimax_move()

    return HttpResponse(json.dumps({'x': x, 'y': y}), content_type='application/json')
