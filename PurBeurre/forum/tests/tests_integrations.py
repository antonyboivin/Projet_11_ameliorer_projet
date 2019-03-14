from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from ..models import Heading, Topic, Post


# At first, I check that all pages of the application are functional.
class StatusCodePages(TestCase):
    """
        Class StatusCodePages ensures that all templates return a status code 200.
    """
    def setUp(self):
        self.heading = Heading.objects.create(name='Django', description='Django board.')
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        self.topic = Topic.objects.create(subject='Hello, world', heading=self.heading, starter=user)
        Post.objects.create(message='Lorem ipsum dolor sit amet', topic=self.topic, created_by=user)

    def test_home_view_status_code(self):
        response = self.client.get(reverse('forum'))
        self.assertEqual(response.status_code, 200)

    def test_forum_topics_view_status_code(self):
        response = self.client.get(reverse('forum topics', kwargs={'pk':1}))
        self.assertEqual(response.status_code, 200)

    def test_new_topic_view_status_code(self):
        response = self.client.get(reverse('new topic', kwargs={'pk':1}))
        self.assertEqual(response.status_code, 200)

    def test_topic_posts_view_status_code(self):
        response = self.client.get(reverse('topic posts', kwargs={'pk': self.heading.pk, 'topic_pk': self.topic.pk}))
        self.assertEqual(response.status_code, 200)

    def test_reply_topic_view_status_code(self):
        response = self.client.get(reverse('reply topic', kwargs={'pk': self.heading.pk, 'topic_pk': self.topic.pk}))
        self.assertEqual(response.status_code, 200)
