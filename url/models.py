from django.db import models

class UrlData(models.Model):
    url = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=15, unique=True)
    def __str__(self):
            return f"Short Url for: {self.url} is {self.slug}"