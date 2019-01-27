from django.urls import reverse
from django.test import TestCase
from .views import forum

class HomeTests(TestCase):
    def test_forum_view_status_code(self):
        url = reverse('forum')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_forum_page(self):
        response = self.client.get(reverse('forum'))
        self.assertTemplateUsed(response, 'forum/forum_home_page.html')