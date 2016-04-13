from django.test import TestCase

from web.models import Player
from web.utils import generate_unique_anonymous_username


class GenerateUniqueAnonymousUsernameTest(TestCase):

    def setUp(self):
        self.player = Player.objects.create(
            username=generate_unique_anonymous_username(),
            type='anonymous',
        )

    def test_two_generated_usernames_shouldnt_be_the_same(self):
        username1 = generate_unique_anonymous_username()
        username2 = generate_unique_anonymous_username()

        self.assertNotEqual(username1, username2)

    def test_generated_username_is_not_in_db(self):
        username = generate_unique_anonymous_username()

        self.assertNotEqual(self.player.username, username)
