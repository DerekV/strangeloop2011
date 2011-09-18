from django.db import models
from yabl.authors.models import Author

class Entry(models.Model):
    author = models.ForeignKey(Author)
    pub_date = models.DateTimeField()
    is_published = models.BooleanField()
    headline = models.CharField(max_length=200)
    slug = models.SlugField()
    summary = models.TextField()
    body = models.TextField()
