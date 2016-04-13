"""tictactoe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from web import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.HomeView.as_view(), name='home'),

    url(r'^game/(?P<game_id>\d+)$', views.GameView.as_view(), name='game'),
    url(r'^game/(?P<game_id>\d+)/ai/move/$', views.ai_next_move, name='ai_next_move'),
    url(r'^game/(?P<game_id>\d+)/rematch$', views.rematch, name='rematch'),
    url(r'^game/(?P<game_id>\d+)/move/new', views.new_move, name='new_move'),
    url(r'^game/new/(?P<p1_type>\w+)/(?P<p2_type>\w+)$', views.new_game, name='new_game'),

    url(r'leaderboard/$', views.Leaderboard.as_view(), name='leaderboard'),
]
