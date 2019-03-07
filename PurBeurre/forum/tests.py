from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import forum, forum_topics
from .models import Heading


class HomeTests(TestCase):
    def setUp(self):
        self.heading = Heading.objects.create(name='PurBeurre_Forum', description='Nice tests for my Pur Beurre Django forum app.')
        url = reverse('forum')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)
    
    def test_home_url_resolves_home_view(self):
        view = resolve('/forum/')
        self.assertEquals(view.func, forum)
    
    def test_home_view_contains_link_to_topics_page(self):
        forum_topics_url = reverse('forum topics', kwargs={'pk': self.heading.pk})
        self.assertContains(self.response, 'href="{0}"'.format(forum_topics_url))


class HeadingTopicsTests(TestCase):
    def setUp(self):
        Heading.objects.create(name='PurBeurre_Forum', description='Nice tests for my Pur Beurre Django forum app.')
 
    def test_b_forum_topics_view_success_status_code(self):
        url = reverse('forum topics', kwargs={'pk' : 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
   
    def test_c_forum_topics_view_not_found_status_code(self):
        url = reverse('forum topics', kwargs={'pk' : 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_d_forum_topics_url_resolves_forum_topics_view(self):
        view = resolve('/forum/1/')
        self.assertEquals(view.func, forum_topics)

    def test_a_heading_topics_view_contains_link_back_to_homepage(self):
        forum_topics_url = reverse('forum topics', kwargs={'pk': 1})
        response = self.client.get(forum_topics_url)
        homepage_url = reverse('forum')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))



