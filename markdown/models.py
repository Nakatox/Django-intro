from django.db import models

# Create your models here.


class Markdown(models.Model):
    url = models.CharField(max_length=128)
    content = models.TextField()