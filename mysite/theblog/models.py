from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = HTMLField()
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} | {self.author}'

    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str___(self):
        return '%s - %s' % (self.post.title, self.name)