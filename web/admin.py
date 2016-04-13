from django.contrib import admin

from web.models import Player, Game, Move


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['username', 'type']


class GameAdmin(admin.ModelAdmin):
    list_display = ['player1', 'player2', 'date_started', 'result']


class MoveAdmin(admin.ModelAdmin):
    list_display = ['game', 'player', 'sequence_no', 'x', 'y']
    list_filter = ['game']


admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Move, MoveAdmin)
