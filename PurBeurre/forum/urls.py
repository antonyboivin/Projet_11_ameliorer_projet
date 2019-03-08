from django.urls import path, re_path
from django.contrib import admin

from . import views


urlpatterns = [
    path('forum/', views.forum, name='forum'),
    re_path(r'^forum/(?P<pk>\d+)/$', views.forum_topics, name='forum topics'),
    re_path(r'^forum/(?P<pk>\d+)/new/$', views.new_topic, name='new topic'),
    re_path(r'^forum/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic posts'),
    re_path(r'^forum/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply topic'),
]