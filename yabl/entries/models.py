from django.db import models
from yabl.authors.models import AUthor

class Entry(model.Model):
    author = models.ForeinKey(Author)
    pub_date = models.DateTimeField()
    is_published = models.BooleanField()
    headline = models.CharField(max_length=200)
    slug = models.SlugField()
    summary = models.TextField()
    body = models.TextField()
