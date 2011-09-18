from django.db import models

class Author(model.Model):
    author = models.ForeinKey(max_length)
    pub_date = models.DateTimeField()
    is_published = models.BooleanField()
    headline = models.CharField(max_length=200)
    slug = models.SlugField()
    summary = models.TextField()
    body = models.TextField()
