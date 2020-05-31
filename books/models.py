from django.db import models
from django.utils import timezone

from authors.models import Author
from categories.models import Category


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    book_image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.IntegerField()
    created = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.title
