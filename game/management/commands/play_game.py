from django.core.management.base import BaseCommand

from game.game import Game


class Command(BaseCommand):

    def handle(self, *args, **options):

        # start a new game
        g = Game()
        g.print_board()

        while True:
            player = 'x' if len(g.moves) % 2 == 0 else 'o'
            print "Player %c:" % player

            x = int(raw_input("Enter x-coordinate: "))
            y = int(raw_input("Enter y-coordinate: "))

            try:
                g.move(player, x, y)
            except AssertionError, msg:
                print "-----------\n%s\n-----------" % msg

            g.print_board()

            end_game_status = g.get_winner_or_draw()

            if end_game_status:
                if end_game_status == 'draw':
                    print "Draw."
                else:
                    print "Player %c wins." % end_game_status
                break



