from django.db import models

# Create your models here.
class NewsAndUpdate(models.Model):
    source = models.CharField(max_length=40)
    title = models.CharField(max_length=100, primary_key=True)
    description = models.TextField(max_length=1000)
    url = models.URLField(max_length=200)
    url_image = models.URLField(max_length=200)
    published_time = models.CharField(max_length=100)
    content = models.TextField(max_length=100000)

    def __str__(self):
        return self.title
