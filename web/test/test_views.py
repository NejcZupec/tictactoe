from django.core.urlresolvers import reverse
from django.test import TestCase


class HomePageTest(TestCase):

    def test_home_page_renders_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_has_title_tic_tac_toe(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Tic Tac Toe</a>")
