from django.core.management.base import BaseCommand

from game.game import Game


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--first_player',
            default='x',
            help="Set which player should start ('x' or 'o')",
        )

    def handle(self, *args, **options):
        player = options['first_player']

        # start a new game
        g = Game()
        g.print_board()

        while True:
            print "Player %c" % player

            x = self.get_input("Enter x-coordinate: ")
            if x is None:
                continue

            y = self.get_input("Enter y-coordinate: ")
            if y is None:
                continue

            try:
                g.move(player, x, y)
                g.print_board()

                end_game_status = g.get_winner_or_draw()

                if end_game_status:
                    if end_game_status == 'draw':
                        print "Draw."
                    else:
                        print "Player %c wins." % end_game_status
                    break

                # change player
                player = 'o' if player == 'x' else 'x'

            except AssertionError, msg:
                print "-----------\n%s\n-----------" % msg

    @staticmethod
    def get_input(msg):
        try:
            return int(raw_input(msg))
        except ValueError:
            print "-----------\n%s\n-----------" % "Only integer is accepted."
            return
