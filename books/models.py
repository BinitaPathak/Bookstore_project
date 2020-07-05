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
    publish_date = models.DateField(default=timezone.now)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    order_date = models.DateField(default=timezone.now)
    # payment_type = models.CharField(max_length=100, null=True)
    # payment_id = models.CharField(max_length=100, null=True)

    # def add_to_cart(self, book_id):
    #     book = Book.objects.get(pk=book_id)
    #     try:
    #         preexisting_order = BookOrder.objects.get(book=book, cart=self)
    #         preexisting_order.quantity += 1
    #         preexisting_order.save()
    #     except BookOrder.DoesNotExist:
    #         new_order = BookOrder.objects.create(
    #             book=book,
    #             cart=self,
    #             quantity=1
    #         )
    #         new_order.save()
    #
    # def remove_from_cart(self, book_id):
    #     book = Book.objects.get(pk=book_id)
    #     try:
    #         preexisting_order = BookOrder.objects.get(book=book, cart=self)
    #         if preexisting_order.quantity > 1:
    #             preexisting_order.quantity -= 1
    #             preexisting_order.save()
    #         else:
    #             preexisting_order.delete()
    #     except BookOrder.DoesNotExist:
    #         pass


class BookOrder(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
