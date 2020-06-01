from django.db import models
from django.utils import timezone

from authors.models import Author
from categories.models import Category
from user.models import UserProfile

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    book_image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    # created = models.DateTimeField(default=timezone.now, null=True, blank=True)
    publish_date = models.DateField(default=timezone.now)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    order_date = models.DateField(null=True)
    payment_type = models.CharField(max_length=100, null=True)
    payment_id = models.CharField(max_length=100, null=True)


class BookOrder(models.Model):
    book = models.ForeignKey(Book)
    cart = models.ForeignKey(Cart)
    quantity = models.IntegerField()