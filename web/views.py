from django.http import Http404
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

        return render(request, self.template_name, {'game': game})


def new_game(request, p1_type, p2_type):

    if p1_type == 'anonymous' and p2_type == 'anonymous':
        game = create_new_game('anonymous', 'anonymous')
        return redirect(game)

    if p1_type == 'anonymous' and p2_type == 'ai_random':
        game = create_new_game('anonymous', 'ai_random')
        return redirect(game)

    raise Http404


