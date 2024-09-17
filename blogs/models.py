from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
class Blogs(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    new_slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.title + " by " + self.author.username
