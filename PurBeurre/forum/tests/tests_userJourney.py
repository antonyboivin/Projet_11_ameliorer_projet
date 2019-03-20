from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Heading
from ..views import forum, forum_topics

class Userjourney(TestCase):
    def setUp(self):
        self.heading = Heading.objects.create(name='Django', description='Django forum.')
        url = reverse('forum')
        self.response = self.client.get(url)

    def test_home_page(self):
        """
        As Boby I have to be able to access the site by entering the URL in my browser.
        En tant que Boby je dois pouvoir accéder au site en rentrant l'URL dans mon navigateur.
        """
        view = resolve('/forum/')
        self.assertEquals(view.func, forum)

    def test_home_view_contains_link_to_topics_page(self):
        """
        En tant que Boby, je dois avoir acces aux liens des topics des forums.
        As Boby, I need to have access to the forum topics links.
        """
        heading_topics_url = reverse('forum topics', kwargs={'pk': self.heading.pk})
        self.assertContains(self.response, 'href="{0}"'.format(heading_topics_url))

    def test_forum_topics_url_resolves_forum_topics_view(self):
        """
        qsdqsd
        """
        view = resolve('/forum/1/')
        self.assertEquals(view.func, forum_topics)

    def test_forum_topics_view_contains_navigation_links(self):
        heading_topics_url = reverse('forum topics', kwargs={'pk': 1})
        homepage_url = reverse('forum')
        new_topic_url = reverse('new topic', kwargs={'pk': 1})
        response = self.client.get(heading_topics_url)
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))
