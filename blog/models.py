from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(default='default.jpeg', upload_to='post_image/')

    def __str__(self):
        return self.title

