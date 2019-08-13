from django.db import models
from django.urls import reverse

class Post(models.Model):
    text = models.CharField(max_length=50,verbose_name='')
    completed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('todo')
