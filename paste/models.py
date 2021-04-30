from django.db import models

# Create your models here.


class Markdown(models.Model):
    url = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url