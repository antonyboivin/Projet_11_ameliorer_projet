from django.db import models
from django.contrib.auth.models import User


class Heading(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    heading = models.ForeignKey(Heading, on_delete=models.CASCADE, related_name='topics')
    starter = models.CharField(max_length=150)

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=150)
    updated_by = models.CharField(max_length=150)
    

    def __str__(self):
        return self.message